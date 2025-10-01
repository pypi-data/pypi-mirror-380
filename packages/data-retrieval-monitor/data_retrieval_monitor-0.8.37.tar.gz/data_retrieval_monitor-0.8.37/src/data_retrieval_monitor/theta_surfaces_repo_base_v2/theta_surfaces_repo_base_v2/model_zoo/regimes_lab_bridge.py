from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Iterable, List
import numpy as np
import polars as pl
import pandas as pd


def _ensure_datetime(df: pl.DataFrame, col: str) -> pl.DataFrame:
    if df.schema.get(col) not in (pl.Datetime,):
        try:
            return df.with_columns(pl.col(col).cast(pl.Datetime))
        except Exception:
            return df
    return df


def build_labels_regimes_lab(
    *,
    df: pl.DataFrame,
    time_col: str,
    feature_cols: List[str],
    asset_col: str = "asset_id",
    split_tag: str = "full",
    regime_models: List[str] | None = None,  # <— NEW
) -> pl.DataFrame:
    """Run regimes_lab on per-asset features to obtain labels for selected/all regime models.

    Returns a long DataFrame with columns: time, asset_id, model_name, regime_code (int).
    """
    import pandas as pd
    import analytics.regimes_lab.regimes as R

    df = _ensure_datetime(df, time_col)
    out_parts: List[pl.DataFrame] = []
    for asset, g in df.group_by(asset_col):
        pdf = (
            g.select([time_col] + feature_cols)
             .to_pandas()
             .set_index(time_col)
             .sort_index()
        )
        if pdf.empty:
            continue
        # pass through chosen models if provided
        L = R.load_or_build_labels(pdf, split_tag=split_tag, models=regime_models)
        L = L.copy(); L.index.name = time_col
        L[asset_col] = str(asset)
        L_long = (
            L.reset_index()
             .melt(id_vars=[time_col, asset_col], var_name="model_name", value_name="regime_code")
        )
        out_parts.append(pl.from_pandas(L_long))
    if not out_parts:
        return pl.DataFrame({"time": [], asset_col: [], "model_name": [], "regime_code": []})
    labels = pl.concat(out_parts).rename({time_col: "time", asset_col: "asset_id"})
    labels = labels.with_columns([
        pl.col("time").cast(pl.Datetime),
        pl.col("asset_id").cast(pl.Utf8),
        pl.col("model_name").cast(pl.Utf8),
        pl.col("regime_code").cast(pl.Int32),
    ])
    return labels


@dataclass
class RegimeAlphaBuildCfg:
    time_col: str = "time"
    asset_col: str = "asset_id"
    return_cols: Dict[str, int] = None  # mapping: col -> horizon
    lags: List[int] = None
    window: int = 120
    annualization: float = 252.0
    target_universe: str = "UNKNOWN"
    model_version_id: str = "v1"
    model_owner_id: str = "regimes_lab"
    hyper_id: str = "h0"
    regime_models: List[str] | None = None  # subset of label model_name to include


def build_alpha_from_regimes_lab(
    *,
    features: pl.DataFrame,
    labels_long: pl.DataFrame,
    cfg: RegimeAlphaBuildCfg,
) -> pl.DataFrame:
    """Convert regimes_lab labels to tall alpha metric surfaces.

    Emits rows with columns:
      time, model_id, model_version_id, model_owner_id, hyper_id,
      target_universe, target_name, regime_id, horizon, lag,
      metric_name, metric_value
    where metrics ∈ {t_stat, p_val (approx), sharpe, ir}.
    """
    if not cfg.return_cols or not cfg.lags:
        raise ValueError("cfg.return_cols and cfg.lags must be provided")

    f = _ensure_datetime(features, cfg.time_col)
    L = labels_long.rename({cfg.time_col: "time", cfg.asset_col: "asset_id"})
    L = _ensure_datetime(L, "time")
    if cfg.regime_models:
        L = L.filter(pl.col("model_name").is_in(cfg.regime_models))

    keep_cols = [cfg.time_col, cfg.asset_col] + [c for c in cfg.return_cols.keys() if c in f.columns]
    f2 = f.select(keep_cols)
    df = f2.join(L.select(["time","asset_id","model_name","regime_code"]),
                 left_on=[cfg.time_col, cfg.asset_col], right_on=["time","asset_id"], how="inner")
    if df.is_empty():
        return pl.DataFrame({
            "time": [], "model_id": [], "model_version_id": [], "model_owner_id": [], "hyper_id": [],
            "target_universe": [], "target_name": [], "regime_id": [], "horizon": [], "lag": [],
            "metric_name": [], "metric_value": []
        })

    parts: List[pl.DataFrame] = []
    for ret_col, h in cfg.return_cols.items():
        if ret_col not in df.columns:
            continue
        for lag in cfg.lags:
            d = df.sort([cfg.asset_col, "model_name", "regime_code", cfg.time_col])
            d = d.with_columns((pl.col(ret_col).shift(-int(lag))).alias("ret_fwd"))
            keys = [cfg.asset_col, "model_name", "regime_code"]
            d = d.with_columns([
                pl.col("ret_fwd").rolling_mean(window_size=cfg.window).over(keys).alias("mu"),
                pl.col("ret_fwd").rolling_std(window_size=cfg.window).over(keys).alias("sd"),
                (pl.col("ret_fwd").is_not_null().cast(pl.Int32).rolling_sum(window_size=cfg.window).over(keys)).alias("n"),
            ])
            d = d.with_columns([
                (pl.when(pl.col("sd") > 0).then(pl.col("mu") / (pl.col("sd") / (pl.col("n").cast(pl.Float64).sqrt().clip_min(1.0)))).otherwise(None)).alias("t_stat"),
                (pl.col("t_stat").abs().map_elements(lambda x: float(np.exp(-abs(x))) if x is not None and np.isfinite(x) else None, return_dtype=pl.Float64)).alias("p_val"),
                (pl.when(pl.col("sd") > 0).then(pl.col("mu") / pl.col("sd")).otherwise(None)).alias("sharpe"),
            ])
            d = d.with_columns(((pl.col("sharpe") * float(cfg.annualization) ** 0.5)).alias("ir"))
            id_cols = [cfg.time_col, cfg.asset_col, "model_name", "regime_code"]
            metrics = d.select(id_cols + [pl.lit(int(h)).alias("horizon"), pl.lit(int(lag)).alias("lag"), "t_stat","p_val","sharpe","ir"])
            tall = metrics.melt(id_vars=[cfg.time_col, cfg.asset_col, "model_name", "regime_code", "horizon","lag"],
                                variable_name="metric_name", value_name="metric_value")
            parts.append(tall)
    if not parts:
        return pl.DataFrame({
            "time": [], "model_id": [], "model_version_id": [], "model_owner_id": [], "hyper_id": [],
            "target_universe": [], "target_name": [], "regime_id": [], "horizon": [], "lag": [],
            "metric_name": [], "metric_value": []
        })

    out = pl.concat(parts)
    out = out.with_columns([
        pl.col(cfg.time_col).alias("time"),
        pl.col(cfg.asset_col).alias("target_name"),
        pl.lit(cfg.target_universe).alias("target_universe"),
        (pl.lit("reglab_") + pl.col("model_name")).alias("model_id"),
        pl.lit(cfg.model_version_id).alias("model_version_id"),
        pl.lit(cfg.model_owner_id).alias("model_owner_id"),
        pl.lit(cfg.hyper_id).alias("hyper_id"),
        pl.col("regime_code").cast(pl.Utf8).alias("regime_id"),
    ])
    cols = [
        "time","model_id","model_version_id","model_owner_id","hyper_id",
        "target_universe","target_name","regime_id","horizon","lag","metric_name","metric_value"
    ]
    out = out.select(cols).sort(["time","target_name","model_id","horizon","lag","metric_name"])
    return out


def build_alpha_from_regimes_lab_ols_hac(
    *,
    returns: pd.DataFrame | pl.DataFrame,
    labels_long: pl.DataFrame | pd.DataFrame,
    horizons: Iterable[int],
    lags: Iterable[int],
    hac_lags: int = 5,
    target_universe: str = "UNKNOWN",
    model_version_id: str = "v1",
    model_owner_id: str = "regimes_lab",
    hyper_id: str = "h0",
) -> pl.DataFrame:
    """Mimic runner logic: OLS(HAC) per (factor, model, regime, lag, horizon)."""
    try:
        import statsmodels.api as sm  # noqa: F401
    except Exception as e:
        raise RuntimeError(f"statsmodels required for OLS-HAC: {e}")

    # normalize inputs
    if isinstance(returns, pl.DataFrame):
        R = returns.to_pandas()
        if "time" in R.columns:
            R = R.set_index("time")
    else:
        R = returns.copy()
    if not isinstance(R.index, pd.DatetimeIndex):
        R.index = pd.to_datetime(R.index)
    R = R.sort_index()

    if isinstance(labels_long, pl.DataFrame):
        L = labels_long.to_pandas()
    else:
        L = labels_long.copy()

    Lw = L.pivot_table(index=["time","asset_id"], columns="model_name", values="regime_code", aggfunc="first")
    Lw = Lw.groupby(level=0).agg(lambda s: pd.Series(s).mode().iloc[0] if len(pd.Series(s).mode())>0 else np.nan)
    if not isinstance(Lw.index, pd.DatetimeIndex):
        Lw.index = pd.to_datetime(Lw.index)
    Lw = Lw.sort_index()

    def fut_sum(y: pd.Series, h: int) -> pd.Series:
        h = int(h)
        if h <= 1:
            return y.copy()
        return y.rolling(h).sum().shift(-h + 1)

    rows = []
    factors = list(R.columns)
    models = list(Lw.columns)
    import statsmodels.api as sm
    for fac in factors:
        r = R[fac].astype(float)
        for h in horizons:
            y = fut_sum(r, int(h)).dropna()
            Lh = Lw.reindex(y.index).copy()
            for m in models:
                lab = pd.to_numeric(Lh[m], errors="coerce")
                if lab.dropna().empty:
                    continue
                regimes = sorted([int(v) for v in pd.unique(lab.dropna())])
                for rid in regimes:
                    for lag in lags:
                        d = (lab.shift(int(lag)) == rid).astype(float)
                        df = pd.concat([y.rename("y"), d.rename("x")], axis=1).replace([np.inf,-np.inf], np.nan).dropna()
                        if df.shape[0] < 50 or df["x"].sum() < 5:
                            continue
                        Xc = sm.add_constant(df[["x"]], has_constant="add")
                        res = sm.OLS(df["y"], Xc, missing="drop").fit(cov_type="HAC", cov_kwds={"maxlags": int(hac_lags)})
                        coef = float(res.params.get("x", np.nan))
                        tval = float(res.tvalues.get("x", np.nan))
                        pval = float(res.pvalues.get("x", np.nan))
                        w = np.sign(coef) * df["x"].values
                        r_strat = w * df["y"].values
                        mu = float(np.nanmean(r_strat))
                        sd = float(np.nanstd(r_strat, ddof=1))
                        sr = (mu / sd) if (sd and sd > 0) else np.nan
                        ir = float(sr * (252.0 ** 0.5)) if sr == sr else np.nan
                        t_last = df.index.max()
                        rows += [
                            {"time": t_last, "model_id": f"reglab_{m}", "model_version_id": model_version_id, "model_owner_id": model_owner_id, "hyper_id": hyper_id,
                             "target_universe": target_universe, "target_name": fac, "regime_id": str(rid), "horizon": int(h), "lag": int(lag),
                             "metric_name": "t_stat", "metric_value": tval},
                            {"time": t_last, "model_id": f"reglab_{m}", "model_version_id": model_version_id, "model_owner_id": model_owner_id, "hyper_id": hyper_id,
                             "target_universe": target_universe, "target_name": fac, "regime_id": str(rid), "horizon": int(h), "lag": int(lag),
                             "metric_name": "p_val", "metric_value": pval},
                            {"time": t_last, "model_id": f"reglab_{m}", "model_version_id": model_version_id, "model_owner_id": model_owner_id, "hyper_id": hyper_id,
                             "target_universe": target_universe, "target_name": fac, "regime_id": str(rid), "horizon": int(h), "lag": int(lag),
                             "metric_name": "sharpe", "metric_value": sr},
                            {"time": t_last, "model_id": f"reglab_{m}", "model_version_id": model_version_id, "model_owner_id": model_owner_id, "hyper_id": hyper_id,
                             "target_universe": target_universe, "target_name": fac, "regime_id": str(rid), "horizon": int(h), "lag": int(lag),
                             "metric_name": "ir", "metric_value": ir},
                        ]
    return pl.from_pandas(pd.DataFrame(rows))