[![Join our Telegram RU](https://img.shields.io/badge/Telegram-RU-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aero25x)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aero25x)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@flaming_chameleon)
[![Reddit](https://img.shields.io/badge/Reddit-FF3A00?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/HiddenCode/)
[![Join our Telegram ENG](https://img.shields.io/badge/Telegram-EN-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding_en)





# Monad Faucet Automation

An automated solution for claiming tokens from the Monad Faucet. Designed specifically for the innovative Monad network—a Layer 1 blockchain and EVM-compatible platform—the script simplifies the token claim process by automating captcha solving, proxy management, and multi-wallet handling.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
  - [Wallet Configuration](#wallet-configuration)
  - [Proxy Setup](#proxy-setup)
  - [Script Settings](#script-settings)
- [Usage](#usage)
- [Logs](#logs)
- [About Monad](#about-monad)
- [Contribution](#contribution)
- [License](#license)

## Project Overview

**Monad Faucet Automation** is a tool designed for users looking to claim tokens from the Monad Faucet effortlessly. Built with advanced automation techniques, this script leverages automated captcha solutions, proxy support, and multi-threaded processing to ensure that every claim is handled quickly and efficiently on Monad’s cutting-edge Layer 1 blockchain.

Monad is known for its innovative parallel transaction processing, which enhances the overall Ethereum ecosystem by providing a more scalable and efficient network. This faucet automation tool is tailored to help users engage with the Monad network by streamlining token distribution from the faucet.

## Features

- **Automated Captcha Solving:** Integrates with captcha-solving services (e.g., 2Captcha) to bypass Turnstile challenges automatically.
- **Proxy Support:** Works seamlessly with both non-authenticated (`ip:port`) and authenticated proxies (`ip:port:user:pass`) for added security and reliability.
- **Multi-threaded Wallet Claims:** Processes multiple wallet addresses concurrently to maximize efficiency.
- **Flexible Wallet Input:** Supports wallet addresses through plain text (`wallet.txt`) or JSON files (`wallets.json`).
- **Detailed Logging:** Tracks successful token claims in `success.txt` and logs any failures in `fail.txt` for easy troubleshooting.

## Installation

### Clone the Repository

Clone the repository from GitHub to begin using the Monad Faucet Automation tool:

```bash
git clone https://github.com/Aero25x/megaeth-faucet.git
cd monad-faucet
```

### Install Dependencies

Install the required dependencies using pip:

```bash
pip install requests colorama twocaptcha pytz tzlocal
pip install 2captcha-python==1.5.1
```

*Ensure you have Python 3.x installed in your environment.*

## Configuration

Before executing the script, you need to update your configuration files and script settings accordingly.

### Wallet Configuration

#### `wallet.txt`

List your Monad wallet addresses, one address per line:

```text
0xYourMonadWalletAddress1
0xYourMonadWalletAddress2
```

#### `wallets.json` (Optional)

You can also include wallet addresses using a JSON file:

```json
[
    {"address": "0xYourMonadWalletAddress3"},
    {"address": "0xYourMonadWalletAddress4"}
]
```

Wallet addresses from both sources will be combined for processing.

### Proxy Setup

#### `proxy.txt`

Provide your proxy details in one of the following formats:

- **Without Authentication:**

  ```text
  192.168.1.100:8080
  ```

- **With Authentication:**

  ```text
  31.56.139.207:6276:hxjsvept:3pzgwox5suvu
  ```

### Script Settings

Open the main script file (e.g., `main.py`) and update the following parameters with your credentials and settings:

```python
TWO_CAPTCHA_API_KEY = "Your_2Captcha_API_Key"
TURNSTILE_SITEKEY = "Your_Turnstile_Sitekey"
TURNSTILE_PAGE_URL = "https://faucet.monad.network/"
```

Adjust additional options such as thread count and API endpoints as per your requirements.

## Usage

Run the script to start claiming tokens from the Monad Faucet:

```bash
python main.py
```

### Example Output

```
Processing wallet: 0xYourMonadWalletAddress1
Attempt 1: Using proxy IP 31.56.139.207
Requesting captcha solution from 2Captcha...
Captcha solved successfully.
Claim response: https://explorer.monad.network/tx/transaction_hash_here
Claim SUCCESS for wallet 0xYourMonadWalletAddress1
```

## Logs

- **Successful Claims:** Stored in `success.txt`
- **Failed Claims:** Recorded in `fail.txt`

## About Monad

Monad is an EVM-compatible Layer 1 blockchain designed to enhance Ethereum's scalability. By enabling parallel execution for transactions, Monad helps improve throughput without compromising the seamless user and developer experience. Applications built on Ethereum work effortlessly on Monad, making it an ideal network for both new projects and established decentralized applications.

## Contribution

Contributions are always welcome! Whether you want to improve the code, add new features, or fix bugs, please open an issue or submit a pull request. Your input helps make the Monad Faucet Automation tool more robust and user-friendly.

## License

This project is licensed under the [MIT License](LICENSE).














[![Join our Telegram RU](https://img.shields.io/badge/Telegram-RU-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aero25x)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aero25x)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@flaming_chameleon)
[![Reddit](https://img.shields.io/badge/Reddit-FF3A00?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/HiddenCode/)
[![Join our Telegram ENG](https://img.shields.io/badge/Telegram-EN-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding_en)
