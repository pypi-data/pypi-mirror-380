from __future__ import annotations
import polars as pl

_UNIVERSE_TZ = {
    "US_EQ": "America/New_York",
    "UK_EQ": "Europe/London",
}

def _localize(df: pl.DataFrame, *, time_col: str, universe: str) -> pl.DataFrame:
    tz = _UNIVERSE_TZ.get(universe, "Europe/London")
    # If time is string or naive datetime, parse/localize; else return as-is
    if df.schema.get(time_col) in (pl.Utf8, pl.String):
        return df.with_columns(pl.col(time_col).str.strptime(pl.Datetime, strict=False, time_unit="us").dt.replace_time_zone(tz))
    elif df.schema.get(time_col) == pl.Datetime:
        # If tz-naive, set timezone; if tz-aware, leave
        try:
            return df.with_columns(pl.col(time_col).dt.replace_time_zone(tz))
        except Exception:
            return df
    return df

def in_session(df: pl.DataFrame, *, time_col: str, universe: str) -> pl.DataFrame:
    df = _localize(df, time_col=time_col, universe=universe)
    # Demo: no filtering window; return localized
    return df

def session_slice(df: pl.DataFrame, *, time_col: str, universe: str, window: str) -> pl.DataFrame:
    df = _localize(df, time_col=time_col, universe=universe)
    # Demo: no window parsing; return localized
    return df
