from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
import polars as pl
import statsmodels.api as sm


try:
    # Prefer configs from analytics.regimes_lab
    from analytics.regimes_lab.configs import TRAIN_FRAC, VAL_FRAC
except Exception:  # fallback defaults
    TRAIN_FRAC, VAL_FRAC = 0.6, 0.2


@dataclass
class SplitSlices:
    train: slice
    val: slice
    test: slice


def _split_slices(idx: pd.DatetimeIndex) -> SplitSlices:
    T = len(idx)
    n_tr = int(TRAIN_FRAC * T)
    n_va = int(VAL_FRAC * T)
    te0 = n_tr + n_va
    return SplitSlices(slice(0, n_tr), slice(n_tr, te0), slice(te0, T))


def _split_info(idx: pd.DatetimeIndex, which: str) -> Tuple[str, str]:
    ss = _split_slices(idx)
    s = ss.train if which == "train" else ss.val if which == "val" else ss.test
    if s.start >= s.stop:
        return ("NA", "NA")
    a = idx[s.start]
    b = idx[s.stop - 1]
    return (str(pd.to_datetime(a)), str(pd.to_datetime(b)))


def _labels_mode_wide(labels_long: pl.DataFrame) -> pl.DataFrame:
    """Polars: per (time, model_name) mode(regime_code) pivoted to wide."""
    if labels_long.is_empty():
        return pl.DataFrame({"time": [], "__empty__": []})
    mode_col = (
        labels_long
        .group_by(["time", "model_name"])  # across assets
        .agg(pl.col("regime_code").mode().first().alias("regime_code"))
        .sort(["time", "model_name"])
    )
    wide = (
        mode_col
        .pivot(index="time", columns="model_name", values="regime_code")
        .sort("time")
    )
    return wide


def _future_sum(y: pd.Series, h: int) -> pd.Series:
    h = int(h)
    return y if h <= 1 else y.rolling(h).sum().shift(-(h - 1))


def _build_dummy_matrix(lab_vals: np.ndarray, regimes: Sequence[str], lags: Sequence[int]) -> Tuple[np.ndarray, List[Tuple[str, int]]]:
    """Return X_full (T×K) and list of (regime_code, lag) per column.

    lab_vals should be a 1-D numpy array of dtype object/str.
    """
    T = lab_vals.shape[0]
    cols = []
    names: List[Tuple[str, int]] = []
    for rid in regimes:
        # equality mask (string compare)
        eq = (lab_vals == rid)
        eq = eq.astype(float, copy=False)
        for L in lags:
            L = int(L)
            if L <= 0:
                x = eq.copy()
            else:
                x = np.empty_like(eq)
                x[:L] = 0.0
                x[L:] = eq[:-L]
            cols.append(x)
            names.append((rid, L))
    X = np.column_stack(cols) if cols else np.zeros((T, 0), dtype=float)
    return X, names


def _rows_from_fit(
    *,
    split_name: str,
    data_freq: str,
    target_universe: str,
    target_name: str,
    model_id: str,
    h: int,
    y: np.ndarray,
    Xk: np.ndarray,
    kept_names: List[Tuple[int, int]],
    res,
    idx_slice: pd.DatetimeIndex,
) -> List[Dict]:
    rows: List[Dict] = []
    # Statsmodels returns params/tvals/pvals including constant at index 0
    betas = res.params[1:]
    tvals = res.tvalues[1:]
    pvals = res.pvalues[1:]
    for j, (rid, L) in enumerate(kept_names):
        b = float(betas[j])
        t = float(tvals[j])
        p = float(pvals[j])
        # Strategy IR based on sign(beta) * dummy
        pos = np.sign(b) * Xk[:, j]
        r_strat = pos * y
        mu = float(np.nanmean(r_strat))
        sd = float(np.nanstd(r_strat, ddof=1))
        sr = mu / sd if sd > 0 else np.nan
        ir = float(sr * (252.0 ** 0.5)) if np.isfinite(sr) else np.nan
        ds, de = (str(idx_slice[0]) if len(idx_slice) else "NA", str(idx_slice[-1]) if len(idx_slice) else "NA")
        t_last = str(pd.to_datetime(idx_slice.max())) if len(idx_slice) else "NA"
        base = {
            "split": split_name,
            "data_freq": data_freq,
            "date_start": ds,
            "date_end": de,
            "time": t_last,
            "model_id": model_id,
            "model_version_id": "v1",
            "model_owner_id": "regimes_lab",
            "hyper_id": "h0",
            "target_universe": target_universe,
            "target_name": target_name,
            "regime_id": str(rid),
            "horizon": int(h),
            "lag": int(L),
        }
        rows += [
            {**base, "metric_name": "t_stat_hac", "metric_value": t},
            {**base, "metric_name": "p_val_hac", "metric_value": p},
            {**base, "metric_name": "ir", "metric_value": ir},
        ]
    return rows


def build_alpha_hac_splits_fast(
    R: pd.DataFrame,
    labels_long: pl.DataFrame,
    horizons: Sequence[int],
    lags: Sequence[int],
    *,
    hac_lags: int = 5,
    target_universe: str = "US_EQ",
    data_freq: str = "1D",
    min_rows: int = 50,
    min_on: int = 5,
    n_jobs: int = 1,
) -> pl.DataFrame:
    """Fast builder for OLS-HAC split metrics.

    - Polars mode aggregation for labels across assets per (time, model).
    - Vectorized dummy construction per (model, regimes, lags).
    - One OLS per (factor, horizon, model, split) with multi-column X.
    - Early filters: ON-count threshold and min rows per split.
    - Optional parallelism across (factor, horizon).
    """
    # Ensure R is datetime-indexed & sorted
    if not isinstance(R.index, pd.DatetimeIndex):
        R = R.copy()
        R.index = pd.to_datetime(R.index)
    R = R.sort_index()
    idx = R.index
    splits = _split_slices(idx)

    # Mode labels per time×model (wide), as Polars then pandas for quick array access
    labels_wide_pl = _labels_mode_wide(labels_long)
    labels_wide_pd = labels_wide_pl.sort("time").to_pandas()
    labels_wide_pd["time"] = pd.to_datetime(labels_wide_pd["time"], utc=False, errors="coerce")
    labels_wide_pd = labels_wide_pd.set_index("time").sort_index()
    # Align label times to R times; try exact first, then pad/bfill fallbacks
    Lw_exact = labels_wide_pd.reindex(idx)
    if Lw_exact.isna().all().all():
        # forward fill to handle piecewise-constant regimes sampled at lower frequency
        Lw_ffill = labels_wide_pd.reindex(idx, method="ffill")
        if Lw_ffill.isna().all().all():
            Lw_bfill = labels_wide_pd.reindex(idx, method="bfill")
            Lw = Lw_bfill
        else:
            Lw = Lw_ffill
    else:
        Lw = Lw_exact

    # Prepare tasks across (factor, horizon)
    factors: List[str] = list(R.columns)
    horizons = [int(h) for h in horizons]

    def _process_one(fac: str, h: int) -> List[Dict]:
        out_rows: List[Dict] = []
        # compute y(h)
        r = pd.to_numeric(R[fac], errors="coerce").astype(float)
        y_full = _future_sum(r, h).dropna()
        if y_full.empty:
            return out_rows
        # Align labels to y_full index; attempt exact then pad fallback
        Lwy = Lw.reindex(y_full.index)
        if Lwy.isna().all().all():
            Lwy = Lw.reindex(y_full.index, method="ffill")
            if Lwy.isna().all().all():
                Lwy = Lw.reindex(y_full.index, method="bfill")
        if Lw.empty:
            return out_rows
        # Split indices must be based on y_full (after horizon rolling)
        y_splits = _split_slices(y_full.index)

        # For each model (column)
        for m in Lwy.columns:
            # keep original codes; do not coerce to numeric to avoid dropping string regimes like 'r1'
            lab = Lwy[m]
            if lab.dropna().empty:
                continue
            # Unique regime codes as strings
            regimes = sorted(str(v) for v in pd.unique(lab.dropna().astype(str)))
            lab_vals = lab.astype(str).to_numpy()
            X_full, names = _build_dummy_matrix(lab_vals, regimes, lags)
            if X_full.shape[1] == 0:
                continue

            # Precompute ON-counts per split (based on y_splits) and drop columns failing min_on in ALL splits
            keep_global = np.zeros(X_full.shape[1], dtype=bool)
            for split_name, s in (("train", y_splits.train), ("val", y_splits.val), ("test", y_splits.test)):
                xs = X_full[s, :]
                keep_global |= (xs.sum(axis=0) >= float(min_on))
            if not keep_global.any():
                continue
            X_full = X_full[:, keep_global]
            kept_names = [nm for (nm, k) in zip(names, keep_global) if k]

            # Per split fit once
            for split_name, s in (("train", y_splits.train), ("val", y_splits.val), ("test", y_splits.test)):
                y = y_full.to_numpy()[s]
                X = X_full[s, :]
                # Early exits
                if y.size < int(min_rows) or X.shape[1] == 0:
                    continue
                # Drop columns that are all-zero within this split
                keep = (X.sum(axis=0) >= float(min_on))
                if not keep.any():
                    continue
                Xk = X[:, keep]
                split_names = [nm for (nm, k) in zip(kept_names, keep) if k]
                try:
                    Xc = np.column_stack([np.ones(len(y)), Xk])
                    res = sm.OLS(y, Xc, missing="drop").fit(
                        cov_type="HAC", cov_kwds={"maxlags": int(hac_lags)}
                    )
                except Exception:
                    continue
                idx_slice = y_full.index[s]
                out_rows.extend(
                    _rows_from_fit(
                        split_name=split_name,
                        data_freq=data_freq,
                        target_universe=target_universe,
                        target_name=fac,
                        model_id=f"reglab_{m}",
                        h=h,
                        y=y,
                        Xk=Xk,
                        kept_names=split_names,
                        res=res,
                        idx_slice=idx_slice,
                    )
                )
        return out_rows

    results: List[Dict] = []
    if n_jobs and int(n_jobs) > 1:
        # Use concurrent.futures for portability
        from concurrent.futures import ProcessPoolExecutor, as_completed

        # Note: functions must be pickleable; define inner task as top-level closure args
        tasks = [(f, h) for f in factors for h in horizons]
        with ProcessPoolExecutor(max_workers=int(n_jobs)) as ex:
            futs = {ex.submit(_process_one, f, h): (f, h) for (f, h) in tasks}
            for fut in as_completed(futs):
                try:
                    results.extend(fut.result())
                except Exception:
                    # best-effort; skip failed tasks
                    pass
    else:
        for f in factors:
            for h in horizons:
                results.extend(_process_one(f, h))

    return pl.from_pandas(pd.DataFrame(results))
