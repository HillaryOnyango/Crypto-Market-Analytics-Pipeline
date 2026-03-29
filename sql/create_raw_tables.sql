create table if not exists raw.raw_binance_trades (
    symbol text,
    agg_trade_id bigint,
    price numeric,
    quantity numeric,
    first_trade_id bigint,
    last_trade_id bigint,
    trade_time bigint,
    is_buyer_maker boolean,
    is_best_match boolean,
    ingestion_time timestamp default current_timestamp
);

create table if not exists raw.raw_binance_tickers (
    symbol text,
    price_change numeric,
    price_change_percent numeric,
    weighted_avg_price numeric,
    last_price numeric,
    last_qty numeric,
    open_price numeric,
    high_price numeric,
    low_price numeric,
    volume numeric,
    quote_volume numeric,
    open_time bigint,
    close_time bigint,
    first_id bigint,
    last_id bigint,
    trade_count bigint,
    ingestion_time timestamp default current_timestamp
);