# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_managedblockchain_query import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AddressIdentifierFilter:
    boto3_raw_data: "type_defs.AddressIdentifierFilterTypeDef" = dataclasses.field()

    transactionEventToAddress = field("transactionEventToAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddressIdentifierFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddressIdentifierFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContractIdentifier:
    boto3_raw_data: "type_defs.ContractIdentifierTypeDef" = dataclasses.field()

    network = field("network")
    contractAddress = field("contractAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContractIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContractIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockchainInstantOutput:
    boto3_raw_data: "type_defs.BlockchainInstantOutputTypeDef" = dataclasses.field()

    time = field("time")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BlockchainInstantOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockchainInstantOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OwnerIdentifier:
    boto3_raw_data: "type_defs.OwnerIdentifierTypeDef" = dataclasses.field()

    address = field("address")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OwnerIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OwnerIdentifierTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TokenIdentifier:
    boto3_raw_data: "type_defs.TokenIdentifierTypeDef" = dataclasses.field()

    network = field("network")
    contractAddress = field("contractAddress")
    tokenId = field("tokenId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TokenIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TokenIdentifierTypeDef"]],
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
class ConfirmationStatusFilter:
    boto3_raw_data: "type_defs.ConfirmationStatusFilterTypeDef" = dataclasses.field()

    include = field("include")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfirmationStatusFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmationStatusFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContractFilter:
    boto3_raw_data: "type_defs.ContractFilterTypeDef" = dataclasses.field()

    network = field("network")
    tokenStandard = field("tokenStandard")
    deployerAddress = field("deployerAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContractFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContractFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContractMetadata:
    boto3_raw_data: "type_defs.ContractMetadataTypeDef" = dataclasses.field()

    name = field("name")
    symbol = field("symbol")
    decimals = field("decimals")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContractMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContractMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransactionInput:
    boto3_raw_data: "type_defs.GetTransactionInputTypeDef" = dataclasses.field()

    network = field("network")
    transactionHash = field("transactionHash")
    transactionId = field("transactionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTransactionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransactionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Transaction:
    boto3_raw_data: "type_defs.TransactionTypeDef" = dataclasses.field()

    network = field("network")
    transactionHash = field("transactionHash")
    transactionTimestamp = field("transactionTimestamp")
    transactionIndex = field("transactionIndex")
    numberOfTransactions = field("numberOfTransactions")
    to = field("to")
    blockHash = field("blockHash")
    blockNumber = field("blockNumber")
    from_ = field("from")
    contractAddress = field("contractAddress")
    gasUsed = field("gasUsed")
    cumulativeGasUsed = field("cumulativeGasUsed")
    effectiveGasPrice = field("effectiveGasPrice")
    signatureV = field("signatureV")
    signatureR = field("signatureR")
    signatureS = field("signatureS")
    transactionFee = field("transactionFee")
    transactionId = field("transactionId")
    confirmationStatus = field("confirmationStatus")
    executionStatus = field("executionStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransactionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransactionTypeDef"]]
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
class ListFilteredTransactionEventsSort:
    boto3_raw_data: "type_defs.ListFilteredTransactionEventsSortTypeDef" = (
        dataclasses.field()
    )

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFilteredTransactionEventsSortTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFilteredTransactionEventsSortTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoutFilter:
    boto3_raw_data: "type_defs.VoutFilterTypeDef" = dataclasses.field()

    voutSpent = field("voutSpent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VoutFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VoutFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OwnerFilter:
    boto3_raw_data: "type_defs.OwnerFilterTypeDef" = dataclasses.field()

    address = field("address")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OwnerFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OwnerFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TokenFilter:
    boto3_raw_data: "type_defs.TokenFilterTypeDef" = dataclasses.field()

    network = field("network")
    contractAddress = field("contractAddress")
    tokenId = field("tokenId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TokenFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TokenFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTransactionEventsInput:
    boto3_raw_data: "type_defs.ListTransactionEventsInputTypeDef" = dataclasses.field()

    network = field("network")
    transactionHash = field("transactionHash")
    transactionId = field("transactionId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTransactionEventsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTransactionEventsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTransactionsSort:
    boto3_raw_data: "type_defs.ListTransactionsSortTypeDef" = dataclasses.field()

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTransactionsSortTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTransactionsSortTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransactionOutputItem:
    boto3_raw_data: "type_defs.TransactionOutputItemTypeDef" = dataclasses.field()

    transactionHash = field("transactionHash")
    network = field("network")
    transactionTimestamp = field("transactionTimestamp")
    transactionId = field("transactionId")
    confirmationStatus = field("confirmationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransactionOutputItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransactionOutputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetContract:
    boto3_raw_data: "type_defs.AssetContractTypeDef" = dataclasses.field()

    @cached_property
    def contractIdentifier(self):  # pragma: no cover
        return ContractIdentifier.make_one(self.boto3_raw_data["contractIdentifier"])

    tokenStandard = field("tokenStandard")
    deployerAddress = field("deployerAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetContractTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetContractTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetContractInput:
    boto3_raw_data: "type_defs.GetAssetContractInputTypeDef" = dataclasses.field()

    @cached_property
    def contractIdentifier(self):  # pragma: no cover
        return ContractIdentifier.make_one(self.boto3_raw_data["contractIdentifier"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssetContractInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetContractInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransactionEvent:
    boto3_raw_data: "type_defs.TransactionEventTypeDef" = dataclasses.field()

    network = field("network")
    transactionHash = field("transactionHash")
    eventType = field("eventType")
    from_ = field("from")
    to = field("to")
    value = field("value")
    contractAddress = field("contractAddress")
    tokenId = field("tokenId")
    transactionId = field("transactionId")
    voutIndex = field("voutIndex")
    voutSpent = field("voutSpent")
    spentVoutTransactionId = field("spentVoutTransactionId")
    spentVoutTransactionHash = field("spentVoutTransactionHash")
    spentVoutIndex = field("spentVoutIndex")

    @cached_property
    def blockchainInstant(self):  # pragma: no cover
        return BlockchainInstantOutput.make_one(
            self.boto3_raw_data["blockchainInstant"]
        )

    confirmationStatus = field("confirmationStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransactionEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransactionEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetTokenBalanceErrorItem:
    boto3_raw_data: "type_defs.BatchGetTokenBalanceErrorItemTypeDef" = (
        dataclasses.field()
    )

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")
    errorType = field("errorType")

    @cached_property
    def tokenIdentifier(self):  # pragma: no cover
        return TokenIdentifier.make_one(self.boto3_raw_data["tokenIdentifier"])

    @cached_property
    def ownerIdentifier(self):  # pragma: no cover
        return OwnerIdentifier.make_one(self.boto3_raw_data["ownerIdentifier"])

    @cached_property
    def atBlockchainInstant(self):  # pragma: no cover
        return BlockchainInstantOutput.make_one(
            self.boto3_raw_data["atBlockchainInstant"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetTokenBalanceErrorItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetTokenBalanceErrorItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetTokenBalanceOutputItem:
    boto3_raw_data: "type_defs.BatchGetTokenBalanceOutputItemTypeDef" = (
        dataclasses.field()
    )

    balance = field("balance")

    @cached_property
    def atBlockchainInstant(self):  # pragma: no cover
        return BlockchainInstantOutput.make_one(
            self.boto3_raw_data["atBlockchainInstant"]
        )

    @cached_property
    def ownerIdentifier(self):  # pragma: no cover
        return OwnerIdentifier.make_one(self.boto3_raw_data["ownerIdentifier"])

    @cached_property
    def tokenIdentifier(self):  # pragma: no cover
        return TokenIdentifier.make_one(self.boto3_raw_data["tokenIdentifier"])

    @cached_property
    def lastUpdatedTime(self):  # pragma: no cover
        return BlockchainInstantOutput.make_one(self.boto3_raw_data["lastUpdatedTime"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetTokenBalanceOutputItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetTokenBalanceOutputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TokenBalance:
    boto3_raw_data: "type_defs.TokenBalanceTypeDef" = dataclasses.field()

    balance = field("balance")

    @cached_property
    def atBlockchainInstant(self):  # pragma: no cover
        return BlockchainInstantOutput.make_one(
            self.boto3_raw_data["atBlockchainInstant"]
        )

    @cached_property
    def ownerIdentifier(self):  # pragma: no cover
        return OwnerIdentifier.make_one(self.boto3_raw_data["ownerIdentifier"])

    @cached_property
    def tokenIdentifier(self):  # pragma: no cover
        return TokenIdentifier.make_one(self.boto3_raw_data["tokenIdentifier"])

    @cached_property
    def lastUpdatedTime(self):  # pragma: no cover
        return BlockchainInstantOutput.make_one(self.boto3_raw_data["lastUpdatedTime"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TokenBalanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TokenBalanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTokenBalanceOutput:
    boto3_raw_data: "type_defs.GetTokenBalanceOutputTypeDef" = dataclasses.field()

    @cached_property
    def ownerIdentifier(self):  # pragma: no cover
        return OwnerIdentifier.make_one(self.boto3_raw_data["ownerIdentifier"])

    @cached_property
    def tokenIdentifier(self):  # pragma: no cover
        return TokenIdentifier.make_one(self.boto3_raw_data["tokenIdentifier"])

    balance = field("balance")

    @cached_property
    def atBlockchainInstant(self):  # pragma: no cover
        return BlockchainInstantOutput.make_one(
            self.boto3_raw_data["atBlockchainInstant"]
        )

    @cached_property
    def lastUpdatedTime(self):  # pragma: no cover
        return BlockchainInstantOutput.make_one(self.boto3_raw_data["lastUpdatedTime"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTokenBalanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTokenBalanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockchainInstant:
    boto3_raw_data: "type_defs.BlockchainInstantTypeDef" = dataclasses.field()

    time = field("time")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlockchainInstantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockchainInstantTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetContractsInput:
    boto3_raw_data: "type_defs.ListAssetContractsInputTypeDef" = dataclasses.field()

    @cached_property
    def contractFilter(self):  # pragma: no cover
        return ContractFilter.make_one(self.boto3_raw_data["contractFilter"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetContractsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetContractsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetContractOutput:
    boto3_raw_data: "type_defs.GetAssetContractOutputTypeDef" = dataclasses.field()

    @cached_property
    def contractIdentifier(self):  # pragma: no cover
        return ContractIdentifier.make_one(self.boto3_raw_data["contractIdentifier"])

    tokenStandard = field("tokenStandard")
    deployerAddress = field("deployerAddress")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ContractMetadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssetContractOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetContractOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransactionOutput:
    boto3_raw_data: "type_defs.GetTransactionOutputTypeDef" = dataclasses.field()

    @cached_property
    def transaction(self):  # pragma: no cover
        return Transaction.make_one(self.boto3_raw_data["transaction"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTransactionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransactionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetContractsInputPaginate:
    boto3_raw_data: "type_defs.ListAssetContractsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def contractFilter(self):  # pragma: no cover
        return ContractFilter.make_one(self.boto3_raw_data["contractFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssetContractsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetContractsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTransactionEventsInputPaginate:
    boto3_raw_data: "type_defs.ListTransactionEventsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    network = field("network")
    transactionHash = field("transactionHash")
    transactionId = field("transactionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTransactionEventsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTransactionEventsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTokenBalancesInputPaginate:
    boto3_raw_data: "type_defs.ListTokenBalancesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tokenFilter(self):  # pragma: no cover
        return TokenFilter.make_one(self.boto3_raw_data["tokenFilter"])

    @cached_property
    def ownerFilter(self):  # pragma: no cover
        return OwnerFilter.make_one(self.boto3_raw_data["ownerFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTokenBalancesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTokenBalancesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTokenBalancesInput:
    boto3_raw_data: "type_defs.ListTokenBalancesInputTypeDef" = dataclasses.field()

    @cached_property
    def tokenFilter(self):  # pragma: no cover
        return TokenFilter.make_one(self.boto3_raw_data["tokenFilter"])

    @cached_property
    def ownerFilter(self):  # pragma: no cover
        return OwnerFilter.make_one(self.boto3_raw_data["ownerFilter"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTokenBalancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTokenBalancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTransactionsOutput:
    boto3_raw_data: "type_defs.ListTransactionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def transactions(self):  # pragma: no cover
        return TransactionOutputItem.make_many(self.boto3_raw_data["transactions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTransactionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTransactionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetContractsOutput:
    boto3_raw_data: "type_defs.ListAssetContractsOutputTypeDef" = dataclasses.field()

    @cached_property
    def contracts(self):  # pragma: no cover
        return AssetContract.make_many(self.boto3_raw_data["contracts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetContractsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetContractsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFilteredTransactionEventsOutput:
    boto3_raw_data: "type_defs.ListFilteredTransactionEventsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def events(self):  # pragma: no cover
        return TransactionEvent.make_many(self.boto3_raw_data["events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFilteredTransactionEventsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFilteredTransactionEventsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTransactionEventsOutput:
    boto3_raw_data: "type_defs.ListTransactionEventsOutputTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return TransactionEvent.make_many(self.boto3_raw_data["events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTransactionEventsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTransactionEventsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetTokenBalanceOutput:
    boto3_raw_data: "type_defs.BatchGetTokenBalanceOutputTypeDef" = dataclasses.field()

    @cached_property
    def tokenBalances(self):  # pragma: no cover
        return BatchGetTokenBalanceOutputItem.make_many(
            self.boto3_raw_data["tokenBalances"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchGetTokenBalanceErrorItem.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetTokenBalanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetTokenBalanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTokenBalancesOutput:
    boto3_raw_data: "type_defs.ListTokenBalancesOutputTypeDef" = dataclasses.field()

    @cached_property
    def tokenBalances(self):  # pragma: no cover
        return TokenBalance.make_many(self.boto3_raw_data["tokenBalances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTokenBalancesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTokenBalancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetTokenBalanceInputItem:
    boto3_raw_data: "type_defs.BatchGetTokenBalanceInputItemTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tokenIdentifier(self):  # pragma: no cover
        return TokenIdentifier.make_one(self.boto3_raw_data["tokenIdentifier"])

    @cached_property
    def ownerIdentifier(self):  # pragma: no cover
        return OwnerIdentifier.make_one(self.boto3_raw_data["ownerIdentifier"])

    atBlockchainInstant = field("atBlockchainInstant")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetTokenBalanceInputItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetTokenBalanceInputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTokenBalanceInput:
    boto3_raw_data: "type_defs.GetTokenBalanceInputTypeDef" = dataclasses.field()

    @cached_property
    def tokenIdentifier(self):  # pragma: no cover
        return TokenIdentifier.make_one(self.boto3_raw_data["tokenIdentifier"])

    @cached_property
    def ownerIdentifier(self):  # pragma: no cover
        return OwnerIdentifier.make_one(self.boto3_raw_data["ownerIdentifier"])

    atBlockchainInstant = field("atBlockchainInstant")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTokenBalanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTokenBalanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTransactionsInputPaginate:
    boto3_raw_data: "type_defs.ListTransactionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    address = field("address")
    network = field("network")
    fromBlockchainInstant = field("fromBlockchainInstant")
    toBlockchainInstant = field("toBlockchainInstant")

    @cached_property
    def sort(self):  # pragma: no cover
        return ListTransactionsSort.make_one(self.boto3_raw_data["sort"])

    @cached_property
    def confirmationStatusFilter(self):  # pragma: no cover
        return ConfirmationStatusFilter.make_one(
            self.boto3_raw_data["confirmationStatusFilter"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTransactionsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTransactionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTransactionsInput:
    boto3_raw_data: "type_defs.ListTransactionsInputTypeDef" = dataclasses.field()

    address = field("address")
    network = field("network")
    fromBlockchainInstant = field("fromBlockchainInstant")
    toBlockchainInstant = field("toBlockchainInstant")

    @cached_property
    def sort(self):  # pragma: no cover
        return ListTransactionsSort.make_one(self.boto3_raw_data["sort"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def confirmationStatusFilter(self):  # pragma: no cover
        return ConfirmationStatusFilter.make_one(
            self.boto3_raw_data["confirmationStatusFilter"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTransactionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTransactionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeFilter:
    boto3_raw_data: "type_defs.TimeFilterTypeDef" = dataclasses.field()

    from_ = field("from")
    to = field("to")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetTokenBalanceInput:
    boto3_raw_data: "type_defs.BatchGetTokenBalanceInputTypeDef" = dataclasses.field()

    @cached_property
    def getTokenBalanceInputs(self):  # pragma: no cover
        return BatchGetTokenBalanceInputItem.make_many(
            self.boto3_raw_data["getTokenBalanceInputs"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetTokenBalanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetTokenBalanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFilteredTransactionEventsInputPaginate:
    boto3_raw_data: "type_defs.ListFilteredTransactionEventsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    network = field("network")

    @cached_property
    def addressIdentifierFilter(self):  # pragma: no cover
        return AddressIdentifierFilter.make_one(
            self.boto3_raw_data["addressIdentifierFilter"]
        )

    @cached_property
    def timeFilter(self):  # pragma: no cover
        return TimeFilter.make_one(self.boto3_raw_data["timeFilter"])

    @cached_property
    def voutFilter(self):  # pragma: no cover
        return VoutFilter.make_one(self.boto3_raw_data["voutFilter"])

    @cached_property
    def confirmationStatusFilter(self):  # pragma: no cover
        return ConfirmationStatusFilter.make_one(
            self.boto3_raw_data["confirmationStatusFilter"]
        )

    @cached_property
    def sort(self):  # pragma: no cover
        return ListFilteredTransactionEventsSort.make_one(self.boto3_raw_data["sort"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFilteredTransactionEventsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFilteredTransactionEventsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFilteredTransactionEventsInput:
    boto3_raw_data: "type_defs.ListFilteredTransactionEventsInputTypeDef" = (
        dataclasses.field()
    )

    network = field("network")

    @cached_property
    def addressIdentifierFilter(self):  # pragma: no cover
        return AddressIdentifierFilter.make_one(
            self.boto3_raw_data["addressIdentifierFilter"]
        )

    @cached_property
    def timeFilter(self):  # pragma: no cover
        return TimeFilter.make_one(self.boto3_raw_data["timeFilter"])

    @cached_property
    def voutFilter(self):  # pragma: no cover
        return VoutFilter.make_one(self.boto3_raw_data["voutFilter"])

    @cached_property
    def confirmationStatusFilter(self):  # pragma: no cover
        return ConfirmationStatusFilter.make_one(
            self.boto3_raw_data["confirmationStatusFilter"]
        )

    @cached_property
    def sort(self):  # pragma: no cover
        return ListFilteredTransactionEventsSort.make_one(self.boto3_raw_data["sort"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFilteredTransactionEventsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFilteredTransactionEventsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
