import re
from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Any, cast

from sun_agent_toolkit.core.classes.tool_base import ToolBase, create_tool
from sun_agent_toolkit.core.classes.wallet_client_base import Balance, Signature, WalletClientBase
from sun_agent_toolkit.core.types.chain import TronChain
from sun_agent_toolkit.core.types.token import Token

from .abi import TRC20_ABI
from .params import (
    ApproveParameters,
    BuildSendTokenParameters,
    BuildSendTrxParameters,
    ConvertFromBaseUnitsParameters,
    ConvertToBaseUnitsParameters,
    DelegateResourceParameters,
    FreezeBalanceParameters,
    GetAccountResourceInfoParameters,
    GetBalanceParameters,
    GetPendingRewardParameters,
    GetTokenAllowanceParameters,
    GetTokenInfoByTickerParameters,
    GetVotesParameters,
    RevokeApprovalParameters,
    SendRawTransactionParameters,
    SendTokenParameters,
    SignTransactionParameters,
    SignTypedDataParameters,
    UndelegateResourceParameters,
    UnfreezeBalanceParameters,
    VoteWitnessParameters,
    WithdrawRewardsParameters,
    WithdrawStakeBalanceParameters,
)
from .tokens import PREDEFINED_TOKENS, TronToken
from .types import TronReadRequest, TronReadResult, TronTransaction


class TronOptions:
    """Configuration options for TRON wallet clients."""

    def __init__(self) -> None:
        pass


class TronWalletBase(WalletClientBase, ABC):
    """Base class for TRON wallet implementations."""

    def __init__(self, tokens: list[TronToken] | None = None, enable_send: bool = True) -> None:
        """Initialize the TRON wallet client.

        Args:
            tokens: List of token configurations
            enable_send: Whether to enable send functionality
        """
        WalletClientBase.__init__(self)
        self.tokens = tokens or PREDEFINED_TOKENS
        self.enable_send = enable_send

    def get_chain(self) -> TronChain:
        """Get the chain type for TRON."""
        network = self.get_network_id()
        return TronChain(network)

    @abstractmethod
    def get_address(self) -> str:
        """Get the wallet's public address."""
        pass

    @abstractmethod
    def get_network_id(self) -> str:
        """Get the network ID (e.g., 'mainnet', 'shasta', 'nile')."""
        pass

    @abstractmethod
    def sign_message(self, message: str) -> Signature:
        """Sign a message with the wallet's private key."""
        pass

    @abstractmethod
    def sign_typed_data(
        self, types: dict[str, Any], primary_type: str, domain: dict[str, Any], value: dict[str, Any]
    ) -> Signature:
        """Sign typed data with the wallet's private key (TRON equivalent of EIP-712)."""
        pass

    @abstractmethod
    def send_transaction(self, transaction: TronTransaction) -> dict[str, str]:
        """Send a transaction on the TRON chain."""
        pass

    @abstractmethod
    def read(self, request: TronReadRequest) -> TronReadResult:
        """Read data from a smart contract."""
        pass

    @abstractmethod
    def get_native_balance(self) -> int:
        """Get the native balance of the wallet in SUN."""
        pass

    @abstractmethod
    def get_account_resource_info(self) -> dict[str, Any]:
        """Account resource info (energy/bandwidth)."""
        pass

    @abstractmethod
    def get_votes(self) -> dict[str, int]:
        """Get voting stats: totalVotes, usedVotes, availableVotes."""
        pass

    @abstractmethod
    def get_pending_reward(self) -> int:
        """Pending reward in SUN."""
        pass

    @abstractmethod
    def build_send_trx(self, params: dict[str, Any]) -> dict[str, Any]:
        """Create an unsigned TRX transfer transaction."""
        pass

    @abstractmethod
    def build_send_token(self, params: dict[str, Any]) -> dict[str, Any]:
        """Create an unsigned TRC20 token transfer transaction."""
        pass

    @abstractmethod
    def sign_transaction(self, transaction: dict[str, Any] | str) -> dict[str, Any]:
        """Sign a transaction payload using the wallet's private key."""
        pass

    @abstractmethod
    def send_raw_transaction(self, signed_transaction: dict[str, Any] | str) -> dict[str, Any]:
        """Broadcast a signed transaction to the network."""
        pass

    # ----- Stake 2.0 & Governance (abstract API to be implemented by concrete client) -----

    @abstractmethod
    def freeze_balance(self, params: dict[str, Any]) -> dict[str, str]:
        """Freeze TRX to obtain ENERGY or BANDWIDTH (Stake 2.0)."""
        pass

    @abstractmethod
    def unfreeze_balance(self, params: dict[str, Any]) -> dict[str, str]:
        """Unstake TRX (Stake 2.0)."""
        pass

    @abstractmethod
    def withdraw_stake_balance(self, params: dict[str, Any]) -> dict[str, str]:
        """Withdraw expired unstaked TRX after cool-down period (Stake 2.0)."""
        pass

    @abstractmethod
    def delegate_resource(self, params: dict[str, Any]) -> dict[str, str]:
        """Delegate ENERGY/BANDWIDTH to another address (Stake 2.0)."""
        pass

    @abstractmethod
    def undelegate_resource(self, params: dict[str, Any]) -> dict[str, str]:
        """Cancel delegation of ENERGY/BANDWIDTH (Stake 2.0)."""
        pass

    @abstractmethod
    def vote_witness(self, params: dict[str, Any]) -> dict[str, str]:
        """Vote for witnesses (governance)."""
        pass

    @abstractmethod
    def withdraw_rewards(self, params: dict[str, Any]) -> dict[str, str]:
        """Withdraw voting rewards."""
        pass

    def balance_of(self, address: str, token_address: str | None = None) -> Balance:
        """Get the balance of an address for native or TRC20 tokens.

        Args:
            address: The address to check balance for
            token_address: Optional TRC20 token address

        Returns:
            Balance information
        """
        if token_address:
            try:
                balance_result = self.read(
                    {
                        "address": token_address,
                        "abi": TRC20_ABI,
                        "functionName": "balanceOf",
                        "args": [address],
                    }
                )

                decimals_result = self.read(
                    {"address": token_address, "abi": TRC20_ABI, "functionName": "decimals", "args": []}
                )

                name_result = self.read(
                    {"address": token_address, "abi": TRC20_ABI, "functionName": "name", "args": []}
                )

                symbol_result = self.read(
                    {"address": token_address, "abi": TRC20_ABI, "functionName": "symbol", "args": []}
                )

                balance_in_base_units = str(balance_result["value"])
                token_decimals = int(decimals_result["value"])
                token_name = str(name_result["value"])
                token_symbol = str(symbol_result["value"])

                # Use proper decimal arithmetic to avoid precision loss
                divisor = Decimal(10) ** token_decimals
                balance_value = str(Decimal(balance_in_base_units) / divisor)

                return {
                    "decimals": token_decimals,
                    "symbol": token_symbol,
                    "name": token_name,
                    "value": balance_value,
                    "in_base_units": balance_in_base_units,
                }
            except Exception as e:
                raise ValueError(f"Failed to fetch token balance: {str(e)}") from e
        else:
            try:
                balance_in_sun = self.get_native_balance()
                decimals = 6
                balance_value = str(Decimal(balance_in_sun) / (10**decimals))

                return {
                    "decimals": decimals,
                    "symbol": "TRX",
                    "name": "TRON",
                    "value": balance_value,
                    "in_base_units": str(balance_in_sun),
                }
            except Exception as e:
                raise ValueError(f"Failed to fetch native balance: {str(e)}") from e

    def get_token_info_by_ticker(self, ticker: str) -> Token:
        """Get token information by ticker symbol.

        Args:
            ticker: The token ticker symbol (e.g., USDT, USDC)

        Returns:
            Token information
        """
        chain = self.get_chain()
        network = cast(str, chain["network"])
        upper_ticker = ticker.upper()

        for token in self.tokens:
            if token["symbol"].upper() == upper_ticker:
                if network in token["networks"]:
                    return {
                        "symbol": token["symbol"],
                        "decimals": token["decimals"],
                        "name": token["name"],
                    }
                raise ValueError(f"Token {ticker} not configured for network {network}")

        if upper_ticker == "TRX":
            return {
                "symbol": "TRX",
                "decimals": 6,
                "name": "TRON",
            }

        raise ValueError(f"Token with ticker {ticker} not found")

    def _get_token_decimals(self, token_address: str | None = None) -> int:
        """Get the decimals for a token.

        Args:
            token_address: The token address, or None for native currency

        Returns:
            Number of decimals
        """
        if token_address:
            try:
                decimals_result = self.read(
                    {"address": token_address, "abi": TRC20_ABI, "functionName": "decimals", "args": []}
                )
                return int(decimals_result["value"])
            except Exception as e:
                raise ValueError(f"Failed to fetch token decimals: {str(e)}") from e

        return 6

    def convert_to_base_units(self, params: dict[str, Any]) -> str:
        """Convert a token amount to base units.

        Args:
            params: Parameters including amount and optional token address

        Returns:
            Amount in base units
        """
        amount = params["amount"]
        token_address = params.get("tokenAddress")

        TRX_NATIVE_ADDR = "T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb"  # mainnet/nile 通用占位
        if token_address == TRX_NATIVE_ADDR:
            token_address = None

        try:
            if not re.match(r"^[0-9]*\.?[0-9]+$", amount):
                raise ValueError(f"Invalid amount format: {amount}")

            decimals = self._get_token_decimals(token_address)
            base_units = int(Decimal(amount) * (10**decimals))
            return str(base_units)
        except Exception as e:
            raise ValueError(f"Failed to convert to base units: {str(e)}") from e

    def convert_from_base_units(self, params: dict[str, Any]) -> str:
        """Convert a token amount from base units to decimal.

        Args:
            params: Parameters including amount and optional token address

        Returns:
            Human-readable amount
        """
        amount = params["amount"]
        token_address = params.get("tokenAddress")

        # 原生 TRX 同样按 6 位精度处理（同上别名集合规则），无需区分网络
        TRX_NATIVE_ADDR = "T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb"
        ZERO_HEX = "0x0000000000000000000000000000000000000000"
        native_aliases = {None, "", ZERO_HEX, TRX_NATIVE_ADDR}
        if token_address in native_aliases:
            token_address = None

        try:
            if not re.match(r"^[0-9]+$", amount):
                raise ValueError(f"Invalid base unit amount format: {amount}")

            decimals = self._get_token_decimals(token_address)
            decimal_amount = Decimal(amount) / (10**decimals)
            return str(decimal_amount)
        except Exception as e:
            raise ValueError(f"Failed to convert from base units: {str(e)}") from e

    def send_token(self, params: dict[str, Any]) -> dict[str, str]:
        """Send tokens (native or TRC20).

        Args:
            params: Parameters including recipient, amount, and optional token address

        Returns:
            Transaction receipt
        """
        if not self.enable_send:
            raise ValueError("Sending tokens is disabled for this wallet")

        recipient = params["recipient"]
        amount_in_base_units = params["amountInBaseUnits"]
        token_address = params.get("tokenAddress")

        try:
            if token_address:
                return self.send_transaction(
                    {
                        "to": token_address,
                        "abi": TRC20_ABI,
                        "functionName": "transfer",
                        "args": [recipient, int(amount_in_base_units)],
                    }
                )
            else:
                return self.send_transaction(
                    {
                        "to": recipient,
                        "value": int(amount_in_base_units),
                    }
                )
        except Exception as e:
            raise ValueError(f"Failed to send token: {str(e)}") from e

    def get_token_allowance(self, params: dict[str, Any]) -> str:
        """Get the allowance of a TRC20 token for a spender.

        Args:
            params: Parameters including token address, owner, and spender

        Returns:
            Allowance in base units
        """
        token_address = params["tokenAddress"]
        owner = params["owner"]
        spender = params["spender"]

        try:
            allowance_result = self.read(
                {
                    "address": token_address,
                    "abi": TRC20_ABI,
                    "functionName": "allowance",
                    "args": [owner, spender],
                }
            )
            return str(allowance_result["value"])
        except Exception as e:
            raise ValueError(f"Failed to fetch allowance: {str(e)}") from e

    def approve(self, params: dict[str, Any]) -> dict[str, str]:
        """Approve a spender to spend TRC20 tokens.

        Args:
            params: Parameters including token address, spender, and amount

        Returns:
            Transaction receipt
        """
        if not self.enable_send:
            raise ValueError("Approval operations are disabled for this wallet")

        token_address = params["tokenAddress"]
        spender = params["spender"]
        amount = params["amount"]

        try:
            if not re.match(r"^[0-9]+$", amount):
                raise ValueError(f"Invalid base unit amount format: {amount}")

            return self.send_transaction(
                {
                    "to": token_address,
                    "abi": TRC20_ABI,
                    "functionName": "approve",
                    "args": [spender, int(amount)],
                }
            )
        except Exception as e:
            raise ValueError(f"Failed to approve: {str(e)}") from e

    def revoke_approval(self, params: dict[str, Any]) -> dict[str, str]:
        """Revoke approval for a TRC20 token from a spender.

        Args:
            params: Parameters including token address and spender

        Returns:
            Transaction receipt
        """
        return self.approve(
            {
                "tokenAddress": params["tokenAddress"],
                "spender": params["spender"],
                "amount": "0",
            }
        )

    def get_core_tools(self) -> list[ToolBase[Any]]:
        """Get the core tools for this wallet client.

        Returns:
            List of tool definitions
        """
        base_tools = [
            tool for tool in super().get_core_tools() if tool.name != "get_balance"
        ]  # we override the get_balance tool

        common_tron_tools = [
            create_tool(
                {
                    "name": "get_balance",
                    "description": "Get the balance of the wallet for native currency or a specific TRC20 token.",
                    "parameters": GetBalanceParameters,
                },
                lambda params: self.balance_of(params["address"], params.get("tokenAddress")),
            ),
            create_tool(
                {
                    "name": "get_token_info_by_ticker",
                    "description": "Get information about a token by its ticker symbol.",
                    "parameters": GetTokenInfoByTickerParameters,
                },
                lambda params: self.get_token_info_by_ticker(params["ticker"]),
            ),
            create_tool(
                {
                    "name": "convert_to_base_units",
                    "description": "Convert a token amount from human-readable units to base units.",
                    "parameters": ConvertToBaseUnitsParameters,
                },
                self.convert_to_base_units,
            ),
            create_tool(
                {
                    "name": "convert_from_base_units",
                    "description": "Convert a token amount from base units to human-readable units.",
                    "parameters": ConvertFromBaseUnitsParameters,
                },
                self.convert_from_base_units,
            ),
            create_tool(
                {
                    "name": "get_token_allowance_tron",
                    "description": "Get the allowance of a TRC20 token for a spender.",
                    "parameters": GetTokenAllowanceParameters,
                },
                self.get_token_allowance,
            ),
            create_tool(
                {
                    "name": "sign_typed_data_tron",
                    "description": "Sign a typed data structure (TRON equivalent of EIP-712).",
                    "parameters": SignTypedDataParameters,
                },
                lambda params: self.sign_typed_data(
                    params["types"], params["primaryType"], params["domain"], params["value"]
                ),
            ),
            create_tool(
                {
                    "name": "get_account_resource_info",
                    "description": "Get account resource info (energy/bandwidth).",
                    "parameters": GetAccountResourceInfoParameters,
                },
                lambda _params: self.get_account_resource_info(),
            ),
            create_tool(
                {
                    "name": "get_votes",
                    "description": "Get voting stats: totalVotes, usedVotes, availableVotes.",
                    "parameters": GetVotesParameters,
                },
                lambda _params: self.get_votes(),
            ),
            create_tool(
                {
                    "name": "get_pending_reward",
                    "description": "Get pending reward (SUN).",
                    "parameters": GetPendingRewardParameters,
                },
                lambda _params: self.get_pending_reward(),
            ),
        ]

        sending_tron_tools = []
        if self.enable_send:
            sending_tron_tools = [
                create_tool(
                    {
                        "name": "buildSendTrx",
                        "description": "Build an unsigned TRX transfer transaction (amount in SUN).",
                        "parameters": BuildSendTrxParameters,
                    },
                    self.build_send_trx,
                ),
                create_tool(
                    {
                        "name": "buidlSendToken",
                        "description": "Build an unsigned TRC20 token transfer transaction (amount in base units).",
                        "parameters": BuildSendTokenParameters,
                    },
                    self.build_send_token,
                ),
                create_tool(
                    {
                        "name": "send_token",
                        "description": "Send native currency or a TRC20 token to a recipient.",
                        "parameters": SendTokenParameters,
                    },
                    self.send_token,
                ),
                create_tool(
                    {
                        "name": "approve_token_tron",
                        "description": "Approve an amount of a TRC20 token for a spender.",
                        "parameters": ApproveParameters,
                    },
                    self.approve,
                ),
                create_tool(
                    {
                        "name": "revoke_token_approval_tron",
                        "description": "Revoke approval for a TRC20 token from a spender.",
                        "parameters": RevokeApprovalParameters,
                    },
                    self.revoke_approval,
                ),
                create_tool(
                    {
                        "name": "signTransaction",
                        "description": "Sign a TRON transaction payload (JSON formatted).",
                        "parameters": SignTransactionParameters,
                    },
                    lambda params: self.sign_transaction(params["transaction"]),
                ),
                create_tool(
                    {
                        "name": "sendRawTransaction",
                        "description": "Broadcast a signed TRON transaction to the network.",
                        "parameters": SendRawTransactionParameters,
                    },
                    lambda params: self.send_raw_transaction(params["signedTransaction"]),
                ),
                create_tool(
                    {
                        "name": "freeze_balance",
                        "description": "Freeze TRX to obtain ENERGY or BANDWIDTH (Stake 2.0). Amount is in SUN.",
                        "parameters": FreezeBalanceParameters,
                    },
                    self.freeze_balance,
                ),
                create_tool(
                    {
                        "name": "unfreeze_balance",
                        "description": "Unstake TRX (Stake 2.0). Optional amount in SUN; omitting unfreezes all for the resource.",
                        "parameters": UnfreezeBalanceParameters,
                    },
                    self.unfreeze_balance,
                ),
                create_tool(
                    {
                        "name": "withdraw_stake_balance",
                        "description": "Withdraw expired unstaked TRX after cool-down period (Stake 2.0).",
                        "parameters": WithdrawStakeBalanceParameters,
                    },
                    self.withdraw_stake_balance,
                ),
                create_tool(
                    {
                        "name": "delegate_resource",
                        "description": "Delegate ENERGY/BANDWIDTH to another address (Stake 2.0). Amount in SUN.",
                        "parameters": DelegateResourceParameters,
                    },
                    self.delegate_resource,
                ),
                create_tool(
                    {
                        "name": "undelegate_resource",
                        "description": "Cancel delegation of ENERGY/BANDWIDTH to another address (Stake 2.0). Amount in SUN.",
                        "parameters": UndelegateResourceParameters,
                    },
                    self.undelegate_resource,
                ),
                create_tool(
                    {
                        "name": "vote_witness",
                        "description": "Vote for witnesses. Provide a list of {witnessAddress, voteCount}.",
                        "parameters": VoteWitnessParameters,
                    },
                    self.vote_witness,
                ),
                create_tool(
                    {
                        "name": "withdraw_rewards",
                        "description": "Withdraw voting rewards.",
                        "parameters": WithdrawRewardsParameters,
                    },
                    self.withdraw_rewards,
                ),
            ]

        return base_tools + common_tron_tools + sending_tron_tools
