from web3 import Web3
import json


private_keys = [key.strip() for key in open("data/private_keys.txt").readlines()]


web3 = Web3()

data = [
    {
        "address": f"{web3.eth.account.from_key(private_key.strip()).address}",
        "privateKey": f"{private_key}"}
    for private_key in private_keys
]

with open("data/wallets.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)