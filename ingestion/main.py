from datetime import datetime, UTC

import pandas as pd
from sqlalchemy import text

from ingestion.binance_client import get_klines
from ingestion.load_postgres import get_engine

symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]


def run():
    engine = get_engine()

    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw"))

    for symbol in symbols:
        data = get_klines(symbol)

        rows = []
        for k in data:
            rows.append(
                {
                    "symbol": symbol,
                    "interval": "1h",
                    "open_time": k[0],
                    "open_price": k[1],
                    "high_price": k[2],
                    "low_price": k[3],
                    "close_price": k[4],
                    "volume": k[5],
                    "close_time": k[6],
                    "ingestion_time": datetime.now(UTC),
                }
            )

        df = pd.DataFrame(rows)

        df.to_sql(
            "raw_binance_klines",
            engine,
            schema="raw",
            if_exists="append",
            index=False,
        )

        print(f"Loaded {len(df)} rows for {symbol}")


if __name__ == "__main__":
    run()