create table if not exists raw.raw_binance_klines (
    symbol text,
    interval text,
    open_time bigint,
    open_price numeric,
    high_price numeric,
    low_price numeric,
    close_price numeric,
    volume numeric,
    close_time bigint,
    ingestion_time timestamp default current_timestamp
);