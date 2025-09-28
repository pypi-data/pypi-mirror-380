# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_savingsplans import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class DeleteQueuedSavingsPlanRequest:
    boto3_raw_data: "type_defs.DeleteQueuedSavingsPlanRequestTypeDef" = (
        dataclasses.field()
    )

    savingsPlanId = field("savingsPlanId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteQueuedSavingsPlanRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQueuedSavingsPlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlanRateFilter:
    boto3_raw_data: "type_defs.SavingsPlanRateFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsPlanRateFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlanRateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlanOfferingRateFilterElement:
    boto3_raw_data: "type_defs.SavingsPlanOfferingRateFilterElementTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SavingsPlanOfferingRateFilterElementTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlanOfferingRateFilterElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlanOfferingFilterElement:
    boto3_raw_data: "type_defs.SavingsPlanOfferingFilterElementTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SavingsPlanOfferingFilterElementTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlanOfferingFilterElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlanFilter:
    boto3_raw_data: "type_defs.SavingsPlanFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SavingsPlanFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlanFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlan:
    boto3_raw_data: "type_defs.SavingsPlanTypeDef" = dataclasses.field()

    offeringId = field("offeringId")
    savingsPlanId = field("savingsPlanId")
    savingsPlanArn = field("savingsPlanArn")
    description = field("description")
    start = field("start")
    end = field("end")
    state = field("state")
    region = field("region")
    ec2InstanceFamily = field("ec2InstanceFamily")
    savingsPlanType = field("savingsPlanType")
    paymentOption = field("paymentOption")
    productTypes = field("productTypes")
    currency = field("currency")
    commitment = field("commitment")
    upfrontPaymentAmount = field("upfrontPaymentAmount")
    recurringPaymentAmount = field("recurringPaymentAmount")
    termDurationInSeconds = field("termDurationInSeconds")
    tags = field("tags")
    returnableUntil = field("returnableUntil")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SavingsPlanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SavingsPlanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

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
class ParentSavingsPlanOffering:
    boto3_raw_data: "type_defs.ParentSavingsPlanOfferingTypeDef" = dataclasses.field()

    offeringId = field("offeringId")
    paymentOption = field("paymentOption")
    planType = field("planType")
    durationSeconds = field("durationSeconds")
    currency = field("currency")
    planDescription = field("planDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParentSavingsPlanOfferingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParentSavingsPlanOfferingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReturnSavingsPlanRequest:
    boto3_raw_data: "type_defs.ReturnSavingsPlanRequestTypeDef" = dataclasses.field()

    savingsPlanId = field("savingsPlanId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReturnSavingsPlanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReturnSavingsPlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlanOfferingProperty:
    boto3_raw_data: "type_defs.SavingsPlanOfferingPropertyTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsPlanOfferingPropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlanOfferingPropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlanOfferingRateProperty:
    boto3_raw_data: "type_defs.SavingsPlanOfferingRatePropertyTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SavingsPlanOfferingRatePropertyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlanOfferingRatePropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlanRateProperty:
    boto3_raw_data: "type_defs.SavingsPlanRatePropertyTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsPlanRatePropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlanRatePropertyTypeDef"]
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

    resourceArn = field("resourceArn")
    tags = field("tags")

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
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

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
class CreateSavingsPlanRequest:
    boto3_raw_data: "type_defs.CreateSavingsPlanRequestTypeDef" = dataclasses.field()

    savingsPlanOfferingId = field("savingsPlanOfferingId")
    commitment = field("commitment")
    upfrontPaymentAmount = field("upfrontPaymentAmount")
    purchaseTime = field("purchaseTime")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSavingsPlanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSavingsPlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSavingsPlanResponse:
    boto3_raw_data: "type_defs.CreateSavingsPlanResponseTypeDef" = dataclasses.field()

    savingsPlanId = field("savingsPlanId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSavingsPlanResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSavingsPlanResponseTypeDef"]
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

    tags = field("tags")

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
class ReturnSavingsPlanResponse:
    boto3_raw_data: "type_defs.ReturnSavingsPlanResponseTypeDef" = dataclasses.field()

    savingsPlanId = field("savingsPlanId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReturnSavingsPlanResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReturnSavingsPlanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSavingsPlanRatesRequest:
    boto3_raw_data: "type_defs.DescribeSavingsPlanRatesRequestTypeDef" = (
        dataclasses.field()
    )

    savingsPlanId = field("savingsPlanId")

    @cached_property
    def filters(self):  # pragma: no cover
        return SavingsPlanRateFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSavingsPlanRatesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSavingsPlanRatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSavingsPlansOfferingRatesRequest:
    boto3_raw_data: "type_defs.DescribeSavingsPlansOfferingRatesRequestTypeDef" = (
        dataclasses.field()
    )

    savingsPlanOfferingIds = field("savingsPlanOfferingIds")
    savingsPlanPaymentOptions = field("savingsPlanPaymentOptions")
    savingsPlanTypes = field("savingsPlanTypes")
    products = field("products")
    serviceCodes = field("serviceCodes")
    usageTypes = field("usageTypes")
    operations = field("operations")

    @cached_property
    def filters(self):  # pragma: no cover
        return SavingsPlanOfferingRateFilterElement.make_many(
            self.boto3_raw_data["filters"]
        )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSavingsPlansOfferingRatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSavingsPlansOfferingRatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSavingsPlansOfferingsRequest:
    boto3_raw_data: "type_defs.DescribeSavingsPlansOfferingsRequestTypeDef" = (
        dataclasses.field()
    )

    offeringIds = field("offeringIds")
    paymentOptions = field("paymentOptions")
    productType = field("productType")
    planTypes = field("planTypes")
    durations = field("durations")
    currencies = field("currencies")
    descriptions = field("descriptions")
    serviceCodes = field("serviceCodes")
    usageTypes = field("usageTypes")
    operations = field("operations")

    @cached_property
    def filters(self):  # pragma: no cover
        return SavingsPlanOfferingFilterElement.make_many(
            self.boto3_raw_data["filters"]
        )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSavingsPlansOfferingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSavingsPlansOfferingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSavingsPlansRequest:
    boto3_raw_data: "type_defs.DescribeSavingsPlansRequestTypeDef" = dataclasses.field()

    savingsPlanArns = field("savingsPlanArns")
    savingsPlanIds = field("savingsPlanIds")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    states = field("states")

    @cached_property
    def filters(self):  # pragma: no cover
        return SavingsPlanFilter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSavingsPlansRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSavingsPlansRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSavingsPlansResponse:
    boto3_raw_data: "type_defs.DescribeSavingsPlansResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def savingsPlans(self):  # pragma: no cover
        return SavingsPlan.make_many(self.boto3_raw_data["savingsPlans"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSavingsPlansResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSavingsPlansResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlanOffering:
    boto3_raw_data: "type_defs.SavingsPlanOfferingTypeDef" = dataclasses.field()

    offeringId = field("offeringId")
    productTypes = field("productTypes")
    planType = field("planType")
    description = field("description")
    paymentOption = field("paymentOption")
    durationSeconds = field("durationSeconds")
    currency = field("currency")
    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")

    @cached_property
    def properties(self):  # pragma: no cover
        return SavingsPlanOfferingProperty.make_many(self.boto3_raw_data["properties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsPlanOfferingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlanOfferingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlanOfferingRate:
    boto3_raw_data: "type_defs.SavingsPlanOfferingRateTypeDef" = dataclasses.field()

    @cached_property
    def savingsPlanOffering(self):  # pragma: no cover
        return ParentSavingsPlanOffering.make_one(
            self.boto3_raw_data["savingsPlanOffering"]
        )

    rate = field("rate")
    unit = field("unit")
    productType = field("productType")
    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")

    @cached_property
    def properties(self):  # pragma: no cover
        return SavingsPlanOfferingRateProperty.make_many(
            self.boto3_raw_data["properties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsPlanOfferingRateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlanOfferingRateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlanRate:
    boto3_raw_data: "type_defs.SavingsPlanRateTypeDef" = dataclasses.field()

    rate = field("rate")
    currency = field("currency")
    unit = field("unit")
    productType = field("productType")
    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")

    @cached_property
    def properties(self):  # pragma: no cover
        return SavingsPlanRateProperty.make_many(self.boto3_raw_data["properties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SavingsPlanRateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SavingsPlanRateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSavingsPlansOfferingsResponse:
    boto3_raw_data: "type_defs.DescribeSavingsPlansOfferingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def searchResults(self):  # pragma: no cover
        return SavingsPlanOffering.make_many(self.boto3_raw_data["searchResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSavingsPlansOfferingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSavingsPlansOfferingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSavingsPlansOfferingRatesResponse:
    boto3_raw_data: "type_defs.DescribeSavingsPlansOfferingRatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def searchResults(self):  # pragma: no cover
        return SavingsPlanOfferingRate.make_many(self.boto3_raw_data["searchResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSavingsPlansOfferingRatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSavingsPlansOfferingRatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSavingsPlanRatesResponse:
    boto3_raw_data: "type_defs.DescribeSavingsPlanRatesResponseTypeDef" = (
        dataclasses.field()
    )

    savingsPlanId = field("savingsPlanId")

    @cached_property
    def searchResults(self):  # pragma: no cover
        return SavingsPlanRate.make_many(self.boto3_raw_data["searchResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSavingsPlanRatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSavingsPlanRatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
