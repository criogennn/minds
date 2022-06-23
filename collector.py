import json
from web3 import Web3

goerli_url = "https://eth-goerli.alchemyapi.io/v2/PFA1dZBZ9PuLICvNABBhhTi1yxLh2UcJ"
web3 = Web3(Web3.HTTPProvider(goerli_url))

address_1 = "0x2ad3E7145f7c4a62078052c4358d8671C8ddCA31"
address_2 = "0x21e2663D0DB4b3EB1E6da33b45efF20608972d49"

private_key = "a2c48afa28ca3e968430b7a82e448a58366fd999ff0b009c7bd97106bcfffeb3"

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