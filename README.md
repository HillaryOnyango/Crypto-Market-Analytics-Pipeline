**# Crypto-Market-Analytics-Pipeline**
This project implements a modern ELT (Extract–Load–Transform) data pipeline for cryptocurrency market analytics.
It ingests real-time market data from the Binance API, stores raw data in PostgreSQL, transforms it using dbt, and visualizes insights in Grafana.

The goal is to simulate a production-grade data engineering workflow similar to those used in fintech and trading platforms.

It ingests real-time market data from the Binance API, stores raw data in PostgreSQL, transforms it using dbt, and visualizes insights in Grafana.

The goal is to simulate a production-grade data engineering workflow similar to those used in fintech and trading platforms.

**Objectives**
Extract market data from Binance API
Load raw data into PostgreSQL
Transform data using dbt
Build analytics-ready tables
Answer key crypto market questions

**Architecture**
Binance API
   ↓
Python Ingestion Layer
   ↓
PostgreSQL (Raw Layer)
   ↓
dbt Staging Models
   ↓
dbt Intermediate Models
   ↓
dbt Mart Tables
   ↓
Grafana Dashboards

| Tool       | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Data ingestion from Binance API |
| PostgreSQL | Data warehouse                  |
| dbt Core   | Data transformation & modeling  |
| Grafana    | Data visualization              |
| Git/GitHub | Version control                 |

**📊 Data Sources**

Data is fetched from Binance public REST API:

Klines (candlestick data)
Trades / Aggregate trades
24h ticker statistics
Symbol metadata
Supported Trading Pairs
BTCUSDT
ETHUSDT
BNBUSDT

**🗃️ Data Modeling**

This project follows a three-layer dbt architecture:

1️⃣ Staging Layer (stg_*)

Purpose: Clean and standardize raw data

Rename columns
Convert timestamps
Cast data types
Remove duplicates

**Examples:**

stg_binance_klines
stg_binance_trades
stg_binance_tickers

2️⃣ Intermediate Layer (int_*)

Purpose: Enrich and aggregate data

Calculate price changes
Aggregate trading volumes
Join datasets

Examples:

int_price_metrics
int_symbol_volume
int_hourly_volatility
3️⃣ Mart Layer (fct_*, dim_*, mart_*)

Purpose: Analytics-ready tables

Examples:

fct_crypto_candles
fct_crypto_trades
dim_symbols
mart_daily_market_summary
mart_rolling_7d_price
📈 Key Analytics Questions

This pipeline enables answering:

What is the daily average price of each cryptocurrency?
Which cryptocurrency has the highest trading volume?
What is the hourly price volatility?
Which trading pair has the largest price movement?
What is the 7-day rolling average price trend?

**🛠️ Project Structure**

crypto-analytics-pipeline/
│
├── ingestion/
│   ├── binance_client.py
│   ├── extract_klines.py
│   ├── extract_trades.py
│   ├── extract_tickers.py
│   └── load_postgres.py
│
├── dbt_crypto/
│   ├── models/
│   │   ├── staging/
│   │   ├── intermediate/
│   │   └── marts/
│   └── dbt_project.yml
│
├── sql/
│   └── create_tables.sql
│
├── dashboards/
│   └── grafana_config.json
│
├── docker-compose.yml
├── requirements.txt
└── README.md
