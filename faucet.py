#!/usr/bin/env python3

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


# ================== IMPORTS ==================
import json
import time
import requests
from twocaptcha import TwoCaptcha
from colorama import init, Fore
from datetime import datetime
import threading
from tzlocal import get_localzone
from concurrent.futures import ThreadPoolExecutor, as_completed

# ================== INITIALIZATION ==================
init(autoreset=True)

# ================== CONFIGURATION ==================
THREADS = 5                                  # Number of threads to use
TWO_CAPTCHA_API_KEY = ""  # 2Captcha API key

TURNSTILE_SITEKEY = "0x4AAAAAABA4JXCaw9E2Py-9"  # Turnstile site key
TURNSTILE_PAGE_URL = "https://testnet.megaeth.com/"  # Turnstile page URL
MEGAETH_API_URL = "https://carrot.megaeth.com/claim"  # Megaeth claim endpoint

WALLETS_FILE = "wallet.txt"      # Primary wallets file
WALLETS_JSON_FILE = "wallets.json" # Secondary wallets file (JSON format)
PROXIES_FILE = "proxy.txt"        # Proxies file

SUCCESS_FILE = "success.txt"      # File to log successful claims
FAIL_FILE = "fail.txt"            # File to log failed claims

HEADERS = {
    "Accept": "*/*",
    "Content-Type": "text/plain;charset=UTF-8",
    "Origin": "https://testnet.megaeth.com",
    "Referer": "https://testnet.megaeth.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

# ================== UTILITY FUNCTIONS ==================
def read_lines(filepath):
    """Read non-empty lines from a file."""
    try:
        with open(filepath, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(Fore.RED + f"Error reading {filepath}: {e}")
        return []

def read_wallets():
    """
    Read wallet addresses from both wallet.txt and wallets.json files.
    Returns a combined list of wallet addresses.
    """
    wallets = read_lines(WALLETS_FILE)
    try:
        with open(WALLETS_JSON_FILE, "r") as f:
            wallets_json = json.load(f)
            wallets += [entry['address'] for entry in wallets_json if 'address' in entry]
    except Exception as e:
        print(Fore.YELLOW + f"Warning: {WALLETS_JSON_FILE} not found or error reading it: {e}")
    return wallets

# ================== PROXY MANAGEMENT ==================
proxies_list = read_lines(PROXIES_FILE)
proxy_index = 0
PROXY_LOCK = threading.Lock()

def format_proxy(proxy_str):
    """
    Convert a proxy string in the format "ip:port:user:pass" or "ip:port"
    into a dictionary suitable for the requests module.
    """
    parts = proxy_str.split(':')
    if len(parts) == 4:
        ip, port, user, passwd = parts
        formatted = f"http://{user}:{passwd}@{ip}:{port}"
        return {'http': formatted, 'https': formatted}
    elif len(parts) == 2:
        ip, port = parts
        formatted = f"http://{ip}:{port}"
        return {'http': formatted, 'https': formatted}
    else:
        raise ValueError(f"Invalid proxy format: {proxy_str}")

def get_next_proxy():
    """Cycle through the proxies list in a thread-safe manner."""
    global proxy_index
    with PROXY_LOCK:
        if not proxies_list:
            return None
        proxy = proxies_list[proxy_index % len(proxies_list)]
        proxy_index += 1
        return proxy

def get_current_ip(proxy_str):
    """Get current IP address using the provided proxy string."""
    try:
        proxy_dict = format_proxy(proxy_str)
    except ValueError as e:
        print(Fore.RED + f"Proxy formatting error: {e}")
        return "Invalid Proxy"
    try:
        r = requests.get("https://api.myip.com", proxies=proxy_dict, timeout=30)
        if r.status_code == 200:
            return r.json().get("ip", "Unknown IP")
    except Exception as e:
        print(Fore.RED + f"Error getting IP with proxy {proxy_str}: {e}")
    return "Unknown IP"

# ================== CAPTCHA SOLVER ==================
def solve_turnstile():
    """
    Solve the Turnstile captcha using 2Captcha.
    Returns the captcha token if successful.
    """
    try:
        solver = TwoCaptcha(TWO_CAPTCHA_API_KEY)
        print(Fore.YELLOW + "Requesting Turnstile captcha solution from 2Captcha...")
        result = solver.turnstile(sitekey=TURNSTILE_SITEKEY, url=TURNSTILE_PAGE_URL)
        token = result.get("code")
        if token:
            print(Fore.GREEN + "Turnstile captcha solved successfully.")
            return token
        else:
            print(Fore.RED + f"Invalid response from captcha solver: {result}")
    except Exception as e:
        print(Fore.RED + f"Turnstile captcha solve error: {e}")
    return None

# ================== CLAIM FUNCTION ==================
def megaeth_claim(wallet, token, proxy_str):
    """
    Send a claim request to the Megaeth faucet.
    Returns the response JSON.
    """
    try:
        proxy_dict = format_proxy(proxy_str)
    except ValueError as e:
        print(Fore.RED + f"Proxy formatting error: {e}")
        return None
    try:
        response = requests.post(
            MEGAETH_API_URL,
            json={"addr": wallet, "token": token},
            headers=HEADERS,
            proxies=proxy_dict,
            timeout=60
        )
        return response.json()
    except Exception as e:
        print(Fore.RED + f"Claim API error for {wallet}: {e}")
    return None

# ================== WALLET PROCESSING ==================
def process_wallet(wallet, stop_event):
    """
    Process a single wallet:
    - Cycle through proxies.
    - Solve the captcha.
    - Attempt to claim the faucet (retry up to 3 times).
    Logs success or failure.
    """
    print(Fore.CYAN + f"Processing wallet: {wallet}")
    max_retries = 3
    attempts = 0
    success_flag = False

    while attempts < max_retries and not success_flag:
        if stop_event.is_set():
            print(Fore.CYAN + "Stop event detected. Exiting thread.")
            return

        proxy_str = get_next_proxy()
        ip = get_current_ip(proxy_str)
        print(Fore.YELLOW + f"Attempt {attempts + 1}: Using proxy IP {ip}")

        captcha_token = solve_turnstile()
        if not captcha_token:
            print(Fore.RED + "Captcha solving failed. Retrying...")
            attempts += 1
            continue

        resp = megaeth_claim(wallet, captcha_token, proxy_str)
        if resp:
            tx_hash = resp.get("txhash", "")
            print(Fore.CYAN + f"Claim response: https://www.megaexplorer.xyz/tx/{tx_hash}")
            message = resp.get("message", "").lower()
            if "less than" in message and "hours have passed since the last claim" in message:
                print(Fore.YELLOW + f"Wallet {wallet} has claimed recently. Skipping further attempts.")
                return
            if resp.get("success", False) and tx_hash:
                success_flag = True
            else:
                print(Fore.RED + "Claim not successful, retrying...")
        else:
            print(Fore.RED + "No response from claim API, retrying...")

        attempts += 1

    if success_flag:
        print(Fore.GREEN + f"Claim SUCCESS for wallet {wallet}")
        with open(SUCCESS_FILE, "a") as f:
            f.write(wallet + "\n")
    else:
        print(Fore.RED + f"Claim FAILED after {max_retries} attempts for wallet {wallet}")
        with open(FAIL_FILE, "a") as f:
            f.write(wallet + "\n")

# ================== MAIN PROCESS ==================
def main_process(stop_event):
    """Main function to process all wallets using multi-threading."""
    print(Fore.CYAN + "Starting Megaeth Faucet Claim Process...")
    wallets = read_wallets()
    if not wallets:
        print(Fore.RED + "No wallets found. Exiting.")
        return

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = {executor.submit(process_wallet, wallet, stop_event): wallet for wallet in wallets}
        try:
            for future in as_completed(futures):
                future.result()
        except KeyboardInterrupt:
            print(Fore.CYAN + "KeyboardInterrupt detected. Stopping all threads...")
            stop_event.set()
            for future in futures:
                future.cancel()
            raise

if __name__ == "__main__":
    stop_event = threading.Event()
    try:
        main_process(stop_event)
    except KeyboardInterrupt:
        print(Fore.CYAN + "User interrupted the process. Exiting...")
