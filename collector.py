import json
from web3 import Web3

goerli_url = "https://eth-goerli.alchemyapi.io/v2/PFA1dZBZ9PuLICvNABBhhTi1yxLh2UcJ"
web3 = Web3(Web3.HTTPProvider(goerli_url))

address_1 = "add1"
address_2 = "add2"

private_key = "you key"

nonce = web3.eth.getTransactionCount(address_1)

tx = {
    'nonce': nonce,
    'to': address_2,
    'value': web3.toWei(0.01, 'ether'),
    'gas': 21000,
    'gasPrice': web3.toWei(1.5, 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))
