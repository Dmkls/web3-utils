import csv
import time
from web3 import Web3

amount: int = int(input("Enter wallet number: "))

web3 = Web3()
web3.eth.account.enable_unaudited_hdwallet_features()


with open(f"wallets/eth/new_addresses{time.time()}-{amount}.csv", 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["WALLET", "PRIVATE KEY", "SEED_PHRASE"])
    for index in range(amount):
        account = web3.eth.account.create_with_mnemonic()
        seed_phrase = account[1]
        address = account[0].address
        private_key = account[0].key.hex()

        # print(f"Address: {address}\nSeed Phrase: {seed_phrase}\nPrivate Key: {private_key}\n")

        csv_writer.writerow([address, private_key, seed_phrase])

