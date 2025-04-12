[![Join our Telegram RU](https://img.shields.io/badge/Telegram-RU-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aero25x)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aero25x)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@flaming_chameleon)
[![Reddit](https://img.shields.io/badge/Reddit-FF3A00?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/HiddenCode/)
[![Join our Telegram ENG](https://img.shields.io/badge/Telegram-EN-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding_en)






# MegaETH Faucet Automation

An automated script designed to claim tokens from the [MegaETH Faucet](https://github.com/Aero25x/megaeth-faucet). This repository harnesses the power of automation, multi-threading, and 2Captcha integration to streamline the token claim process on **MegaETH**, a high-performance, Layer 2 blockchain for Ethereum.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
  - [Wallet Configuration](#wallet-configuration)
  - [Proxy Configuration](#proxy-configuration)
  - [Script Settings](#script-settings)
- [Usage](#usage)
- [Logging](#logging)
- [About MegaETH](#about-megaeth)
- [Contribution](#contribution)
- [License](#license)

## Project Overview

This repository offers an **automated solution** specifically crafted for the MegaETH network. MegaETH is a Layer 2 blockchain solution designed to enhance the scalability of Ethereum by enabling real-time transaction processing. Our script targets the MegaETH Faucet, facilitating **fast and reliable token distribution** through automated processes that handle Turnstile captchas, proxy configurations, and multi-threaded wallet claims. 

## Features

- **Automated Turnstile Captcha Solving:** Seamlessly integrates with [2Captcha](https://2captcha.com/) to solve captchas automatically.
- **Proxy Support:** Compatible with both non-authenticated (`ip:port`) and authenticated proxies (`ip:port:user:pass`).
- **Multi-threaded Processing:** Handles wallet claims concurrently to maximize efficiency and throughput.
- **Flexible Wallet Configuration:** Supports wallet addresses from both `wallet.txt` (plain text) and `wallets.json` (JSON format).
- **Enhanced Logging:** Captures detailed logs with successes in `success.txt` and failures in `fail.txt`.

## Installation

### Clone the Repository

Clone the repository from GitHub to start using the automation tool:

```bash
git clone https://github.com/Aero25x/megaeth-faucet.git
cd megaeth-faucet
```

### Install Dependencies

Install all necessary dependencies with pip:

```bash
pip install requests colorama twocaptcha pytz tzlocal
pip install 2captcha-python==1.5.1
```

*Note: Verify package versions and update if necessary.*

## Configuration

Before running the script, update the configurations to match your environment and MegaETH network settings.

### Wallet Configuration

#### `wallet.txt`

Add your MegaETH wallet addresses—one per line:

```text
0xYourWalletAddress1
0xYourWalletAddress2
```

#### `wallets.json` (Optional)

Load additional wallet addresses using JSON format:

```json
[
    {"address": "0xYourWalletAddress3"},
    {"address": "0xYourWalletAddress4"}
]
```

Wallet addresses from `wallets.json` are combined with those in `wallet.txt`.

### Proxy Configuration

#### `proxy.txt`

List your proxies in one of the following formats:

- **Without Authentication:**

  ```text
  192.168.1.100:8080
  ```

- **With Authentication:**

  ```text
  31.56.139.207:6276:hxjsvept:3pzgwox5suvu
  ```

### Script Settings

Edit the script (e.g., `main.py`) and update your API keys along with MegaETH configuration details:

```python
TWO_CAPTCHA_API_KEY = "Your_2Captcha_API_Key"
TURNSTILE_SITEKEY = "Your_Turnstile_Sitekey"
TURNSTILE_PAGE_URL = "https://testnet.megaeth.com/"
```

You can further adjust thread counts, endpoints, and other settings as needed.

## Usage

Execute the script to initiate the token claim process on the MegaETH Faucet:

```bash
python faucet.py
```

### Example Output

```
Processing wallet: 0xYourWalletAddress1
Attempt 1: Using proxy IP 31.56.139.207
Requesting Turnstile captcha solution from 2Captcha...
Turnstile captcha solved successfully.
Claim response: https://www.megaexplorer.xyz/tx/transaction_hash_here
Claim SUCCESS for wallet 0xYourWalletAddress1
```

## Logging

- **Successful Claims:** All successful transactions are recorded in `success.txt`.
- **Failed Attempts:** Any errors or failed transactions are recorded in `fail.txt`.

## About MegaETH

[MegaETH](https://megaeth.org/) is a state-of-the-art, Layer 2 blockchain network designed to supercharge Ethereum by providing high scalability and low-latency transactions. Key points include:

- **High Throughput:** Capable of processing over 100,000 transactions per second (TPS).
- **Modular Architecture:** Utilizes specialized nodes such as sequencers, provers, and full nodes to optimize transaction ordering and execution.
- **EVM Compatibility:** Fully compatible with the Ethereum Virtual Machine, ensuring seamless integration with existing Ethereum infrastructure.

This automation script is built for users who want to leverage the fast-paced transactions on the MegaETH network for automated token claims.

## Contribution

Contributions are highly encouraged! If you have improvements, feature suggestions, or bug fixes, please open an issue or submit a pull request. Your contributions help make the MegaETH ecosystem even stronger.

## License

This project is open source and available under the [MIT License](LICENSE).




## Disclaimer

Use this script responsibly. The developer is not liable for any misuse or unintended consequences. Always test in a safe environment before deploying in production.

[![Join our Telegram RU](https://img.shields.io/badge/Telegram-RU-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aero25x)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aero25x)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@flaming_chameleon)
[![Reddit](https://img.shields.io/badge/Reddit-FF3A00?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/HiddenCode/)
[![Join our Telegram ENG](https://img.shields.io/badge/Telegram-EN-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding_en)
