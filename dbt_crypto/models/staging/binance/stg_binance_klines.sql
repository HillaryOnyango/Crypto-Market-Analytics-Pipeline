with source as (

    select * from {{ source('raw', 'raw_binance_klines') }}

),

cleaned as (

    select
        symbol,
        interval,
        to_timestamp(open_time / 1000.0) as candle_open_ts,
        to_timestamp(close_time / 1000.0) as candle_close_ts,
        cast(open_price as numeric) as open_price,
        cast(high_price as numeric) as high_price,
        cast(low_price as numeric) as low_price,
        cast(close_price as numeric) as close_price,
        cast(volume as numeric) as volume,
        ingestion_time
    from source

)

select * from cleaned
