from blockchainConnect import getBalance
from covalent import CovalentClient
from dotenv import load_dotenv
import os

load_dotenv()

COVALENT_KEY = os.getenv("COVALENT_KEY")

chainName = "polygon-amoy-testnet"
walletAddress = "0x850b74A3Cd5edeaD1d09c4ce39356ED681709C1c"

c = CovalentClient(COVALENT_KEY)

coinBalance = c.balance_service.get_token_balances_for_wallet_address(chain_name=chainName,
                                                                    wallet_address=walletAddress)

for token in coinBalance.data.items:
    decimals = token.contract_decimals
    symbol = token.contract_ticker_symbol
    name = token.contract_name
    walletBalance = token.balance // 10 ** decimals
    print(f"{name} ({symbol}): {walletBalance}")
