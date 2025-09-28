# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_managedblockchain_query import type_defs as bs_td


class MANAGEDBLOCKCHAIN_QUERYCaster:

    def batch_get_token_balance(
        self,
        res: "bs_td.BatchGetTokenBalanceOutputTypeDef",
    ) -> "dc_td.BatchGetTokenBalanceOutput":
        return dc_td.BatchGetTokenBalanceOutput.make_one(res)

    def get_asset_contract(
        self,
        res: "bs_td.GetAssetContractOutputTypeDef",
    ) -> "dc_td.GetAssetContractOutput":
        return dc_td.GetAssetContractOutput.make_one(res)

    def get_token_balance(
        self,
        res: "bs_td.GetTokenBalanceOutputTypeDef",
    ) -> "dc_td.GetTokenBalanceOutput":
        return dc_td.GetTokenBalanceOutput.make_one(res)

    def get_transaction(
        self,
        res: "bs_td.GetTransactionOutputTypeDef",
    ) -> "dc_td.GetTransactionOutput":
        return dc_td.GetTransactionOutput.make_one(res)

    def list_asset_contracts(
        self,
        res: "bs_td.ListAssetContractsOutputTypeDef",
    ) -> "dc_td.ListAssetContractsOutput":
        return dc_td.ListAssetContractsOutput.make_one(res)

    def list_filtered_transaction_events(
        self,
        res: "bs_td.ListFilteredTransactionEventsOutputTypeDef",
    ) -> "dc_td.ListFilteredTransactionEventsOutput":
        return dc_td.ListFilteredTransactionEventsOutput.make_one(res)

    def list_token_balances(
        self,
        res: "bs_td.ListTokenBalancesOutputTypeDef",
    ) -> "dc_td.ListTokenBalancesOutput":
        return dc_td.ListTokenBalancesOutput.make_one(res)

    def list_transaction_events(
        self,
        res: "bs_td.ListTransactionEventsOutputTypeDef",
    ) -> "dc_td.ListTransactionEventsOutput":
        return dc_td.ListTransactionEventsOutput.make_one(res)

    def list_transactions(
        self,
        res: "bs_td.ListTransactionsOutputTypeDef",
    ) -> "dc_td.ListTransactionsOutput":
        return dc_td.ListTransactionsOutput.make_one(res)


managedblockchain_query_caster = MANAGEDBLOCKCHAIN_QUERYCaster()
