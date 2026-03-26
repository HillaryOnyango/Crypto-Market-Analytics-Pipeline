import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BINANCE_BASE_URL")


def get_klines(symbol: str, interval: str = "1h", limit: int = 100):
    url = f"{BASE_URL}/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()