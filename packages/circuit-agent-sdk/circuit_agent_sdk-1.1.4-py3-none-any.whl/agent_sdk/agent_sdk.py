"""
Main AgentSdk class with simplified API surface.

This module provides the primary AgentSdk class that serves as the main entry point
for all agent operations. It offers a clean, type-safe interface with just two
core methods that cover the majority of agent interactions.
"""

from typing import Any

from .client import APIClient
from .types import (
    AddLogRequest,
    EthereumSignRequest,
    EvmMessageSignRequest,
    EvmMessageSignResponse,
    SDKConfig,
    SignAndSendRequest,
    SignAndSendResponse,
    SolanaSignRequest,
    SwidgeExecuteResponse,
    SwidgeExecuteResponseData,
    SwidgeQuoteData,
    SwidgeQuoteRequest,
    SwidgeQuoteResponse,
    UpdateJobStatusRequest,
    UpdateJobStatusResponse,
    get_chain_id_from_network,
    is_ethereum_network,
    is_solana_network,
)


class AgentSdk:
    """
    Main SDK entrypoint used by agents to interact with the Circuit backend.

    Provides a minimal sdk with three core methods that cover the
    majority of agent interactions:

    - send_log() — emit timeline logs for observability and UX
    - sign_message() — sign EIP712 and EIP191 messages on EVM networks
    - sign_and_send() — sign and broadcast transactions across networks
    - swidge — cross-chain swap operations
    """

    # Type annotation for the swidge property - this helps IDEs understand the type
    swidge: "SwidgeApi"

    def __init__(self, config: SDKConfig) -> None:
        """
        Create a new AgentSdk instance.

        Args:
            config: SDK configuration
                - session_id: Numeric session identifier that scopes auth and actions
                - verbose: When True, prints detailed request/response logs
                - testing: When True, short-circuits network calls with mock values
                - base_url: Override API base URL (detected automatically otherwise)

        Example:
            ```python
            sdk = AgentSdk(SDKConfig(session_id=42, verbose=True))
            ```
        """
        self.config = config
        self.client = APIClient(config)
        # Pass the sign_and_send method to utils to avoid circular dependency
        # self.utils = AgentUtils(self.client, self.config, self.sign_and_send)

        # Initialize swidge property
        self.swidge = SwidgeApi(self)

    def _mask_sensitive_data(self, data: Any) -> Any:
        """
        Mask sensitive information in data structures.

        Args:
            data: Data to mask

        Returns:
            Data with sensitive information masked
        """
        if isinstance(data, dict):
            masked_data = {}
            for key, value in data.items():
                if key.lower() in ["authorization", "x-api-key", "bearer", "token"]:
                    if isinstance(value, str) and len(value) > 8:
                        # Show first 8 characters and mask the rest
                        masked_data[key] = f"{value[:8]}...***MASKED***"
                    else:
                        masked_data[key] = "***MASKED***"
                else:
                    masked_data[key] = self._mask_sensitive_data(value)
            return masked_data
        elif isinstance(data, list):
            return [self._mask_sensitive_data(item) for item in data]
        else:
            return data

    def _log(self, log: str, data: Any = None) -> None:
        """Log debug information when verbose mode is enabled."""
        if self.config.verbose:
            log_message = f"[AGENT SDK DEBUG] {log}"
            if data is not None:
                import json

                masked_data = self._mask_sensitive_data(data)
                log_message += f" {json.dumps(masked_data, indent=2, default=str)}"
            print(log_message)

    def send_log(self, log: AddLogRequest | dict) -> None:
        """Add a log to the agent timeline.

        Args:
            log: Log entry with 'type' and 'short_message' fields.
                type: One of "observe", "validate", "reflect", "error", "warning"
                short_message: Brief message (max 250 chars, auto-truncated)

        Example:
            sdk.send_log({"type": "observe", "short_message": "Starting swap"})
        """
        # Handle both dict and Pydantic model inputs
        try:
            if isinstance(log, dict):
                # Automatically truncate logs that exceed 250 characters before validation
                if "short_message" in log and len(log["short_message"]) > 250:
                    original_message = log["short_message"]
                    truncated_message = original_message[:247] + "..."
                    self._log(
                        f"Message truncated from {len(original_message)} to 250 characters"
                    )
                    log["short_message"] = truncated_message

                # Convert dict to Pydantic model for validation and type safety
                message_obj = AddLogRequest(**log)
            else:
                # For Pydantic models, we need to handle truncation differently
                # since validation already happened. We'll create a new dict and truncate it.
                message_dict = log.model_dump()

                if len(message_dict["short_message"]) > 250:
                    original_message = message_dict["short_message"]
                    truncated_message = original_message[:247] + "..."
                    self._log(
                        f"Message truncated from {len(original_message)} to 250 characters"
                    )
                    message_dict["short_message"] = truncated_message
                    # Create a new Pydantic model with the truncated log
                    message_obj = AddLogRequest(**message_dict)
                else:
                    message_obj = log
        except Exception as validation_error:
            # Enhanced error logging for Pydantic validation failures
            error_type = type(validation_error).__name__
            error_message = str(validation_error)
            self._log(
                "SEND_LOG_VALIDATION_ERROR",
                {
                    "error_type": error_type,
                    "error": error_message,
                    "log_input": log,
                    "log_type": type(log).__name__,
                },
            )
            # Silently fail - validation errors shouldn't crash the agent
            return

        self._log("ADD_LOG", message_obj.model_dump())

        # Convert to the internal logs format
        logs_request = [
            {"type": message_obj.type, "shortMessage": message_obj.short_message}
        ]

        try:
            self._send_logs(logs_request)
        except Exception as e:
            # Log the error but don't let it bubble up to user code
            error_type = type(e).__name__
            error_message = str(e)
            self._log(
                "SEND_LOG_ERROR",
                {
                    "error_type": error_type,
                    "error": error_message,
                    "log_data": logs_request,
                },
            )
            # Silently fail - logging errors shouldn't crash the agent

    def sign_and_send(self, request: SignAndSendRequest | dict) -> SignAndSendResponse:
        """Sign and broadcast a transaction on the specified network.

        Args:
            request: Transaction request with 'network', 'request', and optional 'message' fields.
                network: "solana" or "ethereum:chainId" (e.g., "ethereum:1", "ethereum:42161")
                message: Optional context message for observability (max 250 chars)
                request: Transaction payload
                    For Ethereum:
                        to_address: Recipient address as hex string
                        data: Calldata as hex string (use "0x" for transfers)
                        value: Wei amount as string
                        gas: Gas limit (optional)
                        max_fee_per_gas: Max fee per gas in wei as string (optional)
                        max_priority_fee_per_gas: Max priority fee per gas in wei as string (optional)
                        nonce: Transaction nonce (optional)
                        enforce_transaction_success: Enforce transaction success (optional)
                    For Solana:
                        hex_transaction: Serialized VersionedTransaction as hex string

        Returns:
            SignAndSendResponse with success status and transaction hash or error details.

        Example:
            sdk.sign_and_send({
                "network": "ethereum:42161",
                "request": {
                    "to_address": "0xabc...",
                    "data": "0x",
                    "value": "1000000000000000",
                    "gas": 21000,
                    "max_fee_per_gas": "20000000000"
                },
                "message": "Transfer"
            })
        """
        try:
            # Handle both dict and Pydantic model inputs (like TypeScript SDK)
            if isinstance(request, dict):
                # Convert dict to Pydantic model for validation and type safety
                request_obj = SignAndSendRequest(**request)
            else:
                request_obj = request
            self._log(
                "SIGN_AND_SEND",
                {
                    "request": request_obj.model_dump(),
                    "testing_mode": self.config.testing,
                },
            )

            if self.config.testing:
                return SignAndSendResponse(
                    success=True,
                    internal_transaction_id=123,
                    tx_hash=(
                        "0xTEST"
                        if is_ethereum_network(request_obj.network)
                        else "TEST_SOL_TX"
                    ),
                    transaction_url=None,
                    error=None,
                    error_details=None,
                )

            if is_ethereum_network(request_obj.network):
                chain_id = get_chain_id_from_network(request_obj.network)

                # Ensure we have an Ethereum request
                if not isinstance(request_obj.request, EthereumSignRequest):
                    return SignAndSendResponse(
                        success=False,
                        internal_transaction_id=None,
                        tx_hash=None,
                        transaction_url=None,
                        error="Ethereum network requires EthereumSignRequest",
                        error_details={
                            "message": "Ethereum network requires EthereumSignRequest"
                        },
                    )

                # Build request payload, only including non-None values
                payload = {
                    "chainId": chain_id,
                    "toAddress": request_obj.request.to_address,
                    "data": request_obj.request.data,
                    "valueWei": request_obj.request.value,  # Map 'value' to 'valueWei'
                }

                if request_obj.message is not None:
                    payload["message"] = request_obj.message
                # Only add optional fields if they have values
                if request_obj.request.gas is not None:
                    payload["gas"] = request_obj.request.gas
                if request_obj.request.max_fee_per_gas is not None:
                    payload["maxFeePerGas"] = request_obj.request.max_fee_per_gas
                if request_obj.request.max_priority_fee_per_gas is not None:
                    payload["maxPriorityFeePerGas"] = (
                        request_obj.request.max_priority_fee_per_gas
                    )
                if request_obj.request.nonce is not None:
                    payload["nonce"] = request_obj.request.nonce
                if request_obj.request.enforce_transaction_success is not None:
                    payload["enforceTransactionSuccess"] = (
                        request_obj.request.enforce_transaction_success
                    )

                return self._handle_evm_transaction(payload)

            if is_solana_network(request_obj.network):
                # Ensure we have a Solana request
                if not isinstance(request_obj.request, SolanaSignRequest):
                    return SignAndSendResponse(
                        success=False,
                        internal_transaction_id=None,
                        tx_hash=None,
                        transaction_url=None,
                        error="Solana network requires SolanaSignRequest",
                        error_details={
                            "message": "Solana network requires SolanaSignRequest"
                        },
                    )

                return self._handle_solana_transaction(
                    {
                        "hexTransaction": request_obj.request.hex_transaction,
                        "message": request_obj.message,
                    }
                )

            return SignAndSendResponse(
                success=False,
                internal_transaction_id=None,
                tx_hash=None,
                transaction_url=None,
                error=f"Unsupported network: {request_obj.network}",
                error_details={
                    "message": f"Unsupported network: {request_obj.network}"
                },
            )

        except Exception as e:
            self._log("SIGN_AND_SEND_ERROR", {"error": str(e)})
            return SignAndSendResponse(
                success=False,
                internal_transaction_id=None,
                tx_hash=None,
                transaction_url=None,
                error=str(e),
                error_details={"message": str(e), "type": type(e).__name__},
            )

    def sign_message(
        self, request: EvmMessageSignRequest | dict
    ) -> EvmMessageSignResponse:
        """
        Sign a message on an EVM network.

        Args:
            request: EVM message signing input
                - messageType: "eip712" or "eip191"
                - chainId: Ethereum chain ID
                - data: Message data structure

        Returns:
            EvmMessageSignResponse with signature components
        """
        if isinstance(request, dict):
            request_obj = EvmMessageSignRequest(**request)
        else:
            request_obj = request

        self._log(
            "SIGN_MESSAGE",
            {"request": request_obj.model_dump(), "testing_mode": self.config.testing},
        )

        if self.config.testing:
            return EvmMessageSignResponse(
                status=200,
                v=27,
                r="0xTEST_R",
                s="0xTEST_S",
                formattedSignature="0xTEST_SIGNATURE",
                type="evm",
            )

        try:
            # Call the message signing endpoint
            response = self.client.post("/v1/messages/evm", request_obj.model_dump())
            return EvmMessageSignResponse(**response)
        except Exception as e:
            self._log("SIGN_MESSAGE_ERROR", {"error": str(e)})
            # Return an error response instead of letting the exception bubble up
            return EvmMessageSignResponse(
                status=400, v=0, r="0x0", s="0x0", formattedSignature="0x0", type="evm"
            )

    def _update_job_status(
        self, request: UpdateJobStatusRequest | dict
    ) -> UpdateJobStatusResponse:
        """
        Internal method to update job status. Used by the Agent wrapper for automatic tracking.

        This method is not intended for direct use by agent developers - job status tracking
        is handled automatically by the Agent wrapper.
        """
        # Handle both dict and Pydantic model inputs
        if isinstance(request, dict):
            request_obj = UpdateJobStatusRequest(**request)
        else:
            request_obj = request

        self._log("UPDATE_JOB_STATUS", request_obj.model_dump())

        if self.config.testing:
            return UpdateJobStatusResponse(
                status=200,
                message="Job status updated successfully (TESTING)",
            )

        # Call the job status update endpoint
        # Don't include jobId in body since it's in the URL path
        payload: dict[str, str] = {
            "status": request_obj.status,
        }
        if request_obj.errorMessage:
            payload["errorMessage"] = request_obj.errorMessage

        try:
            response = self.client.post(f"/v1/jobs/{request_obj.jobId}/status", payload)
            return UpdateJobStatusResponse(**response)
        except Exception as e:
            self._log("UPDATE_JOB_STATUS_ERROR", {"error": str(e)})
            # Return an error response instead of letting the exception bubble up
            return UpdateJobStatusResponse(
                status=400, message=f"Failed to update job status: {str(e)}"
            )

    # =====================
    # Private Implementation Methods (migrated from AgentToolset)
    # =====================

    def _handle_evm_transaction(self, request: dict[str, Any]) -> SignAndSendResponse:
        """Handle EVM transaction signing and broadcasting."""
        try:
            # 1) Sign the transaction
            sign_response = self.client.post("/v1/transactions/evm", request)

            # 2) Broadcast the transaction
            transaction_id = sign_response["internalTransactionId"]
            broadcast_response = self.client.post(
                f"/v1/transactions/evm/{transaction_id}/broadcast"
            )

            return SignAndSendResponse(
                success=True,
                internal_transaction_id=transaction_id,
                tx_hash=broadcast_response["txHash"],
                transaction_url=broadcast_response.get("transactionUrl"),
                error=None,
                error_details=None,
            )
        except Exception as e:
            self._log("EVM_TRANSACTION_ERROR", {"error": str(e)})

            # Extract error details from HTTP error
            error_details = {"message": str(e), "type": type(e).__name__}

            # Try to extract status code if it's an HTTP error
            if hasattr(e, "response") and hasattr(e.response, "status_code"):
                error_details["status"] = e.response.status_code
                reason = getattr(e.response, "reason", None)
                if reason is not None:
                    error_details["status_text"] = str(reason)

            return SignAndSendResponse(
                success=False,
                internal_transaction_id=None,
                tx_hash=None,
                transaction_url=None,
                error=str(e),
                error_details=error_details,
            )

    def _handle_solana_transaction(
        self, request: dict[str, Any]
    ) -> SignAndSendResponse:
        """Handle Solana transaction signing and broadcasting."""
        try:
            # 1) Sign the transaction
            sign_response = self.client.post("/v1/transactions/solana", request)

            # 2) Broadcast the transaction
            transaction_id = sign_response["internalTransactionId"]
            broadcast_response = self.client.post(
                f"/v1/transactions/solana/{transaction_id}/broadcast"
            )

            return SignAndSendResponse(
                success=True,
                internal_transaction_id=transaction_id,
                tx_hash=broadcast_response["txHash"],
                transaction_url=broadcast_response.get("transactionUrl"),
                error=None,
                error_details=None,
            )
        except Exception as e:
            self._log("SOLANA_TRANSACTION_ERROR", {"error": str(e)})

            # Extract error details from HTTP error
            error_details = {"message": str(e), "type": type(e).__name__}

            # Try to extract status code if it's an HTTP error
            if hasattr(e, "response") and hasattr(e.response, "status_code"):
                error_details["status"] = e.response.status_code
                reason = getattr(e.response, "reason", None)
                if reason is not None:
                    error_details["status_text"] = str(reason)

            return SignAndSendResponse(
                success=False,
                internal_transaction_id=None,
                tx_hash=None,
                transaction_url=None,
                error=str(e),
                error_details=error_details,
            )

    def _send_logs(self, logs: list) -> dict[str, Any]:
        """Send logs to the agent timeline (migrated from AgentToolset)."""
        if self.config.testing:
            print(f"Logs added successfully (TESTING): {logs}")
            return {
                "status": 200,
                "message": "Logs added successfully (TESTING)",
            }

        return self.client.post("/v1/logs", logs)


class SwidgeApi:
    """Cross-chain swap operations using Swidge.

    Workflow: quote() -> execute(quote.data) -> check result.data.status
    """

    def __init__(self, sdk: "AgentSdk"):
        self._sdk = sdk

    def quote(self, request: SwidgeQuoteRequest | dict) -> SwidgeQuoteResponse:
        """Get a cross-chain swap or bridge quote.

        Args:
            request: Quote parameters with wallet info, amount, and optional tokens/slippage.
                from: Source wallet {"network": "ethereum:1", "address": "0x..."}
                to: Destination wallet {"network": "ethereum:42161", "address": "0x..."}
                amount: Amount in smallest unit (e.g., "1000000000000000000" for 1 ETH)
                fromToken: Source token address (optional, omit for native tokens)
                toToken: Destination token address (optional, omit for native tokens)
                slippage: Slippage tolerance % as string (default: "0.5")
                priceImpact: Max price impact % as string (default: "0.5")

        Returns:
            SwidgeQuoteResponse with pricing, fees, and transaction steps.

        Example:
            quote = sdk.swidge.quote({
                "from": {"network": "ethereum:1", "address": user_address},
                "to": {"network": "ethereum:42161", "address": user_address},
                "amount": "1000000000000000000",  # 1 ETH
                "toToken": "0x2f2a2543B76A4166549F7aaB2e75BEF0aefC5b0f"  # WBTC
            })
        """
        return self._handle_swidge_quote(request)

    def execute(self, quote_data: SwidgeQuoteData) -> SwidgeExecuteResponse:
        """Execute a cross-chain swap or bridge using a quote.

        Args:
            quote_data: Complete quote object from sdk.swidge.quote().

        Returns:
            SwidgeExecuteResponse with transaction status and details.

        Example:
            quote = sdk.swidge.quote({...})
            if quote.success and quote.data:
                result = sdk.swidge.execute(quote.data)
        """
        return self._handle_swidge_execute(quote_data)

    def _handle_swidge_quote(
        self, request: SwidgeQuoteRequest | dict
    ) -> SwidgeQuoteResponse:
        """Handle swidge quote requests."""
        self._sdk._log("=== SWIDGE QUOTE ===")
        self._sdk._log("Request:", request)
        self._sdk._log("Testing mode:", self._sdk.config.testing)
        self._sdk._log("===================")

        try:
            # Handle both dict and Pydantic model inputs
            if isinstance(request, dict):
                request_obj = SwidgeQuoteRequest(**request)
            else:
                request_obj = request

            if self._sdk.config.testing:
                test_data = {
                    "engine": "relay",
                    "assetSend": {
                        "network": request_obj.from_.network,
                        "address": request_obj.from_.address,
                        "token": request_obj.fromToken,
                        "name": "Test Asset",
                        "symbol": "TEST",
                        "decimals": 18,
                        "amount": request_obj.amount,
                        "minimumAmount": request_obj.amount,
                        "amountFormatted": "1.0",
                        "amountUsd": "100.00",
                    },
                    "assetReceive": {
                        "network": request_obj.to.network,
                        "address": request_obj.to.address,
                        "token": request_obj.toToken,
                        "name": "Test Asset",
                        "symbol": "TEST",
                        "decimals": 18,
                        "amount": "950000000000000000",
                        "minimumAmount": "950000000000000000",
                        "amountFormatted": "0.95",
                        "amountUsd": "95.00",
                    },
                    "priceImpact": {"percentage": "0.5", "usd": "5.00"},
                    "fees": [
                        {
                            "name": "gas",
                            "amount": "21000000000000000",
                            "amountFormatted": "0.021",
                            "amountUsd": "2.10",
                        }
                    ],
                    "steps": [
                        {
                            "type": "transaction",
                            "description": "Test swap transaction",
                            "transactionDetails": {
                                "type": "evm",
                                "from": "0x1234567890123456789012345678901234567890",
                                "to": "0x1234567890123456789012345678901234567890",
                                "chainId": 1,
                                "value": 0,
                                "data": "0x",
                                "gas": 21000,
                                "maxFeePerGas": 20000000000,
                                "maxPriorityFeePerGas": 1000000000,
                            },
                            "metadata": {"requestId": "test-request-id"},
                        }
                    ],
                }
                return SwidgeQuoteResponse(
                    success=True,
                    error=None,
                    errorDetails=None,
                    data=SwidgeQuoteData.model_validate(test_data),
                )

            response = self._sdk.client.post(
                "/v1/swidge/quote",
                request_obj.model_dump(by_alias=True, exclude_none=True),
            )

            return SwidgeQuoteResponse(
                success=True,
                error=None,
                errorDetails=None,
                data=SwidgeQuoteData(**response),
            )
        except Exception as error:
            self._sdk._log("=== SWIDGE QUOTE ERROR ===")
            self._sdk._log("Error:", error)
            self._sdk._log("=========================")

            error_message = "Failed to get swidge quote"
            status = None
            status_text = None

            if isinstance(error, Exception):
                error_message = str(error)

                # Try to extract HTTP status from error message
                if hasattr(error, "response") and hasattr(
                    error.response, "status_code"
                ):
                    status = error.response.status_code
                    if hasattr(error.response, "reason"):
                        status_text = str(error.response.reason)

            return SwidgeQuoteResponse(
                success=False,
                data=None,
                error=error_message,
                errorDetails={
                    "message": error_message,
                    "status": status,
                    "statusText": status_text,
                },
            )

    def _handle_swidge_execute(
        self, quote_data: SwidgeQuoteData
    ) -> SwidgeExecuteResponse:
        """Handle swidge execute requests."""
        self._sdk._log("=== SWIDGE EXECUTE ===")
        self._sdk._log("Quote:", quote_data)
        self._sdk._log("Testing mode:", self._sdk.config.testing)
        self._sdk._log("=====================")

        try:
            if self._sdk.config.testing:
                import time

                execute_data = {
                    "status": "success",
                    "in": {
                        "network": quote_data.assetSend.network,
                        "txs": [
                            "0x1234567890123456789012345678901234567890123456789012345678901234"
                        ],
                    },
                    "out": {
                        "network": quote_data.assetReceive.network,
                        "txs": [
                            "0x1234567890123456789012345678901234567890123456789012345678901234"
                        ],
                    },
                    "lastUpdated": int(
                        time.time() * 1000
                    ),  # Current timestamp in milliseconds
                }
                return SwidgeExecuteResponse(
                    success=True,
                    error=None,
                    errorDetails=None,
                    data=SwidgeExecuteResponseData.model_validate(execute_data),
                )

            self._sdk._log("Making execute request to /v1/swidge/execute")
            response = self._sdk.client.post(
                "/v1/swidge/execute",
                quote_data.model_dump(by_alias=True, exclude_none=True),
            )
            self._sdk._log("Execute response received:", response)

            return SwidgeExecuteResponse(
                success=True,
                error=None,
                errorDetails=None,
                data=SwidgeExecuteResponseData(**response),
            )
        except Exception as error:
            self._sdk._log("=== SWIDGE EXECUTE ERROR ===")
            self._sdk._log("Error:", error)
            self._sdk._log("============================")

            error_message = "Failed to execute swidge swap"
            status = None
            status_text = None

            if isinstance(error, Exception):
                error_message = str(error)

                # Try to extract HTTP status from error message
                if hasattr(error, "response") and hasattr(
                    error.response, "status_code"
                ):
                    status = error.response.status_code
                    if hasattr(error.response, "reason"):
                        status_text = str(error.response.reason)

            return SwidgeExecuteResponse(
                success=False,
                data=None,
                error=error_message,
                errorDetails={
                    "message": error_message,
                    "status": status,
                    "statusText": status_text,
                },
            )

    # No legacy methods - clean major version!
