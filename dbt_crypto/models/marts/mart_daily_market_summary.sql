with candles as (

    select * from {{ ref('stg_binance_klines') }}

),

daily as (

    select
        symbol,
        date_trunc('day', candle_open_ts) as market_date,
        avg(close_price) as avg_daily_price,
        max(high_price) as daily_high,
        min(low_price) as daily_low,
        sum(volume) as total_volume,
        count(*) as total_candles
    from candles
    group by 1, 2

)

select * from daily
