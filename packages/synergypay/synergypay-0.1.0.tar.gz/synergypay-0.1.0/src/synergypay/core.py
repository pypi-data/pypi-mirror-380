"""
Core SynergyPay agent functionality.

This module provides the main SynergyPayAgent class with methods for:
- Agent registration with wallet generation
- Web3 payment sending and verification
- Agent-to-agent communication
"""

import os
import json
import uuid
import asyncio
import time
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
from dotenv import load_dotenv
from web3 import Web3
from eth_account import Account
import requests
import httpx


class SynergyPayAgent:
    """
    Main agent class for SynergyPay functionality.
    
    Provides methods for agent registration, payment sending, and verification.
    """
    
    def __init__(self, config_path: Optional[str] = None, 
                 web3_rpc_url: Optional[str] = None,
                 chain_id: Optional[int] = None,
                 token_address: Optional[str] = None,
                 service_price_wei: Optional[int] = None,
                 owner_pub_key: Optional[str] = None):
        """
        Initialize the SynergyPay agent.
        
        Args:
            config_path: Optional path to configuration directory. 
                        Defaults to current working directory.
            web3_rpc_url: Web3 RPC endpoint URL (overrides env var)
            chain_id: Blockchain chain ID (overrides env var)
            token_address: Token contract address (overrides env var)
            service_price_wei: Default service price in wei (overrides env var)
            owner_pub_key: Owner's public key (overrides env var)
        """
        self.config_path = Path(config_path) if config_path else Path.cwd()
        self.env_file = self.config_path / ".env"
        
        # Load environment variables (if .env file exists)
        if self.env_file.exists():
            load_dotenv(self.env_file)
        
        # Configuration with constructor parameters taking precedence
        self.web3_rpc_url = web3_rpc_url or os.getenv("WEB3_RPC_URL")
        if not self.web3_rpc_url:
            raise ValueError("web3_rpc_url is required. Provide via constructor or WEB3_RPC_URL env var.")
        
        # Initialize Web3 connection
        self.w3 = Web3(Web3.HTTPProvider(self.web3_rpc_url))
        
        # Configuration with defaults
        self.chain_id = chain_id or int(os.getenv("CHAIN_ID", "1"))
        self.token_address = token_address or os.getenv("TOKEN_ADDRESS", "")
        self.service_price_wei = service_price_wei or int(os.getenv("SERVICE_PRICE_WEI", "1000000000000000000"))  # 1 ETH
        self.owner_pub_key = owner_pub_key or os.getenv("OWNER_PUB_KEY")
        
        # Agent state
        self.account: Optional[Account] = None
        self.address: Optional[str] = None
        self.device_id: Optional[str] = None
        
        # Wallet file path
        self.wallet_file = self.config_path / "wallet.json"
    
    def register_agent(self, agent_name: str, device_id: str, owner_pub_key: Optional[str] = None, 
                      bot_metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Register agent with wallet generation and Synergetics API registration.
        
        Args:
            agent_name: Name of the agent (e.g., "Agent_A", "Agent_B")
            device_id: Required device ID for the agent
            owner_pub_key: Owner's public key. If None, reads from OWNER_PUB_KEY env var.
            bot_metadata: Custom bot metadata dictionary. If None, uses empty dict.
            
        Returns:
            Dict containing registration status and agent details
            
        Raises:
            ValueError: If device_id is not provided or empty
        """
        try:
            # Validate required device_id parameter
            if not device_id or not isinstance(device_id, str) or not device_id.strip():
                raise ValueError("device_id is required and must be a non-empty string")
            
            # Generate or load wallet with required device_id
            self._create_or_load_wallet(agent_name, custom_device_id=device_id)
            
            # Get owner public key
            if not owner_pub_key:
                owner_pub_key = self.owner_pub_key
                if not owner_pub_key:
                    raise ValueError("owner_pub_key is required. Provide via constructor, method parameter, or OWNER_PUB_KEY env var.")
            
            # Register with Synergetics API using custom metadata
            registration_success = self._register_with_api(agent_name, owner_pub_key, bot_metadata)
            
            return {
                "status": "success" if registration_success else "partial",
                "agent_name": agent_name,
                "address": self.address,
                "device_id": self.device_id,
                "bot_metadata": bot_metadata or {},
                "api_registration": registration_success,
                "message": "Agent registered successfully" if registration_success else "Wallet created but API registration failed"
            }
            
        except Exception as e:
            return {
                "status": "error",
                "agent_name": agent_name,
                "error": str(e),
                "message": f"Agent registration failed: {e}"
            }
    
    def send_payment(self, recipient_address: str, amount_eth: Optional[float] = None) -> Dict[str, Any]:
        """
        Send Web3 payment to recipient address.
        
        Args:
            recipient_address: Ethereum address to send payment to
            amount_eth: Amount in ETH (e.g., 0.001). If None, uses SERVICE_PRICE_WEI from config.
            
        Returns:
            Dict containing payment status and transaction details
        """
        if not self.account:
            raise ValueError("Agent not registered. Call register_agent() first.")
        
        # Convert ETH to wei or use default from config
        if amount_eth is not None:
            amount_wei = int(self.w3.to_wei(amount_eth, 'ether'))
        else:
            # Convert config wei to ETH for default amount
            amount_wei = self.service_price_wei
            amount_eth = self.w3.from_wei(amount_wei, 'ether')
        
        try:
            # Check balance
            balance = self.w3.eth.get_balance(self.address)
            if balance < amount_wei:
                raise ValueError(f"Insufficient balance. Need {self.w3.from_wei(amount_wei, 'ether'):.4f} ETH")
            
            # Create transaction
            nonce = self.w3.eth.get_transaction_count(self.address)
            
            transaction = {
                "to": recipient_address,
                "value": amount_wei,
                "gas": 21000,
                "gasPrice": self.w3.eth.gas_price,
                "nonce": nonce,
                "chainId": self.chain_id,
            }
            
            # Sign and send transaction
            signed_txn = self.w3.eth.account.sign_transaction(transaction, self.account.key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
            tx_hash_hex = tx_hash.hex()
            
            # Generate payment ID
            payment_id = str(uuid.uuid4())
            
            return {
                "status": "success",
                "tx_hash": tx_hash_hex,
                "amount_wei": amount_wei,
                "amount_eth": float(amount_eth),
                "recipient": recipient_address,
                "sender": self.address,
                "payment_id": payment_id,
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "message": f"Payment failed: {e}"
            }
    
    def verify_payment(self, tx_hash: str, expected_recipient: Optional[str] = None, 
                      expected_amount_eth: Optional[float] = None, max_retries: int = 5, 
                      retry_delay: int = 3) -> Dict[str, Any]:
        """
        Verify a Web3 payment transaction on-chain.
        
        Args:
            tx_hash: Transaction hash to verify
            expected_recipient: Expected recipient address (optional)
            expected_amount_eth: Expected amount in ETH (optional, e.g., 0.001)
            max_retries: Maximum number of retries for transaction mining
            retry_delay: Delay between retries in seconds
            
        Returns:
            Dict containing verification status and transaction details
        """        
        try:
            # Wait for transaction to be mined with retries
            tx_receipt = None
            for attempt in range(max_retries):
                try:
                    tx_receipt = self.w3.eth.get_transaction_receipt(tx_hash)
                    break  # Transaction found and mined
                except Exception:
                    if attempt < max_retries - 1:
                        print(f"⏳ Transaction not mined yet, waiting {retry_delay}s... (attempt {attempt + 1}/{max_retries})")
                        time.sleep(retry_delay)
                    else:
                        # Check if transaction exists but not mined yet
                        try:
                            tx = self.w3.eth.get_transaction(tx_hash)
                            return {
                                "status": "pending",
                                "tx_hash": tx_hash,
                                "verified": False,
                                "message": "Transaction found but not yet mined",
                                "transaction_exists": True
                            }
                        except Exception:
                            return {
                                "status": "error",
                                "tx_hash": tx_hash,
                                "verified": False,
                                "message": "Transaction not found or not mined after maximum retries",
                                "transaction_exists": False
                            }
            
            if not tx_receipt:
                return {
                    "status": "error",
                    "tx_hash": tx_hash,
                    "verified": False,
                    "message": "Could not get transaction receipt"
                }
            
            # Check if transaction was successful
            if tx_receipt.status != 1:
                return {
                    "status": "error",
                    "tx_hash": tx_hash,
                    "verified": False,
                    "message": "Transaction failed",
                    "block_number": tx_receipt.blockNumber
                }
            
            # Get transaction details
            tx = self.w3.eth.get_transaction(tx_hash)
            
            # Verify recipient if provided
            if expected_recipient and tx['to'] and tx['to'].lower() != expected_recipient.lower():
                return {
                    "status": "error",
                    "tx_hash": tx_hash,
                    "verified": False,
                    "message": f"Recipient mismatch. Expected: {expected_recipient}, Got: {tx['to']}",
                    "expected_recipient": expected_recipient,
                    "actual_recipient": tx['to']
                }
            
            # Verify amount if provided - expected_amount_eth is converted to wei and compared
            if expected_amount_eth is not None:
                expected_amount_wei = int(self.w3.to_wei(expected_amount_eth, 'ether'))
                if tx['value'] != expected_amount_wei:
                    return {
                    "status": "error",
                    "tx_hash": tx_hash,
                    "verified": False,
                    "message": f"Amount mismatch. Expected: {expected_amount_eth} ETH ({expected_amount_wei} wei), Got: {tx['value']} wei",
                    "expected_amount_eth": expected_amount_eth,
                    "expected_amount_wei": expected_amount_wei,
                    "actual_amount_wei": tx['value'],
                    "actual_amount_eth": self.w3.from_wei(tx['value'], 'ether')
                    }
            
            return {
                "status": "success",
                "tx_hash": tx_hash,
                "verified": True,
                "block_number": tx_receipt.blockNumber,
                "recipient": tx['to'],
                "amount_wei": tx['value'],
                "amount_eth": float(self.w3.from_wei(tx['value'], 'ether')),
                "sender": tx['from'],
                "gas_used": tx_receipt.gasUsed,
                "transaction_index": tx_receipt.transactionIndex
            }
            
        except Exception as e:
            return {
                "status": "error",
                "tx_hash": tx_hash,
                "verified": False,
                "message": f"Verification failed: {e}",
                "error_type": type(e).__name__
            }
    
    async def verify_payment_async(self, tx_hash: str, expected_recipient: Optional[str] = None, 
                                 expected_amount_eth: Optional[float] = None, max_retries: int = 5, 
                                 retry_delay: int = 3) -> Dict[str, Any]:
        """
        Async version of verify_payment with better waiting handling.
        
        Args:
            tx_hash: Transaction hash to verify
            expected_recipient: Expected recipient address (optional)
            expected_amount_eth: Expected amount in ETH (optional, e.g., 0.001)
            max_retries: Maximum number of retries for transaction mining
            retry_delay: Delay between retries in seconds
            
        Returns:
            Dict containing verification status and transaction details
        """
        try:
            # Wait for transaction to be mined with retries
            tx_receipt = None
            for attempt in range(max_retries):
                try:
                    tx_receipt = self.w3.eth.get_transaction_receipt(tx_hash)
                    break  # Transaction found and mined
                except Exception:
                    if attempt < max_retries - 1:
                        print(f"⏳ Transaction not mined yet, waiting {retry_delay}s... (attempt {attempt + 1}/{max_retries})")
                        await asyncio.sleep(retry_delay)
                    else:
                        # Check if transaction exists but not mined yet
                        try:
                            tx = self.w3.eth.get_transaction(tx_hash)
                            return {
                                "status": "pending",
                                "tx_hash": tx_hash,
                                "verified": False,
                                "message": "Transaction found but not yet mined",
                                "transaction_exists": True
                            }
                        except Exception:
                            return {
                                "status": "error",
                                "tx_hash": tx_hash,
                                "verified": False,
                                "message": "Transaction not found or not mined after maximum retries",
                                "transaction_exists": False
                            }
            
            if not tx_receipt:
                return {
                    "status": "error",
                    "tx_hash": tx_hash,
                    "verified": False,
                    "message": "Could not get transaction receipt"
                }
            
            # Check if transaction was successful
            if tx_receipt.status != 1:
                return {
                    "status": "error",
                    "tx_hash": tx_hash,
                    "verified": False,
                    "message": "Transaction failed",
                    "block_number": tx_receipt.blockNumber
                }
            
            # Get transaction details
            tx = self.w3.eth.get_transaction(tx_hash)
            
            # Verify recipient if provided
            if expected_recipient and tx['to'] and tx['to'].lower() != expected_recipient.lower():
                return {
                    "status": "error",
                    "tx_hash": tx_hash,
                    "verified": False,
                    "message": f"Recipient mismatch. Expected: {expected_recipient}, Got: {tx['to']}",
                    "expected_recipient": expected_recipient,
                    "actual_recipient": tx['to']
                }
            
            # Verify amount if provided - expected_amount_eth is converted to wei and compared
            if expected_amount_eth is not None:
                expected_amount_wei = int(self.w3.to_wei(expected_amount_eth, 'ether'))
                if tx['value'] != expected_amount_wei:
                    return {
                    "status": "error",
                    "tx_hash": tx_hash,
                    "verified": False,
                    "message": f"Amount mismatch. Expected: {expected_amount_eth} ETH ({expected_amount_wei} wei), Got: {tx['value']} wei",
                    "expected_amount_eth": expected_amount_eth,
                    "expected_amount_wei": expected_amount_wei,
                    "actual_amount_wei": tx['value'],
                    "actual_amount_eth": self.w3.from_wei(tx['value'], 'ether')
                    }
            
            return {
                "status": "success",
                "tx_hash": tx_hash,
                "verified": True,
                "block_number": tx_receipt.blockNumber,
                "recipient": tx['to'],
                "amount_wei": tx['value'],
                "amount_eth": float(self.w3.from_wei(tx['value'], 'ether')),
                "sender": tx['from'],
                "gas_used": tx_receipt.gasUsed,
                "transaction_index": tx_receipt.transactionIndex
            }
            
        except Exception as e:
            return {
                "status": "error",
                "tx_hash": tx_hash,
                "verified": False,
                "message": f"Verification failed: {e}",
                "error_type": type(e).__name__
            }
    
    
    
    def _create_or_load_wallet(self, agent_name: str, custom_device_id: str) -> None:
        """Create or load wallet for the agent with required device_id."""
        if self.wallet_file.exists():
            # Load existing wallet
            with open(self.wallet_file, "r") as f:
                wallet_data = json.load(f)
                self.account = Account.from_key(wallet_data["private_key"])
                self.address = wallet_data["address"]
                # Always update with the provided device_id
                self.device_id = custom_device_id
                wallet_data["DEVICE_ID"] = self.device_id
                wallet_data["DEVICE_TYPE"] = agent_name
                with open(self.wallet_file, "w") as f:
                    json.dump(wallet_data, f, indent=2)
        else:
            # Create new wallet
            self.account = Account.create()
            self.address = self.account.address
            self.device_id = custom_device_id
            
            wallet_data = {
                "private_key": self.account.key.hex(),
                "address": self.address,
                "DEVICE_TYPE": agent_name,
                "DEVICE_ID": self.device_id,
            } 
            
            with open(self.wallet_file, "w") as f:
                json.dump(wallet_data, f, indent=2)
        
        # Update .env file
        self._update_env_file("AGENT_ADDRESS", self.address)
        self._update_env_file("AGENT_PRIVATE_KEY", self.account.key.hex())
    
    def _register_with_api(self, agent_name: str, owner_pub_key: str, bot_metadata: Optional[Dict[str, Any]] = None) -> bool:
        """Register agent with Synergetics API."""
        data = {
            "deviceID": self.device_id,
            "deviceType": agent_name,
            "botMetadata": bot_metadata or {},
            "botExecutorWallet": self.address,
            "publickey": owner_pub_key,
        }
        
        headers = {"Content-Type": "application/json"}
        url = "https://api.synergetics.ai/transformer-bots/v1/bot/register"
        
        try:
            response = requests.post(url, json=data, headers=headers)
            return response.status_code in [200, 201, 400]  # 400 means already registered
        except Exception:
            return False
    
    def _update_env_file(self, key: str, value: str) -> None:
        """Update or add a key-value pair to the .env file."""
        env_lines = []
        if self.env_file.exists():
            with open(self.env_file, "r") as f:
                env_lines = f.readlines()
        
        # Update or add the key-value pair
        key_found = False
        for i, line in enumerate(env_lines):
            if line.startswith(f"{key}="):
                env_lines[i] = f"{key}={value}\n"
                key_found = True
                break
        
        # If key not found, add it
        if not key_found:
            env_lines.append(f"{key}={value}\n")
        
        # Write back to .env file
        with open(self.env_file, "w") as f:
            f.writelines(env_lines)
