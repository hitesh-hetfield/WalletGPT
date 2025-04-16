from web3 import Web3
from covalent import CovalentClient
from dotenv import load_dotenv
import os

load_dotenv()

COVALENT_KEY = os.getenv("COVALENT_KEY")
CHAIN_NAME = "polygon-amoy-testnet"

# RPC_URL = "https://rpc.testnet.5ire.network"
RPC_URL = "https://rpc-amoy.polygon.technology/"

c = CovalentClient(COVALENT_KEY)
web3 = Web3(Web3.HTTPProvider(RPC_URL))

def isConnected():
    return web3.is_connected()

def validAddress(address: str):
    return web3.is_address(address)

# Native balance
def getBalance(address: str):
    if not web3.is_address(address):
        raise ValueError("Invalid Address")

    balance_list = []

    # fetching token balance 
    tokenBalance = c.balance_service.get_token_balances_for_wallet_address(chain_name=CHAIN_NAME,
                                                                           wallet_address=address)

    for tokens in tokenBalance.data.items:
        symbol = tokens.contract_ticker_symbol
        decimals = tokens.contract_decimals
        name = tokens.contract_name
        balance = tokens.balance // 10 ** decimals

        balance_list.append(f"{name} ({symbol}): {balance}")

    return balance_list