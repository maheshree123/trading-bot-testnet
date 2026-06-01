# Binance Futures Testnet Trading Bot

## Overview

A Python-based trading bot for Binance Futures Testnet (USDT-M) that allows users to place MARKET and LIMIT orders through a command-line interface and a lightweight Streamlit UI.

The application is designed with a modular architecture, input validation, logging, and exception handling to ensure reliability and maintainability.

---

## Features

* Place MARKET orders
* Place LIMIT orders
* Support BUY and SELL sides
* Binance Futures Testnet integration
* Command Line Interface (CLI)
* Streamlit-based UI
* Input validation
* Structured logging
* Error handling for API and network failures

---

## Project Structure

trading_bot/

├── bot/

│   ├── client.py

│   ├── orders.py

│   ├── validators.py

│   └── logging_config.py

├── cli.py

├── app.py

├── logs/

├── requirements.txt

└── README.md

---

## Technologies Used

* Python 3.x
* Binance Futures Testnet API
* python-binance
* Streamlit
* Logging
* argparse

---

## Setup

### 1. Clone the repository

git clone <repository-url>

cd trading_bot

### 2. Create a virtual environment

python -m venv venv

### 3. Activate the environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### 4. Install dependencies

pip install -r requirements.txt

### 5. Configure API credentials

Create a `.env` file:

API_KEY=your_api_key

API_SECRET=your_api_secret

---

## Running the CLI

### Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 110000

---

## Running the Streamlit UI

streamlit run app.py

---

## Logging

All API requests, responses, and errors are stored in the log file.

Example information logged:

* Order requests
* Order responses
* Validation failures
* API exceptions
* Network errors

---

## Error Handling

The application handles:

* Invalid symbols
* Invalid order types
* Invalid quantities
* Missing limit order price
* Binance API exceptions
* Network connectivity issues

---

## Sample Output

Order Request:

Symbol: BTCUSDT

Side: BUY

Type: MARKET

Quantity: 0.001

Order Response:

Order ID: 12345678

Status: FILLED

Executed Quantity: 0.001

Success: Order placed successfully

---

## Assumptions

* Users have an active Binance Futures Testnet account.
* Valid API credentials are configured.
* Testnet environment is available.

---

## Future Improvements

* Stop-Limit Orders
* OCO Orders
* Grid Trading Strategies
* Trade History Dashboard
* Risk Management Features

---

## Author

Maheshree Katla
Computer Engineering Student
