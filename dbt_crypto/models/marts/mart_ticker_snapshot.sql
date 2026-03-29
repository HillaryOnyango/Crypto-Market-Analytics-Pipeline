with tickers as (

    select * from {{ ref('stg_binance_tickers') }}

)

select
    symbol,
    close_ts as snapshot_ts,
    last_price,
    weighted_avg_price,
    price_change,
    price_change_percent,
    volume,
    quote_volume,
    trade_count,
    high_price,
    low_price
from tickers
