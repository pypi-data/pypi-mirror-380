"""
SynergyPay SDK - Web3 payment SDK for Synergetics platform.

This package provides functionality for:
- Agent registration with wallet generation
- Web3 payment sending and verification
"""

from .core import SynergyPayAgent

__version__ = "0.1.0"
__all__ = [
    "SynergyPayAgent",
]
