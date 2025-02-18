import csv
import time
from web3 import Web3
import os

amount: int = int(input("Enter wallet number: "))
private_name = "private_keys"
addresses_name = "addresses"
seed_name = "seeds"

def write_in_file(path: str, data: str):
    with open(path, 'a', encoding="utf-8") as f:
        f.write(f'{data}\n')

web3 = Web3()
web3.eth.account.enable_unaudited_hdwallet_features()

now = time.time()
os.mkdir(f"./wallets/eth/{now}")
with open(f"wallets/eth/new_addresses{now}-{amount}.csv", 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["WALLET", "PRIVATE KEY", "SEED_PHRASE"])
    for index in range(amount):
        account = web3.eth.account.create_with_mnemonic()
        seed_phrase = account[1]
        address = account[0].address
        private_key = account[0].key.hex()

        write_in_file(f"wallets/eth/{now}/{addresses_name}-{now}-{amount}.txt", address)
        write_in_file(f"wallets/eth/{now}/{private_name}-{now}-{amount}.txt", private_key)
        write_in_file(f"wallets/eth/{now}/{seed_name}-{now}-{amount}.txt", seed_phrase)

        # print(f"Address: {address}\nSeed Phrase: {seed_phrase}\nPrivate Key: {private_key}\n")

        csv_writer.writerow([address, private_key, seed_phrase])

