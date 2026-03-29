with trades as (

    select * from {{ ref('stg_binance_trades') }}

)

select
    symbol,
    date_trunc('day', trade_ts) as trade_date,
    sum(quantity) as total_base_volume,
    avg(price) as avg_trade_price,
    count(*) as total_trades
from trades
group by 1, 2
