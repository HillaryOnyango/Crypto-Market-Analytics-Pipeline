with candles as (

    select * from {{ ref('stg_binance_klines') }}

),

hourly as (

    select
        symbol,
        candle_open_ts as hour_ts,
        high_price,
        low_price,
        close_price,
        case
            when close_price = 0 then null
            else (high_price - low_price) / close_price
        end as hourly_volatility_ratio
    from candles
    where interval = '1h'

)

select * from hourly
