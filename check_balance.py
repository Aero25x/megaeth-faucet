#!/usr/bin/env python3
import json
import requests
from tqdm import tqdm  # Progress bar import

# Set your RPC endpoint (e.g., Infura, Alchemy, or your own node)
RPC_ENDPOINT = "https://carrot.megaeth.com/rpc"  # <-- Replace with your RPC endpoint

def get_balance(address):
    """
    Fetch the native balance for the given address via JSON-RPC.
    Returns the balance in Ether as a float, or None if fetching fails.
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }
    try:
        response = requests.post(RPC_ENDPOINT, json=payload)
        response.raise_for_status()
        result = response.json().get("result")
        if result:
            # Convert balance from hex (Wei) to Ether
            balance_wei = int(result, 16)
            balance_eth = balance_wei / (10 ** 18)
            return balance_eth
    except Exception as e:
        print(f"Error fetching balance for {address}: {e}")
    return None

def main():
    try:
        with open("wallets.json", "r") as f:
            wallets = json.load(f)
    except Exception as e:
        print(f"Error loading wallets.json: {e}")
        return

    # Create a list to hold wallets with an empty balance.
    empty_wallets = []

    # Process wallets in reverse order with a progress bar
    for wallet in tqdm(wallets[::-1], desc="Processing wallets"):
        address = wallet.get("address")
        private_key = wallet.get("privateKey")
        balance = get_balance(address)

        # Print wallet details to the console
        print(f"\n\n\nAddress: {address}")
        print(f"Balance: {balance} ETH")
        print(f"PrivateKey: {private_key}")
        print("-" * 40)

        # Check if balance is "empty" (None or zero)
        if balance is None or balance == 0:
            empty_wallets.append({
                "address": address,
                "balance": balance if balance is not None else 0,
                "privateKey": private_key
            })

    # Save empty wallets to file "empty.txt"
    if empty_wallets:
        try:
            with open("empty.txt", "w") as f:
                for ew in empty_wallets:
                    f.write(f"{ew.get('address')}\n")
                    # Uncomment the lines below if you wish to add more details
                    # f.write(f"Balance: {ew.get('balance')} ETH\n")
                    # f.write(f"PrivateKey: {ew.get('privateKey')}\n")
                    # f.write("-" * 40 + "\n")
            print(f"\nSaved {len(empty_wallets)} wallet(s) with empty balance to empty.txt.")
        except Exception as e:
            print(f"Error saving empty wallets: {e}")
    else:
        print("\nNo wallets with empty balance were found.")



print("""



  _    _ _     _     _             _____          _
 | |  | (_)   | |   | |           / ____|        | |
 | |__| |_  __| | __| | ___ _ __ | |     ___   __| | ___
 |  __  | |/ _` |/ _` |/ _ \ '_ \| |    / _ \ / _` |/ _ \\
 | |  | | | (_| | (_| |  __/ | | | |___| (_) | (_| |  __/
 |_|  |_|_|\__,_|\__,_|\___|_| |_|\_____\___/ \__,_|\___|

             MegaETH Faucet by Aero25x

            Join us to get more scripts
            https://t.me/hidden_coding


    """)


if __name__ == "__main__":
    main()
