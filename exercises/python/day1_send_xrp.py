"""
Day 1 Exercise: Send XRP
========================
Send 10 XRP from wallet[0] to wallet[1] on XRPL Testnet.

Reference materials:
- https://learn.xrpl-commons.org/course/blockchain-foundations-for-web2-developers/lesson/create-accounts-and-send-xrp/
- https://xrpl.org/docs/references/protocol/transactions/types/payment
- https://xrpl-py.readthedocs.io/en/stable/
"""

import json
from xrpl.clients import WebsocketClient
from xrpl.wallet import Wallet
from xrpl.models.transactions import Payment
from xrpl.transaction import submit_and_wait
from xrpl.utils import xrp_to_drops
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'scripts'))
from notify_progress import notify_progress

TESTNET_URL = 'wss://s.altnet.rippletest.net:51233'

# Load wallets
with open('../../wallets.json') as f:
    data = json.load(f)
    wallets = data['wallets']

sender = Wallet.from_seed(wallets[0]['seed'])
receiver = Wallet.from_seed(wallets[1]['seed'])

print(f"Sender:   {sender.address}")
print(f"Receiver: {receiver.address}")

with WebsocketClient(TESTNET_URL) as client:

    # ╔══════════════════════════════════════════════════════════════════╗
    # ║ TODO 1: Create a Payment transaction                             ║
    # ║                                                                  ║
    # ║ HINT: Payment(account=sender.address,                            ║
    # ║              amount=xrp_to_drops(10),                            ║
    # ║              destination=receiver.address)                       ║
    # ╚══════════════════════════════════════════════════════════════════╝

    # ╔══════════════════════════════════════════════════════════════════╗
    # ║ TODO 2: Submit the transaction and print the result              ║
    # ║                                                                  ║
    # ║ HINT: result = submit_and_wait(payment_tx, client, sender)       ║
    # ║       print(result)                                              ║
    # ╚══════════════════════════════════════════════════════════════════╝
    pass

# Explorer: https://testnet.xrpl.org/accounts/{address}
print(f"\nCheck sender:   https://testnet.xrpl.org/accounts/{sender.address}")
print(f"Check receiver: https://testnet.xrpl.org/accounts/{receiver.address}")
notify_progress('Day 1: Send XRP')
