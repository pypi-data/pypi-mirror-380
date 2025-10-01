
from __future__ import annotations
import polars as pl, json, time

def save_parquet_with_meta(df: pl.DataFrame, path: str, meta: dict | None = None):
    df = df if isinstance(df, pl.DataFrame) else pl.DataFrame(df)
    if meta:
        df = df.with_columns([pl.lit(json.dumps(meta)).alias("__meta__")])
    df.write_parquet(path)
    return path
