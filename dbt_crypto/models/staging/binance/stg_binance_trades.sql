with source as (

    select * from {{ source('raw', 'raw_binance_trades') }}

),

cleaned as (

    select
        symbol,
        agg_trade_id,
        to_timestamp(trade_time / 1000.0) as trade_ts,
        cast(price as numeric) as price,
        cast(quantity as numeric) as quantity,
        cast(first_trade_id as bigint) as first_trade_id,
        cast(last_trade_id as bigint) as last_trade_id,
        cast(is_buyer_maker as boolean) as is_buyer_maker,
        cast(is_best_match as boolean) as is_best_match,
        ingestion_time
    from source

)

select * from cleaned