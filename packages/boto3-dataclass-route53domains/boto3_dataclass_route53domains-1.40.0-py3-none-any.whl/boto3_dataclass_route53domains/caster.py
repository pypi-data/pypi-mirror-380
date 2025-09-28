# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_route53domains import type_defs as bs_td


class ROUTE53DOMAINSCaster:

    def accept_domain_transfer_from_another_aws_account(
        self,
        res: "bs_td.AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef",
    ) -> "dc_td.AcceptDomainTransferFromAnotherAwsAccountResponse":
        return dc_td.AcceptDomainTransferFromAnotherAwsAccountResponse.make_one(res)

    def associate_delegation_signer_to_domain(
        self,
        res: "bs_td.AssociateDelegationSignerToDomainResponseTypeDef",
    ) -> "dc_td.AssociateDelegationSignerToDomainResponse":
        return dc_td.AssociateDelegationSignerToDomainResponse.make_one(res)

    def cancel_domain_transfer_to_another_aws_account(
        self,
        res: "bs_td.CancelDomainTransferToAnotherAwsAccountResponseTypeDef",
    ) -> "dc_td.CancelDomainTransferToAnotherAwsAccountResponse":
        return dc_td.CancelDomainTransferToAnotherAwsAccountResponse.make_one(res)

    def check_domain_availability(
        self,
        res: "bs_td.CheckDomainAvailabilityResponseTypeDef",
    ) -> "dc_td.CheckDomainAvailabilityResponse":
        return dc_td.CheckDomainAvailabilityResponse.make_one(res)

    def check_domain_transferability(
        self,
        res: "bs_td.CheckDomainTransferabilityResponseTypeDef",
    ) -> "dc_td.CheckDomainTransferabilityResponse":
        return dc_td.CheckDomainTransferabilityResponse.make_one(res)

    def delete_domain(
        self,
        res: "bs_td.DeleteDomainResponseTypeDef",
    ) -> "dc_td.DeleteDomainResponse":
        return dc_td.DeleteDomainResponse.make_one(res)

    def disable_domain_transfer_lock(
        self,
        res: "bs_td.DisableDomainTransferLockResponseTypeDef",
    ) -> "dc_td.DisableDomainTransferLockResponse":
        return dc_td.DisableDomainTransferLockResponse.make_one(res)

    def disassociate_delegation_signer_from_domain(
        self,
        res: "bs_td.DisassociateDelegationSignerFromDomainResponseTypeDef",
    ) -> "dc_td.DisassociateDelegationSignerFromDomainResponse":
        return dc_td.DisassociateDelegationSignerFromDomainResponse.make_one(res)

    def enable_domain_transfer_lock(
        self,
        res: "bs_td.EnableDomainTransferLockResponseTypeDef",
    ) -> "dc_td.EnableDomainTransferLockResponse":
        return dc_td.EnableDomainTransferLockResponse.make_one(res)

    def get_contact_reachability_status(
        self,
        res: "bs_td.GetContactReachabilityStatusResponseTypeDef",
    ) -> "dc_td.GetContactReachabilityStatusResponse":
        return dc_td.GetContactReachabilityStatusResponse.make_one(res)

    def get_domain_detail(
        self,
        res: "bs_td.GetDomainDetailResponseTypeDef",
    ) -> "dc_td.GetDomainDetailResponse":
        return dc_td.GetDomainDetailResponse.make_one(res)

    def get_domain_suggestions(
        self,
        res: "bs_td.GetDomainSuggestionsResponseTypeDef",
    ) -> "dc_td.GetDomainSuggestionsResponse":
        return dc_td.GetDomainSuggestionsResponse.make_one(res)

    def get_operation_detail(
        self,
        res: "bs_td.GetOperationDetailResponseTypeDef",
    ) -> "dc_td.GetOperationDetailResponse":
        return dc_td.GetOperationDetailResponse.make_one(res)

    def list_domains(
        self,
        res: "bs_td.ListDomainsResponseTypeDef",
    ) -> "dc_td.ListDomainsResponse":
        return dc_td.ListDomainsResponse.make_one(res)

    def list_operations(
        self,
        res: "bs_td.ListOperationsResponseTypeDef",
    ) -> "dc_td.ListOperationsResponse":
        return dc_td.ListOperationsResponse.make_one(res)

    def list_prices(
        self,
        res: "bs_td.ListPricesResponseTypeDef",
    ) -> "dc_td.ListPricesResponse":
        return dc_td.ListPricesResponse.make_one(res)

    def list_tags_for_domain(
        self,
        res: "bs_td.ListTagsForDomainResponseTypeDef",
    ) -> "dc_td.ListTagsForDomainResponse":
        return dc_td.ListTagsForDomainResponse.make_one(res)

    def push_domain(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def register_domain(
        self,
        res: "bs_td.RegisterDomainResponseTypeDef",
    ) -> "dc_td.RegisterDomainResponse":
        return dc_td.RegisterDomainResponse.make_one(res)

    def reject_domain_transfer_from_another_aws_account(
        self,
        res: "bs_td.RejectDomainTransferFromAnotherAwsAccountResponseTypeDef",
    ) -> "dc_td.RejectDomainTransferFromAnotherAwsAccountResponse":
        return dc_td.RejectDomainTransferFromAnotherAwsAccountResponse.make_one(res)

    def renew_domain(
        self,
        res: "bs_td.RenewDomainResponseTypeDef",
    ) -> "dc_td.RenewDomainResponse":
        return dc_td.RenewDomainResponse.make_one(res)

    def resend_contact_reachability_email(
        self,
        res: "bs_td.ResendContactReachabilityEmailResponseTypeDef",
    ) -> "dc_td.ResendContactReachabilityEmailResponse":
        return dc_td.ResendContactReachabilityEmailResponse.make_one(res)

    def resend_operation_authorization(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def retrieve_domain_auth_code(
        self,
        res: "bs_td.RetrieveDomainAuthCodeResponseTypeDef",
    ) -> "dc_td.RetrieveDomainAuthCodeResponse":
        return dc_td.RetrieveDomainAuthCodeResponse.make_one(res)

    def transfer_domain(
        self,
        res: "bs_td.TransferDomainResponseTypeDef",
    ) -> "dc_td.TransferDomainResponse":
        return dc_td.TransferDomainResponse.make_one(res)

    def transfer_domain_to_another_aws_account(
        self,
        res: "bs_td.TransferDomainToAnotherAwsAccountResponseTypeDef",
    ) -> "dc_td.TransferDomainToAnotherAwsAccountResponse":
        return dc_td.TransferDomainToAnotherAwsAccountResponse.make_one(res)

    def update_domain_contact(
        self,
        res: "bs_td.UpdateDomainContactResponseTypeDef",
    ) -> "dc_td.UpdateDomainContactResponse":
        return dc_td.UpdateDomainContactResponse.make_one(res)

    def update_domain_contact_privacy(
        self,
        res: "bs_td.UpdateDomainContactPrivacyResponseTypeDef",
    ) -> "dc_td.UpdateDomainContactPrivacyResponse":
        return dc_td.UpdateDomainContactPrivacyResponse.make_one(res)

    def update_domain_nameservers(
        self,
        res: "bs_td.UpdateDomainNameserversResponseTypeDef",
    ) -> "dc_td.UpdateDomainNameserversResponse":
        return dc_td.UpdateDomainNameserversResponse.make_one(res)

    def view_billing(
        self,
        res: "bs_td.ViewBillingResponseTypeDef",
    ) -> "dc_td.ViewBillingResponse":
        return dc_td.ViewBillingResponse.make_one(res)


route53domains_caster = ROUTE53DOMAINSCaster()
