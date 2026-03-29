from ingestion.binance_client import get_klines, get_agg_trades, get_ticker_24hr
from ingestion.load_postgres import get_engine
import pandas as pd
from datetime import datetime, UTC

symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]

def load_klines(engine):
    for symbol in symbols:
        data = get_klines(symbol)

        rows = []
        for k in data:
            rows.append({
                "symbol": symbol,
                "interval": "1h",
                "open_time": k[0],
                "open_price": k[1],
                "high_price": k[2],
                "low_price": k[3],
                "close_price": k[4],
                "volume": k[5],
                "close_time": k[6],
                "ingestion_time": datetime.now(UTC)
            })

        df = pd.DataFrame(rows)
        df.to_sql("raw_binance_klines", engine, schema="raw", if_exists="append", index=False)
        print(f"Loaded {len(df)} kline rows for {symbol}")

def load_trades(engine):
    for symbol in symbols:
        data = get_agg_trades(symbol)

        rows = []
        for t in data:
            rows.append({
                "symbol": symbol,
                "agg_trade_id": t["a"],
                "price": t["p"],
                "quantity": t["q"],
                "first_trade_id": t["f"],
                "last_trade_id": t["l"],
                "trade_time": t["T"],
                "is_buyer_maker": t["m"],
                "is_best_match": t["M"],
                "ingestion_time": datetime.now(UTC)
            })

        df = pd.DataFrame(rows)
        df.to_sql("raw_binance_trades", engine, schema="raw", if_exists="append", index=False)
        print(f"Loaded {len(df)} trade rows for {symbol}")

def load_tickers(engine):
    rows = []
    for symbol in symbols:
        t = get_ticker_24hr(symbol)
        rows.append({
            "symbol": t["symbol"],
            "price_change": t["priceChange"],
            "price_change_percent": t["priceChangePercent"],
            "weighted_avg_price": t["weightedAvgPrice"],
            "last_price": t["lastPrice"],
            "last_qty": t["lastQty"],
            "open_price": t["openPrice"],
            "high_price": t["highPrice"],
            "low_price": t["lowPrice"],
            "volume": t["volume"],
            "quote_volume": t["quoteVolume"],
            "open_time": t["openTime"],
            "close_time": t["closeTime"],
            "first_id": t["firstId"],
            "last_id": t["lastId"],
            "trade_count": t["count"],
            "ingestion_time": datetime.now(UTC)
        })

    df = pd.DataFrame(rows)
    df.to_sql("raw_binance_tickers", engine, schema="raw", if_exists="append", index=False)
    print(f"Loaded {len(df)} ticker rows")

def run():
    engine = get_engine()
    load_klines(engine)
    load_trades(engine)
    load_tickers(engine)

if __name__ == "__main__":
    run()