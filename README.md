[![Join our Telegram RU](https://img.shields.io/badge/Telegram-RU-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aero25x)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aero25x)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@flaming_chameleon)
[![Reddit](https://img.shields.io/badge/Reddit-FF3A00?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/HiddenCode/)
[![Join our Telegram ENG](https://img.shields.io/badge/Telegram-EN-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding_en)


# MegaETH Faucet Automation

An automated script designed to simplify claiming tokens from the MegaETH Faucet. This script solves Turnstile captchas using 2Captcha integration, supports proxies (including authenticated proxies), and processes multiple wallet addresses concurrently.

## Features

- **Automated Turnstile Captcha Solving:** Integrates with 2Captcha to automatically solve captchas.
- **Proxy Support:** Works with both non-authenticated (`ip:port`) and authenticated proxies (`ip:port:user:pass`).
- **Multi-threaded Processing:** Processes wallet claims concurrently for improved efficiency.
- **Flexible Wallet Configuration:** Supports wallet addresses from both `wallet.txt` (plain text) and `wallets.json` (JSON format).
- **Comprehensive Logging:** Logs successful claims in `success.txt` and failures in `fail.txt`.

## Installation

### Clone Repository

```bash
git clone https://github.com/Aero25x/megaeth-faucet.git
cd megaeth-faucet
```

### Install Dependencies

```bash
pip install requests colorama twocaptcha pytz tzlocal
pip install 2captcha-python == 1.5.1
```

## Configuration

Before running the script, configure the following files and settings:

### 1. `wallet.txt`
Add your wallet addresses, one per line:

```text
0xYourWalletAddress1
0xYourWalletAddress2
```

### 2. `wallets.json` (Optional)
To load additional wallets from a JSON file, create `wallets.json`:

```json
[
    {"address": "0xYourWalletAddress3"},
    {"address": "0xYourWalletAddress4"}
]
```

Wallet addresses from `wallets.json` will be combined with those in `wallet.txt`.

### 3. `proxy.txt`
List your proxies in one of the following formats:

- **Without Authentication:**

```text
192.168.1.100:8080
```

- **With Authentication:**

```text
31.56.139.207:6276:hxjsvept:3pzgwox5suvu
```

### 4. Script Configuration

Edit the script (e.g., `main.py`) to update your API keys and other settings:

```python
TWO_CAPTCHA_API_KEY = "Your_2Captcha_API_Key"
TURNSTILE_SITEKEY = "Your_Turnstile_Sitekey"
TURNSTILE_PAGE_URL = "https://testnet.megaeth.com/"
```

Adjust additional configuration options such as thread count and API endpoints as needed.

## Running the Script

To start the claim process, run:

```bash
python main.py
```

### Example Run Output

```
Processing wallet: 0xYourWalletAddress1
Attempt 1: Using proxy IP 31.56.139.207
Requesting Turnstile captcha solution from 2Captcha...
Turnstile captcha solved successfully.
Claim response: https://www.megaexplorer.xyz/tx/transaction_hash_here
Claim SUCCESS for wallet 0xYourWalletAddress1
```

## Logs

- **Successful Claims:** Logged in `success.txt`
- **Failed Attempts:** Logged in `fail.txt`

## Contribution

Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

## Disclaimer

Use this script responsibly. The developer is not liable for any misuse or unintended consequences. Always test in a safe environment before deploying in production.

[![Join our Telegram RU](https://img.shields.io/badge/Telegram-RU-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aero25x)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aero25x)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@flaming_chameleon)
[![Reddit](https://img.shields.io/badge/Reddit-FF3A00?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/HiddenCode/)
[![Join our Telegram ENG](https://img.shields.io/badge/Telegram-EN-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding_en)
