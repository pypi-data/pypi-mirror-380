# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_route53domains import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptDomainTransferFromAnotherAwsAccountRequest:
    boto3_raw_data: (
        "type_defs.AcceptDomainTransferFromAnotherAwsAccountRequestTypeDef"
    ) = dataclasses.field()

    DomainName = field("DomainName")
    Password = field("Password")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptDomainTransferFromAnotherAwsAccountRequestTypeDef"
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
                "type_defs.AcceptDomainTransferFromAnotherAwsAccountRequestTypeDef"
            ]
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
class DnssecSigningAttributes:
    boto3_raw_data: "type_defs.DnssecSigningAttributesTypeDef" = dataclasses.field()

    Algorithm = field("Algorithm")
    Flags = field("Flags")
    PublicKey = field("PublicKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DnssecSigningAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DnssecSigningAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillingRecord:
    boto3_raw_data: "type_defs.BillingRecordTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Operation = field("Operation")
    InvoiceId = field("InvoiceId")
    BillDate = field("BillDate")
    Price = field("Price")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BillingRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BillingRecordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelDomainTransferToAnotherAwsAccountRequest:
    boto3_raw_data: (
        "type_defs.CancelDomainTransferToAnotherAwsAccountRequestTypeDef"
    ) = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelDomainTransferToAnotherAwsAccountRequestTypeDef"
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
                "type_defs.CancelDomainTransferToAnotherAwsAccountRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckDomainAvailabilityRequest:
    boto3_raw_data: "type_defs.CheckDomainAvailabilityRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    IdnLangCode = field("IdnLangCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CheckDomainAvailabilityRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckDomainAvailabilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckDomainTransferabilityRequest:
    boto3_raw_data: "type_defs.CheckDomainTransferabilityRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    AuthCode = field("AuthCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CheckDomainTransferabilityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckDomainTransferabilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainTransferability:
    boto3_raw_data: "type_defs.DomainTransferabilityTypeDef" = dataclasses.field()

    Transferable = field("Transferable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainTransferabilityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainTransferabilityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Consent:
    boto3_raw_data: "type_defs.ConsentTypeDef" = dataclasses.field()

    MaxPrice = field("MaxPrice")
    Currency = field("Currency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConsentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConsentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtraParam:
    boto3_raw_data: "type_defs.ExtraParamTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtraParamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExtraParamTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainRequest:
    boto3_raw_data: "type_defs.DeleteDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTagsForDomainRequest:
    boto3_raw_data: "type_defs.DeleteTagsForDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    TagsToDelete = field("TagsToDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTagsForDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTagsForDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableDomainAutoRenewRequest:
    boto3_raw_data: "type_defs.DisableDomainAutoRenewRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisableDomainAutoRenewRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableDomainAutoRenewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableDomainTransferLockRequest:
    boto3_raw_data: "type_defs.DisableDomainTransferLockRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisableDomainTransferLockRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableDomainTransferLockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateDelegationSignerFromDomainRequest:
    boto3_raw_data: "type_defs.DisassociateDelegationSignerFromDomainRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateDelegationSignerFromDomainRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateDelegationSignerFromDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DnssecKey:
    boto3_raw_data: "type_defs.DnssecKeyTypeDef" = dataclasses.field()

    Algorithm = field("Algorithm")
    Flags = field("Flags")
    PublicKey = field("PublicKey")
    DigestType = field("DigestType")
    Digest = field("Digest")
    KeyTag = field("KeyTag")
    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DnssecKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DnssecKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PriceWithCurrency:
    boto3_raw_data: "type_defs.PriceWithCurrencyTypeDef" = dataclasses.field()

    Price = field("Price")
    Currency = field("Currency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PriceWithCurrencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PriceWithCurrencyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainSuggestion:
    boto3_raw_data: "type_defs.DomainSuggestionTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Availability = field("Availability")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainSuggestionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainSuggestionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainSummary:
    boto3_raw_data: "type_defs.DomainSummaryTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    AutoRenew = field("AutoRenew")
    TransferLock = field("TransferLock")
    Expiry = field("Expiry")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableDomainAutoRenewRequest:
    boto3_raw_data: "type_defs.EnableDomainAutoRenewRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableDomainAutoRenewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableDomainAutoRenewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableDomainTransferLockRequest:
    boto3_raw_data: "type_defs.EnableDomainTransferLockRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnableDomainTransferLockRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableDomainTransferLockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCondition:
    boto3_raw_data: "type_defs.FilterConditionTypeDef" = dataclasses.field()

    Name = field("Name")
    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactReachabilityStatusRequest:
    boto3_raw_data: "type_defs.GetContactReachabilityStatusRequestTypeDef" = (
        dataclasses.field()
    )

    domainName = field("domainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContactReachabilityStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactReachabilityStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainDetailRequest:
    boto3_raw_data: "type_defs.GetDomainDetailRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainDetailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainDetailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NameserverOutput:
    boto3_raw_data: "type_defs.NameserverOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    GlueIps = field("GlueIps")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NameserverOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NameserverOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainSuggestionsRequest:
    boto3_raw_data: "type_defs.GetDomainSuggestionsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    SuggestionCount = field("SuggestionCount")
    OnlyAvailable = field("OnlyAvailable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainSuggestionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainSuggestionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOperationDetailRequest:
    boto3_raw_data: "type_defs.GetOperationDetailRequestTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOperationDetailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOperationDetailRequestTypeDef"]
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
class SortCondition:
    boto3_raw_data: "type_defs.SortConditionTypeDef" = dataclasses.field()

    Name = field("Name")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OperationSummary:
    boto3_raw_data: "type_defs.OperationSummaryTypeDef" = dataclasses.field()

    OperationId = field("OperationId")
    Status = field("Status")
    Type = field("Type")
    SubmittedDate = field("SubmittedDate")
    DomainName = field("DomainName")
    Message = field("Message")
    StatusFlag = field("StatusFlag")
    LastUpdatedDate = field("LastUpdatedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OperationSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OperationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricesRequest:
    boto3_raw_data: "type_defs.ListPricesRequestTypeDef" = dataclasses.field()

    Tld = field("Tld")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListPricesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForDomainRequest:
    boto3_raw_data: "type_defs.ListTagsForDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Nameserver:
    boto3_raw_data: "type_defs.NameserverTypeDef" = dataclasses.field()

    Name = field("Name")
    GlueIps = field("GlueIps")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NameserverTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NameserverTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PushDomainRequest:
    boto3_raw_data: "type_defs.PushDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Target = field("Target")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PushDomainRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PushDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectDomainTransferFromAnotherAwsAccountRequest:
    boto3_raw_data: (
        "type_defs.RejectDomainTransferFromAnotherAwsAccountRequestTypeDef"
    ) = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectDomainTransferFromAnotherAwsAccountRequestTypeDef"
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
                "type_defs.RejectDomainTransferFromAnotherAwsAccountRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenewDomainRequest:
    boto3_raw_data: "type_defs.RenewDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    CurrentExpiryYear = field("CurrentExpiryYear")
    DurationInYears = field("DurationInYears")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RenewDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RenewDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResendContactReachabilityEmailRequest:
    boto3_raw_data: "type_defs.ResendContactReachabilityEmailRequestTypeDef" = (
        dataclasses.field()
    )

    domainName = field("domainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResendContactReachabilityEmailRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResendContactReachabilityEmailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResendOperationAuthorizationRequest:
    boto3_raw_data: "type_defs.ResendOperationAuthorizationRequestTypeDef" = (
        dataclasses.field()
    )

    OperationId = field("OperationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResendOperationAuthorizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResendOperationAuthorizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveDomainAuthCodeRequest:
    boto3_raw_data: "type_defs.RetrieveDomainAuthCodeRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RetrieveDomainAuthCodeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveDomainAuthCodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransferDomainToAnotherAwsAccountRequest:
    boto3_raw_data: "type_defs.TransferDomainToAnotherAwsAccountRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TransferDomainToAnotherAwsAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransferDomainToAnotherAwsAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainContactPrivacyRequest:
    boto3_raw_data: "type_defs.UpdateDomainContactPrivacyRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    AdminPrivacy = field("AdminPrivacy")
    RegistrantPrivacy = field("RegistrantPrivacy")
    TechPrivacy = field("TechPrivacy")
    BillingPrivacy = field("BillingPrivacy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDomainContactPrivacyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainContactPrivacyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptDomainTransferFromAnotherAwsAccountResponse:
    boto3_raw_data: (
        "type_defs.AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef"
    ) = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef"
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
                "type_defs.AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateDelegationSignerToDomainResponse:
    boto3_raw_data: "type_defs.AssociateDelegationSignerToDomainResponseTypeDef" = (
        dataclasses.field()
    )

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateDelegationSignerToDomainResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateDelegationSignerToDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelDomainTransferToAnotherAwsAccountResponse:
    boto3_raw_data: (
        "type_defs.CancelDomainTransferToAnotherAwsAccountResponseTypeDef"
    ) = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelDomainTransferToAnotherAwsAccountResponseTypeDef"
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
                "type_defs.CancelDomainTransferToAnotherAwsAccountResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckDomainAvailabilityResponse:
    boto3_raw_data: "type_defs.CheckDomainAvailabilityResponseTypeDef" = (
        dataclasses.field()
    )

    Availability = field("Availability")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CheckDomainAvailabilityResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckDomainAvailabilityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainResponse:
    boto3_raw_data: "type_defs.DeleteDomainResponseTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableDomainTransferLockResponse:
    boto3_raw_data: "type_defs.DisableDomainTransferLockResponseTypeDef" = (
        dataclasses.field()
    )

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisableDomainTransferLockResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableDomainTransferLockResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateDelegationSignerFromDomainResponse:
    boto3_raw_data: (
        "type_defs.DisassociateDelegationSignerFromDomainResponseTypeDef"
    ) = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateDelegationSignerFromDomainResponseTypeDef"
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
                "type_defs.DisassociateDelegationSignerFromDomainResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableDomainTransferLockResponse:
    boto3_raw_data: "type_defs.EnableDomainTransferLockResponseTypeDef" = (
        dataclasses.field()
    )

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnableDomainTransferLockResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableDomainTransferLockResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactReachabilityStatusResponse:
    boto3_raw_data: "type_defs.GetContactReachabilityStatusResponseTypeDef" = (
        dataclasses.field()
    )

    domainName = field("domainName")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContactReachabilityStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactReachabilityStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOperationDetailResponse:
    boto3_raw_data: "type_defs.GetOperationDetailResponseTypeDef" = dataclasses.field()

    OperationId = field("OperationId")
    Status = field("Status")
    Message = field("Message")
    DomainName = field("DomainName")
    Type = field("Type")
    SubmittedDate = field("SubmittedDate")
    LastUpdatedDate = field("LastUpdatedDate")
    StatusFlag = field("StatusFlag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOperationDetailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOperationDetailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterDomainResponse:
    boto3_raw_data: "type_defs.RegisterDomainResponseTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectDomainTransferFromAnotherAwsAccountResponse:
    boto3_raw_data: (
        "type_defs.RejectDomainTransferFromAnotherAwsAccountResponseTypeDef"
    ) = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectDomainTransferFromAnotherAwsAccountResponseTypeDef"
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
                "type_defs.RejectDomainTransferFromAnotherAwsAccountResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenewDomainResponse:
    boto3_raw_data: "type_defs.RenewDomainResponseTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RenewDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RenewDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResendContactReachabilityEmailResponse:
    boto3_raw_data: "type_defs.ResendContactReachabilityEmailResponseTypeDef" = (
        dataclasses.field()
    )

    domainName = field("domainName")
    emailAddress = field("emailAddress")
    isAlreadyVerified = field("isAlreadyVerified")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResendContactReachabilityEmailResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResendContactReachabilityEmailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveDomainAuthCodeResponse:
    boto3_raw_data: "type_defs.RetrieveDomainAuthCodeResponseTypeDef" = (
        dataclasses.field()
    )

    AuthCode = field("AuthCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RetrieveDomainAuthCodeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveDomainAuthCodeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransferDomainResponse:
    boto3_raw_data: "type_defs.TransferDomainResponseTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransferDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransferDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransferDomainToAnotherAwsAccountResponse:
    boto3_raw_data: "type_defs.TransferDomainToAnotherAwsAccountResponseTypeDef" = (
        dataclasses.field()
    )

    OperationId = field("OperationId")
    Password = field("Password")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TransferDomainToAnotherAwsAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransferDomainToAnotherAwsAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainContactPrivacyResponse:
    boto3_raw_data: "type_defs.UpdateDomainContactPrivacyResponseTypeDef" = (
        dataclasses.field()
    )

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDomainContactPrivacyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainContactPrivacyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainContactResponse:
    boto3_raw_data: "type_defs.UpdateDomainContactResponseTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainNameserversResponse:
    boto3_raw_data: "type_defs.UpdateDomainNameserversResponseTypeDef" = (
        dataclasses.field()
    )

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDomainNameserversResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainNameserversResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateDelegationSignerToDomainRequest:
    boto3_raw_data: "type_defs.AssociateDelegationSignerToDomainRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @cached_property
    def SigningAttributes(self):  # pragma: no cover
        return DnssecSigningAttributes.make_one(
            self.boto3_raw_data["SigningAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateDelegationSignerToDomainRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateDelegationSignerToDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewBillingResponse:
    boto3_raw_data: "type_defs.ViewBillingResponseTypeDef" = dataclasses.field()

    NextPageMarker = field("NextPageMarker")

    @cached_property
    def BillingRecords(self):  # pragma: no cover
        return BillingRecord.make_many(self.boto3_raw_data["BillingRecords"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ViewBillingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ViewBillingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckDomainTransferabilityResponse:
    boto3_raw_data: "type_defs.CheckDomainTransferabilityResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Transferability(self):  # pragma: no cover
        return DomainTransferability.make_one(self.boto3_raw_data["Transferability"])

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CheckDomainTransferabilityResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckDomainTransferabilityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactDetailOutput:
    boto3_raw_data: "type_defs.ContactDetailOutputTypeDef" = dataclasses.field()

    FirstName = field("FirstName")
    LastName = field("LastName")
    ContactType = field("ContactType")
    OrganizationName = field("OrganizationName")
    AddressLine1 = field("AddressLine1")
    AddressLine2 = field("AddressLine2")
    City = field("City")
    State = field("State")
    CountryCode = field("CountryCode")
    ZipCode = field("ZipCode")
    PhoneNumber = field("PhoneNumber")
    Email = field("Email")
    Fax = field("Fax")

    @cached_property
    def ExtraParams(self):  # pragma: no cover
        return ExtraParam.make_many(self.boto3_raw_data["ExtraParams"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactDetailOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactDetailOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactDetail:
    boto3_raw_data: "type_defs.ContactDetailTypeDef" = dataclasses.field()

    FirstName = field("FirstName")
    LastName = field("LastName")
    ContactType = field("ContactType")
    OrganizationName = field("OrganizationName")
    AddressLine1 = field("AddressLine1")
    AddressLine2 = field("AddressLine2")
    City = field("City")
    State = field("State")
    CountryCode = field("CountryCode")
    ZipCode = field("ZipCode")
    PhoneNumber = field("PhoneNumber")
    Email = field("Email")
    Fax = field("Fax")

    @cached_property
    def ExtraParams(self):  # pragma: no cover
        return ExtraParam.make_many(self.boto3_raw_data["ExtraParams"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainPrice:
    boto3_raw_data: "type_defs.DomainPriceTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def RegistrationPrice(self):  # pragma: no cover
        return PriceWithCurrency.make_one(self.boto3_raw_data["RegistrationPrice"])

    @cached_property
    def TransferPrice(self):  # pragma: no cover
        return PriceWithCurrency.make_one(self.boto3_raw_data["TransferPrice"])

    @cached_property
    def RenewalPrice(self):  # pragma: no cover
        return PriceWithCurrency.make_one(self.boto3_raw_data["RenewalPrice"])

    @cached_property
    def ChangeOwnershipPrice(self):  # pragma: no cover
        return PriceWithCurrency.make_one(self.boto3_raw_data["ChangeOwnershipPrice"])

    @cached_property
    def RestorationPrice(self):  # pragma: no cover
        return PriceWithCurrency.make_one(self.boto3_raw_data["RestorationPrice"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainPriceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainPriceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainSuggestionsResponse:
    boto3_raw_data: "type_defs.GetDomainSuggestionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SuggestionsList(self):  # pragma: no cover
        return DomainSuggestion.make_many(self.boto3_raw_data["SuggestionsList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainSuggestionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainSuggestionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsResponse:
    boto3_raw_data: "type_defs.ListDomainsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Domains(self):  # pragma: no cover
        return DomainSummary.make_many(self.boto3_raw_data["Domains"])

    NextPageMarker = field("NextPageMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricesRequestPaginate:
    boto3_raw_data: "type_defs.ListPricesRequestPaginateTypeDef" = dataclasses.field()

    Tld = field("Tld")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPricesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsRequestPaginate:
    boto3_raw_data: "type_defs.ListDomainsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def FilterConditions(self):  # pragma: no cover
        return FilterCondition.make_many(self.boto3_raw_data["FilterConditions"])

    @cached_property
    def SortCondition(self):  # pragma: no cover
        return SortCondition.make_one(self.boto3_raw_data["SortCondition"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsRequest:
    boto3_raw_data: "type_defs.ListDomainsRequestTypeDef" = dataclasses.field()

    @cached_property
    def FilterConditions(self):  # pragma: no cover
        return FilterCondition.make_many(self.boto3_raw_data["FilterConditions"])

    @cached_property
    def SortCondition(self):  # pragma: no cover
        return SortCondition.make_one(self.boto3_raw_data["SortCondition"])

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOperationsRequestPaginate:
    boto3_raw_data: "type_defs.ListOperationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SubmittedSince = field("SubmittedSince")
    Status = field("Status")
    Type = field("Type")
    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOperationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOperationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOperationsRequest:
    boto3_raw_data: "type_defs.ListOperationsRequestTypeDef" = dataclasses.field()

    SubmittedSince = field("SubmittedSince")
    Marker = field("Marker")
    MaxItems = field("MaxItems")
    Status = field("Status")
    Type = field("Type")
    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOperationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOperationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewBillingRequestPaginate:
    boto3_raw_data: "type_defs.ViewBillingRequestPaginateTypeDef" = dataclasses.field()

    Start = field("Start")
    End = field("End")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ViewBillingRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ViewBillingRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewBillingRequest:
    boto3_raw_data: "type_defs.ViewBillingRequestTypeDef" = dataclasses.field()

    Start = field("Start")
    End = field("End")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ViewBillingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ViewBillingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOperationsResponse:
    boto3_raw_data: "type_defs.ListOperationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Operations(self):  # pragma: no cover
        return OperationSummary.make_many(self.boto3_raw_data["Operations"])

    NextPageMarker = field("NextPageMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOperationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOperationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForDomainResponse:
    boto3_raw_data: "type_defs.ListTagsForDomainResponseTypeDef" = dataclasses.field()

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTagsForDomainRequest:
    boto3_raw_data: "type_defs.UpdateTagsForDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @cached_property
    def TagsToUpdate(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagsToUpdate"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTagsForDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTagsForDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainDetailResponse:
    boto3_raw_data: "type_defs.GetDomainDetailResponseTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @cached_property
    def Nameservers(self):  # pragma: no cover
        return NameserverOutput.make_many(self.boto3_raw_data["Nameservers"])

    AutoRenew = field("AutoRenew")

    @cached_property
    def AdminContact(self):  # pragma: no cover
        return ContactDetailOutput.make_one(self.boto3_raw_data["AdminContact"])

    @cached_property
    def RegistrantContact(self):  # pragma: no cover
        return ContactDetailOutput.make_one(self.boto3_raw_data["RegistrantContact"])

    @cached_property
    def TechContact(self):  # pragma: no cover
        return ContactDetailOutput.make_one(self.boto3_raw_data["TechContact"])

    AdminPrivacy = field("AdminPrivacy")
    RegistrantPrivacy = field("RegistrantPrivacy")
    TechPrivacy = field("TechPrivacy")
    RegistrarName = field("RegistrarName")
    WhoIsServer = field("WhoIsServer")
    RegistrarUrl = field("RegistrarUrl")
    AbuseContactEmail = field("AbuseContactEmail")
    AbuseContactPhone = field("AbuseContactPhone")
    RegistryDomainId = field("RegistryDomainId")
    CreationDate = field("CreationDate")
    UpdatedDate = field("UpdatedDate")
    ExpirationDate = field("ExpirationDate")
    Reseller = field("Reseller")
    DnsSec = field("DnsSec")
    StatusList = field("StatusList")

    @cached_property
    def DnssecKeys(self):  # pragma: no cover
        return DnssecKey.make_many(self.boto3_raw_data["DnssecKeys"])

    @cached_property
    def BillingContact(self):  # pragma: no cover
        return ContactDetailOutput.make_one(self.boto3_raw_data["BillingContact"])

    BillingPrivacy = field("BillingPrivacy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainDetailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainDetailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricesResponse:
    boto3_raw_data: "type_defs.ListPricesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Prices(self):  # pragma: no cover
        return DomainPrice.make_many(self.boto3_raw_data["Prices"])

    NextPageMarker = field("NextPageMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPricesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainNameserversRequest:
    boto3_raw_data: "type_defs.UpdateDomainNameserversRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    Nameservers = field("Nameservers")
    FIAuthKey = field("FIAuthKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDomainNameserversRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainNameserversRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterDomainRequest:
    boto3_raw_data: "type_defs.RegisterDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DurationInYears = field("DurationInYears")
    AdminContact = field("AdminContact")
    RegistrantContact = field("RegistrantContact")
    TechContact = field("TechContact")
    IdnLangCode = field("IdnLangCode")
    AutoRenew = field("AutoRenew")
    PrivacyProtectAdminContact = field("PrivacyProtectAdminContact")
    PrivacyProtectRegistrantContact = field("PrivacyProtectRegistrantContact")
    PrivacyProtectTechContact = field("PrivacyProtectTechContact")
    BillingContact = field("BillingContact")
    PrivacyProtectBillingContact = field("PrivacyProtectBillingContact")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransferDomainRequest:
    boto3_raw_data: "type_defs.TransferDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DurationInYears = field("DurationInYears")
    AdminContact = field("AdminContact")
    RegistrantContact = field("RegistrantContact")
    TechContact = field("TechContact")
    IdnLangCode = field("IdnLangCode")
    Nameservers = field("Nameservers")
    AuthCode = field("AuthCode")
    AutoRenew = field("AutoRenew")
    PrivacyProtectAdminContact = field("PrivacyProtectAdminContact")
    PrivacyProtectRegistrantContact = field("PrivacyProtectRegistrantContact")
    PrivacyProtectTechContact = field("PrivacyProtectTechContact")
    BillingContact = field("BillingContact")
    PrivacyProtectBillingContact = field("PrivacyProtectBillingContact")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransferDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransferDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainContactRequest:
    boto3_raw_data: "type_defs.UpdateDomainContactRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    AdminContact = field("AdminContact")
    RegistrantContact = field("RegistrantContact")
    TechContact = field("TechContact")

    @cached_property
    def Consent(self):  # pragma: no cover
        return Consent.make_one(self.boto3_raw_data["Consent"])

    BillingContact = field("BillingContact")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
