import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BINANCE_BASE_URL", "https://data-api.binance.vision")

def get_klines(symbol: str, interval: str = "1h", limit: int = 100):
    url = f"{BASE_URL}/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()

def get_agg_trades(symbol: str, limit: int = 500):
    url = f"{BASE_URL}/api/v3/aggTrades"
    params = {"symbol": symbol, "limit": limit}
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()

def get_ticker_24hr(symbol: str):
    url = f"{BASE_URL}/api/v3/ticker/24hr"
    params = {"symbol": symbol}
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()