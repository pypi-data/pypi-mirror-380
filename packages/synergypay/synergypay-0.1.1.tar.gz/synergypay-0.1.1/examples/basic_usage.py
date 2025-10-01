"""
Basic usage example for SynergyPay SDK.

This example demonstrates:
1. Agent registration with wallet generation
2. Sending Web3 payments
3. Verifying payments on-chain
4. A2A communication with payment context
"""

import asyncio
import os
from synergypay import SynergyPayAgent

# Example configuration (you can use either env vars OR constructor params)
EXAMPLE_CONFIG = {
    "WEB3_RPC_URL": "https://polygon-amoy.g.alchemy.com/v2/aa4IWs1eAs5AW8HradhbXMTTPi1WbGSS",
    "CHAIN_ID": "80002",
    "TOKEN_ADDRESS": "0x0",
    "SERVICE_PRICE_WEI": "1000000000000000",
    "OWNER_PUB_KEY": "0x519BB090e59527df951725952F1000C083F512a3"
}


def setup_environment():
    """Setup environment variables for the example (Option A)."""
    for key, value in EXAMPLE_CONFIG.items():
        os.environ[key] = value


def example_with_constructor():
    """Example: Initialize agent with constructor parameters (Option B)."""
    print("\n=== Initialize with Constructor Parameters ===")
    
    # No .env file needed - pass everything via constructor
    agent = SynergyPayAgent(
        web3_rpc_url="https://polygon-amoy.g.alchemy.com/v2/aa4IWs1eAs5AW8HradhbXMTTPi1WbGSS",
        chain_id=80002,
        token_address="0x0",
        service_price_wei=1000000000000000,
        owner_pub_key="0x519BB090e59527df951725952F1000C083F512a3"
    )
    
    print("✅ Agent initialized with constructor parameters")
    print(f"   RPC URL: {agent.web3_rpc_url}")
    print(f"   Chain ID: {agent.chain_id}")
    
    return agent


def example_agent_registration():
    """Example: Register an agent with wallet generation."""
    print("=== Agent Registration Example ===")
    
    agent = SynergyPayAgent()
    
    # Example custom device ID and bot metadata
    custom_device_id = "custom-device-123"
    bot_metadata = {
        "description": "Payment processing agent",
        "version": "1.0.0",
        "capabilities": ["payment", "verification", "a2a"],
        "network": "polygon-amoy"
    }
    
    # Register agent with required device_id and custom parameters
    result = agent.register_agent(
        agent_name="ExampleAgent",
        device_id=custom_device_id,
        bot_metadata=bot_metadata
    )
    
    if result["status"] == "success":
        print(f"✅ Agent registered successfully!")
        print(f"   Address: {result['address']}")
        print(f"   Device ID: {result['device_id']}")
        print(f"   Bot Metadata: {result['bot_metadata']}")
        print(f"   API Registration: {result['api_registration']}")
    else:
        print(f"❌ Agent registration failed: {result['message']}")
    
    return agent


def example_error_when_device_id_missing():
    """Example: Show error when device_id is not provided."""
    print("\n=== Error Example: Missing Device ID ===")
    
    agent = SynergyPayAgent()
    
    try:
        # This will fail because device_id is required but not provided
        result = agent.register_agent("BadAgent")  # Missing device_id parameter
        
        if result["status"] == "error":
            print(f"❌ Expected error: {result['message']}")
        else:
            print(f"⚠️ Unexpected success: {result}")
    except TypeError as e:
        print(f"❌ Expected TypeError: {e}")
        print("   This shows that device_id is now a required parameter")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def example_error_when_device_id_empty():
    """Example: Show error when device_id is empty."""
    print("\n=== Error Example: Empty Device ID ===")
    
    agent = SynergyPayAgent()
    
    # This will fail because device_id is empty
    result = agent.register_agent("BadAgent", "")  # Empty device_id
    
    if result["status"] == "error":
        print(f"❌ Expected error: {result['message']}")
    else:
        print(f"⏰ Unexpected success: {result}")


def example_send_payment(agent: SynergyPayAgent):
    """Example: Send a Web3 payment."""
    print("\n=== Send Payment Example ===")
    
    # Example recipient address (replace with actual address)
    recipient_address = "0x84D4742e101db6e933127cf56FFb1e4A39B05f82"
    amount_eth = 0.000001  # 0.0001 ETH
    
    print(f"Sending {amount_eth} ETH to {recipient_address}")
    
    result = agent.send_payment(recipient_address, amount_eth)
    
    if result["status"] == "success":
        print(f"✅ Payment sent successfully!")
        print(f"   Transaction Hash: {result['tx_hash']}")
        print(f"   Amount: {result['amount_eth']} ETH")
        print(f"   Payment ID: {result['payment_id']}")
        return result["tx_hash"]
    else:
        print(f"❌ Payment failed: {result['message']}")
        return None


def example_verify_payment(agent: SynergyPayAgent, tx_hash: str):
    """Example: Verify a payment on-chain."""
    print("\n=== Verify Payment Example ===")
    
    if not tx_hash:
        print("❌ No transaction hash to verify")
        return
    
    print(f"Verifying transaction: {tx_hash}")
    
    result = agent.verify_payment(tx_hash, max_retries=3, retry_delay=2)
    
    if result["status"] == "success" and result["verified"]:
        print(f"✅ Payment verified successfully!")
        print(f"   Block Number: {result['block_number']}")
        print(f"   Recipient: {result['recipient']}")
        print(f"   Amount: {result['amount_eth']} ETH")
        print(f"   Sender: {result['sender']}")
        print(f"   Gas Used: {result.get('gas_used', 'N/A')}")
    elif result["status"] == "pending":
        print(f"⏳ Transaction pending - {result['message']}")
        print("   Try again later or use verify_payment_async for better handling")
    else:
        print(f"❌ Payment verification failed: {result['message']}")
        if result.get('transaction_exists') is not None:
            print(f"   Transaction exists: {result['transaction_exists']}")


async def example_verify_payment_async(agent: SynergyPayAgent, tx_hash: str):
    """Example: Verify a payment on-chain using async method."""
    print("\n=== Verify Payment (Async) Example ===")
    
    if not tx_hash:
        print("❌ No transaction hash to verify")
        return
    
    print(f"Verifying transaction async: {tx_hash}")
    
    result = await agent.verify_payment_async(tx_hash, max_retries=5, retry_delay=3)
    
    if result["status"] == "success" and result["verified"]:
        print(f"✅ Payment verified successfully!")
        print(f"   Block Number: {result['block_number']}")
        print(f"   Recipient: {result['recipient']}")
        print(f"   Amount: {result['amount_eth']} ETH")
        print(f"   Sender: {result['sender']}")
        print(f"   Gas Used: {result.get('gas_used', 'N/A')}")
    elif result["status"] == "pending":
        print(f"⏳ Transaction still pending - {result['message']}")
    else:
        print(f"❌ Payment verification failed: {result['message']}")
        if result.get('transaction_exists') is not None:
            print(f"   Transaction exists: {result['transaction_exists']}")


async def main():
    """Run all examples."""
    print("🚀 SynergyPay SDK Examples\n")
     
    print("=== Configuration Method A: Using Environment Variables ===")
    # Setup environment
    setup_environment()
    
    # Example 1: Agent Registration
    agent = example_agent_registration()
    
    print("\n=== Configuration Method B: Using Constructor Parameters ===")
    # Show constructor initialization
    agent_constructor = example_with_constructor()
     
    print("\n=== Running Send Payment Example ===")
    # Example 2: Send Payment
    tx_hash = example_send_payment(agent)
     
    print("\n=== Running Payment Verification Examples ===")
    # Example 3: Verify Payment
    example_verify_payment(agent, tx_hash)
     
    # Example 4: Verify Payment (Async) - if previous verification was pending
    if tx_hash:
        print("\n=== Running Async Verification Example ===")
        await example_verify_payment_async(agent, tx_hash)
     
     
    print("\n✅ All examples completed!")


if __name__ == "__main__":
    asyncio.run(main())
