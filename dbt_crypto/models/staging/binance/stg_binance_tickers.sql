with source as (

    select * from {{ source('raw', 'raw_binance_tickers') }}

),

cleaned as (

    select
        symbol,
        cast(price_change as numeric) as price_change,
        cast(price_change_percent as numeric) as price_change_percent,
        cast(weighted_avg_price as numeric) as weighted_avg_price,
        cast(last_price as numeric) as last_price,
        cast(last_qty as numeric) as last_qty,
        cast(open_price as numeric) as open_price,
        cast(high_price as numeric) as high_price,
        cast(low_price as numeric) as low_price,
        cast(volume as numeric) as volume,
        cast(quote_volume as numeric) as quote_volume,
        to_timestamp(open_time / 1000.0) as open_ts,
        to_timestamp(close_time / 1000.0) as close_ts,
        cast(first_id as bigint) as first_id,
        cast(last_id as bigint) as last_id,
        cast(trade_count as bigint) as trade_count,
        ingestion_time
    from source

)

select * from cleaned