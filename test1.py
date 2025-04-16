from blockchainConnect import getBalance

tokens = getBalance("0x850b74A3Cd5edeaD1d09c4ce39356ED681709C1c")

for token in tokens:
    print(token)