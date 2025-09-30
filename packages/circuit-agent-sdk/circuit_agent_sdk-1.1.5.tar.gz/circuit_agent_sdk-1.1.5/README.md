# Circuit Agent SDK - Python

> **Clean, type-safe Python SDK for building cross-chain agents on the circuit platform**

A Python SDK for building automated agents to deploy on Circuit. Features a simple API surface with just **3 main methods** and full type safety.

> **💡 Best used with [Circuit Agents CLI](https://github.com/circuitorg/agents-cli)** - Deploy, manage, and test your agents with ease

## ✨ Features

- **🎯 Simple API**: Only 3 main methods - `send_log()`, `sign_and_send()`, and `swidge.*` (swap/bridge)
- **🔒 Type Hinting**: Network parameter determines valid request shapes automatically
- **🚀 Cross-Chain**: Unified interface for EVM and Solana networks
- **🌉 Cross-Chain Swaps**: Built-in Swidge integration for seamless token swaps and bridges

## 🚀 Quick Start
### Install the SDK
```bash
pip install circuit-agent-sdk
# or with uv
uv pip install circuit-agent-sdk
```

### Sample SDK Usage
>**NOTE:** The fastest, and recommended, way to get started is to setup an agent via the circuit [CLI](https://github.com/circuitorg/agents-cli)'s 'circuit agent init' command. This will setup a sample agent directory with the necessary agent wireframe, and configure the cli to allow you for easy testing and deployment. You just simply need to add in your secret formula to the execution and stop functions.

```python
from agent_sdk import AgentSdk, SDKConfig

# Initialize the sdk
sdk = AgentSdk(SDKConfig(
    session_id=123
))
```

## 🎯 Core SDK API (Only 2 Methods!)

### 1. Add Logs to Timeline

```python
await sdk.send_log({
    "type": "observe",
    "short_message": "Starting swap operation"
})
```

### 2. Sign & Send Transactions

#### Ethereum (any EVM chain)

```python
# Native ETH transfer
await sdk.sign_and_send({
    "network": "ethereum:1",  # Chain ID in network string
    "request": {
        "to_address": "0x742d35cc6634C0532925a3b8D65e95f32B6b5582",
        "data": "0x",
        "value": "1000000000000000000"  # 1 ETH in wei
    },
    "message": "Sending 1 ETH"
})

# Contract interaction
await sdk.sign_and_send({
    "network": "ethereum:42161",  # Arbitrum
    "request": {
        "to_address": "0xTokenContract...",
        "data": "0xa9059cbb...",  # encoded transfer()
        "value": "0"
    }
})
```

#### Solana

```python
await sdk.sign_and_send({
    "network": "solana",
    "request": {
        "hex_transaction": "010001030a0b..."  # serialized VersionedTransaction
    }
})
```


## 🌉 Cross-Chain Swaps with Swidge

The SDK includes built-in Swidge integration for seamless cross-chain token swaps and bridges.

Swidge provides a unified interface that handles both **swapping** (exchanging tokens within the same network) and **bridging** (moving tokens across different networks) through a single, easy-to-use API. Whether you're doing a simple token swap on Ethereum or bridging assets across chains, the same quote-and-execute pattern works for everything.

### 3. Cross-Chain Swaps & Bridges

#### Get a Quote

```python
# 🌉 Bridge USDC: Polygon → Arbitrum
bridge_quote = sdk.swidge.quote({
    "from": {"network": "ethereum:137", "address": user_address},
    "to": {"network": "ethereum:42161", "address": user_address},
    "amount": "50000000",  # $50 USDC (6 decimals)
    "fromToken": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",  # USDC on Polygon
    "toToken": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",   # USDC on Arbitrum
    "slippage": "2.0",  # 2% slippage for cross-chain (default: 0.5%)
    "priceImpact": "1.0"  # 1% max price impact (default: 0.5%)
})

# 🔄 Swap USDC → ETH on same chain (using defaults)
swap_quote = sdk.swidge.quote({
    "from": {"network": "ethereum:42161", "address": user_address},
    "to": {"network": "ethereum:42161", "address": user_address},
    "amount": "100000000",  # $100 USDC (6 decimals)
    "fromToken": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",  # USDC
    # toToken omitted = native ETH (default behavior)
    # slippage defaults to "0.5", priceImpact defaults to "0.5"
})

if quote.success:
    print(f"💰 You'll receive: {quote.data.asset_receive.amountFormatted}")
    print(f"💸 Total fees: {', '.join([f.name for f in quote.data.fees])}")
elif quote.error:
    # Check for specific error types
    if quote.error == "Wallet not found":
        print("👛 Wallet not found")
    elif quote.error == "From wallet does not match session wallet":
        print("🔐 Wallet address doesn't match session")
    else:
        print("❓ Quote not available for this swap")
```

#### Execute a Swap

```python
# 1️⃣ Get a quote first
quote_request = {
    "from": {"network": "ethereum:42161", "address": user_address},
    "to": {"network": "ethereum:1", "address": user_address},
    "amount": "100000000",  # $100 USDC
    "fromToken": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",  # USDC on Arbitrum
    "priceImpact": "0.1",  # Conservative price impact setting
    "slippage": "5.0"
}

quote = sdk.swidge.quote(quote_request)

# 2️⃣ Handle quote failures with retry logic
if quote.error == "No quote provided":
    print("❓ Quote not available, increasing price impact and retrying...")
    # Retry with more permissive parameters
    quote_request["priceImpact"] = "10.0"
    quote_request["slippage"] = "10.0"
    quote = sdk.swidge.quote(quote_request)

# 3️⃣ Execute the swap if quote succeeded
if quote.success and quote.data:
    print(f"💰 Expected to receive: {quote.data.asset_receive.amountFormatted}")
    print(f"💸 Fees: {', '.join([f'{f.name}: {f.amountFormatted}' for f in quote.data.fees])}")

    result = sdk.swidge.execute(quote.data)

    if result.success and result.data:
        print(f"🎉 Status: {result.data.status}")

        if result.data.status == "success":
            print(f"📤 Sent: {result.data.in.txs[0]}")
            print(f"📥 Received: {result.data.out.txs[0]}")
            print("✅ Cross-chain swap completed!")
        elif result.data.status == "failure":
            print("❌ Transaction failed")
        elif result.data.status == "refund":
            print("↩️ Transaction was refunded")
        elif result.data.status == "delayed":
            print("⏰ Transaction is delayed")
    else:
        print(f"❌ Execute failed: {result.error}")
else:
    print(f"❌ Quote failed after retry: {quote.error}")
    return {"success": False}
```

### Swidge API Reference

#### `sdk.swidge.quote(request: SwidgeQuoteRequest | dict) -> SwidgeQuoteResponse`

Get pricing and routing information for token swaps between networks or within the same network.

**Parameters:**
```python
{
    "from": {"network": str, "address": str},
    "to": {"network": str, "address": str},
    "amount": str,                    # Amount in token's smallest unit
    "fromToken": str | None,          # Source token contract (omit for native tokens)
    "toToken": str | None,           # Destination token contract (omit for native tokens)
    "slippage": str | None,           # Slippage tolerance % (default: "0.5")
    "priceImpact": str | None        # Max price impact % (default: "0.5")
}
```

**Returns:**
```python
{
    "success": bool,
    "data": {
        "engine": "relay",
        "asset_send": {
            "network": str,
            "address": str,
            "token": str | None,
            "amount": str,
            "amountFormatted": str,
            "amountUsd": str,
            # ... additional fields
        },
        "asset_receive": {
            "network": str,
            "address": str,
            "token": str | None,
            "amount": str,
            "amountFormatted": str,
            "amountUsd": str,
            # ... additional fields
        },
        "priceImpact": {
            "usd": str | None,
            "percentage": str | None
        },
        "fees": [
            {
                "name": str,
                "amount": str | None,
                "amountFormatted": str | None,
                "amountUsd": str | None
            }
        ],
        "steps": [
            # Transaction and signature steps
        ]
    } | None,
    "error": str | None,
    "errorDetails": dict | None
}
```

⚠️ **Important Notes:**
- **Small amounts may fail**: Use at least $10-20 worth to avoid fee/slippage issues
- **Slippage matters**: Default is 0.5% for most cases, increase to 1-2% for volatile pairs
- **Different networks = bridge**: Same network = swap

#### `sdk.swidge.execute(quoteData: SwidgeQuoteData) -> SwidgeExecuteResponse`

Execute a cross-chain swap or bridge using a quote from `sdk.swidge.quote()`.

⚠️ **What happens:**
- Signs transactions using your wallet's policy engine
- Broadcasts to the blockchain(s)
- Waits for cross-chain completion (this may take some time depending on network status)
- Returns final status with transaction hashes

**Parameters:**
- `quote_data`: Complete quote object from `sdk.swidge.quote()`

**Returns:**
```python
{
    "success": bool,
    "data": {
        "status": "success" | "failure" | "refund" | "delayed",
        "in": {
            "network": str,
            "txs": [str]  # Transaction hashes
        },
        "out": {
            "network": str,
            "txs": [str]  # Transaction hashes
        },
        "lastUpdated": int  # Timestamp
    } | None,
    "error": str | None,
    "errorDetails": dict | None
}
```
