from __future__ import annotations

import math
from typing import Iterable, Literal

import numpy as np
import pandas as pd
import polars as pl

try:
    import statsmodels.api as sm  # type: ignore
except Exception:  # pragma: no cover
    sm = None


def future_sum(y: pd.Series, h: int) -> pd.Series:
    """Forward h-step sum aligned at t.

    y_h(t) = sum_{i=0..h-1} y(t+i)
    """
    h = int(h)
    if h <= 1:
        return y.copy()
    return y.rolling(h).sum().shift(-h + 1)


def hac_ols_1x_numpy(y: np.ndarray | pd.Series, x: np.ndarray | pd.Series, maxlags: int = 5) -> tuple[float, float, float, float, float]:
    """NumPy Newey–West HAC for single regressor + intercept.

    Returns (beta1, t_beta1, p_beta1, alpha, se_beta1).
    """
    yv = np.asarray(y, float)
    xv = np.asarray(x, float)
    m = np.isfinite(yv) & np.isfinite(xv)
    yv = yv[m]; xv = xv[m]
    n = yv.shape[0]
    if n < 8:
        return np.nan, np.nan, np.nan, np.nan, np.nan
    X = np.column_stack([np.ones(n), xv])
    # Guard against singular design (e.g., xv constant or all zeros)
    if np.linalg.matrix_rank(X) < 2:
        return np.nan, np.nan, np.nan, np.nan, np.nan
    XtX = X.T @ X
    # Use lstsq to be robust to near-singularity
    beta, *_ = np.linalg.lstsq(X, yv, rcond=None)
    resid = yv - X @ beta
    Z = resid[:, None] * X
    S = (Z.T @ Z) / n
    L = int(maxlags)
    for k in range(1, L + 1):
        w = 1.0 - k / (L + 1.0)
        Gk = (Z[k:].T @ Z[:-k]) / n
        S += w * (Gk + Gk.T)
    Q = XtX / n
    # Pseudo-inverse for stability in edge cases
    Qinv = np.linalg.pinv(Q)
    cov = Qinv @ S @ Qinv
    se = np.sqrt(np.diag(cov))
    b1 = float(beta[1]); a = float(beta[0])
    t = float(b1 / se[1]) if se[1] > 0 else np.nan
    from scipy.stats import norm  # local import
    p = float(2 * norm.sf(abs(t))) if np.isfinite(t) else np.nan
    return b1, t, p, a, float(se[1])


def hac_ols_1x_sm(y: np.ndarray | pd.Series, x: np.ndarray | pd.Series, maxlags: int = 5) -> tuple[float, float, float, float, float]:
    """Statsmodels OLS with HAC covariance for single regressor + intercept.

    Returns (beta1, t_beta1, p_beta1, alpha, se_beta1).
    """
    if sm is None:
        raise RuntimeError("statsmodels not available")
    df = pd.DataFrame({"y": y, "x": x}).replace([np.inf, -np.inf], np.nan).dropna()
    if df.shape[0] < 8:
        return np.nan, np.nan, np.nan, np.nan, np.nan
    Xc = sm.add_constant(df[["x"]], has_constant="add")
    res = sm.OLS(df["y"], Xc, missing="drop").fit(cov_type="HAC", cov_kwds={"maxlags": int(maxlags)})
    b1 = float(res.params.get("x", np.nan))
    t = float(res.tvalues.get("x", np.nan))
    p = float(res.pvalues.get("x", np.nan))
    a = float(res.params.get("const", np.nan))
    se1 = float(res.bse.get("x", np.nan))
    return b1, t, p, a, se1


def _labels_time_by_model(
    labels_long: pl.DataFrame | pd.DataFrame,
    *,
    agg: Literal["mode", "first", "given"] = "mode",
) -> pd.DataFrame:
    """Make a time-indexed wide label table per model_name.

    If multiple assets are present for the same time and model, aggregate across assets.
    - mode: majority regime across assets (consensus universe regime)
    - first: take the first available asset's regime (deterministic if asset ordering is stable)

    Returns a pandas DataFrame indexed by time with columns=model_name and values=regime_code.
    """
    if isinstance(labels_long, pl.DataFrame):
        L = labels_long.to_pandas().copy()
    else:
        L = labels_long.copy()

    if agg == "given":
        # Expect exactly one regime per (time, model_name) across assets.
        # If multiple assets disagree at the same time for a model, this is an error.
        grp = (
            L.groupby(["time", "model_name"])  # type: ignore[arg-type]
             .agg(nu=("regime_code", "nunique"), first_val=("regime_code", "first"))
             .reset_index()
        )
        bad = grp[grp["nu"] > 1]
        if not bad.empty:
            sample = bad.head(5).to_dict(orient="records")
            raise ValueError(
                f"labels_long has conflicting regimes for the same (time, model_name). Example rows: {sample}. "
                f"Provide unique per-time labels or choose label_agg='mode'."
            )
        # Safe to pivot unique values
        Luniq = L.groupby(["time", "model_name"])  # type: ignore[arg-type]
        Luniq = Luniq["regime_code"].first().unstack("model_name")
        Lw = Luniq
    else:
        Lw = L.pivot_table(
            index=["time", "asset_id"],
            columns="model_name",
            values="regime_code",
            aggfunc="first",
        )
    if agg == "mode":
        def _mode_ser(s: pd.Series):
            m = pd.Series(s).mode()
            return m.iloc[0] if len(m) else np.nan

        Lw = Lw.groupby(level=0).agg(_mode_ser)
    elif agg == "first":
        Lw = Lw.groupby(level=0).first()
    elif agg == "given":
        pass
    else:  # pragma: no cover
        raise ValueError(f"Unsupported agg: {agg}")

    if not isinstance(Lw.index, pd.DatetimeIndex):
        Lw.index = pd.to_datetime(Lw.index)
    Lw = Lw.sort_index()
    return Lw


def build_alpha_hac_splits_v2(
    R: pd.DataFrame,
    labels_long: pl.DataFrame | pd.DataFrame,
    horizons: Iterable[int],
    lags: Iterable[int],
    *,
    hac_lags: int = 5,
    target_universe: str = "US_EQ",
    train_frac: float = 0.6,
    val_frac: float = 0.2,
    data_freq: str | None = None,
    label_agg: Literal["mode", "first", "given"] = "mode",
    method: Literal["statsmodels", "numpy"] = "statsmodels",
    regression: Literal["single", "multi"] = "single",
    multi_drop: str | int = "other",
    n_jobs: int = 1,
) -> pl.DataFrame:
    """Compute HAC t-stats, p-values and IR per (factor, model, regime, horizon, lag) for train/val/test.

    - R: DataFrame of factor returns, datetime index.
    - labels_long: long frame with columns (time, asset_id, model_name, regime_code)
    - horizons: iterable of horizons for future_sum.
    - lags: iterable of indicator lags applied to regime labels.
    - label_agg: how to aggregate labels across assets at each time per model.
    - method: 'statsmodels' (authoritative) or 'numpy' (faster; may differ numerically if not carefully matched).
    """
    if not isinstance(R.index, pd.DatetimeIndex):
        R = R.copy()
        R.index = pd.to_datetime(R.index)
    R = R.sort_index()

    # prepare label table
    Lw = _labels_time_by_model(labels_long, agg=label_agg)

    idx = R.index
    T = len(idx)
    n_tr = int(train_frac * T)
    n_va = int(val_frac * T)
    te0 = n_tr + n_va
    tr_idx, va_idx, te_idx = idx[:n_tr], idx[n_tr:te0], idx[te0:]

    def split_info(which: str):
        if which == "train":
            a, b = tr_idx.min(), tr_idx.max()
        elif which == "val":
            a, b = va_idx.min(), va_idx.max()
        else:
            a, b = te_idx.min(), te_idx.max()
        return str(pd.to_datetime(a)), str(pd.to_datetime(b))

    def _ols_hac_single(y: pd.Series, x: pd.Series):
        """Single dummy OLS with HAC; returns coef, t, p, mu_pred_when_x1, ir, t_last."""
        y = pd.Series(y).astype(float)
        x = pd.Series(x).astype(float)
        df = (
            pd.concat([y.rename("y"), x.rename("x")], axis=1)
            .replace([np.inf, -np.inf], np.nan)
            .dropna()
        )
        if df.shape[0] < max(50, 7) or df["x"].sum() < 5:
            return None
        if method == "statsmodels":
            if sm is None:
                raise RuntimeError("statsmodels not available")
            Xc = sm.add_constant(df[["x"]], has_constant="add")
            res = sm.OLS(df["y"], Xc, missing="drop").fit(
                cov_type="HAC", cov_kwds={"maxlags": int(hac_lags)}
            )
            coef = float(res.params.get("x", np.nan))
            tval = float(res.tvalues.get("x", np.nan))
            pval = float(res.pvalues.get("x", np.nan))
            alpha = float(res.params.get("const", np.nan))
        else:
            # Lightweight NW-HAC using Bartlett kernel; note: may not be numerically identical to statsmodels
            yv = df["y"].values.astype(float)
            xv = df["x"].values.astype(float)
            n = len(yv)
            X = np.column_stack([np.ones(n), xv])
            XtX = X.T @ X
            beta = np.linalg.solve(XtX, X.T @ yv)
            resid = yv - X @ beta
            Z = resid[:, None] * X
            S = (Z.T @ Z) / n
            L = int(hac_lags)
            for k in range(1, L + 1):
                w = 1.0 - k / (L + 1.0)
                Gk = (Z[k:].T @ Z[:-k]) / n
                S += w * (Gk + Gk.T)
            Q = XtX / n
            Qinv = np.linalg.inv(Q)
            cov = Qinv @ S @ Qinv
            se = np.sqrt(np.diag(cov))
            coef = float(beta[1])
            tval = float(coef / se[1]) if se[1] > 0 else np.nan
            from scipy.stats import norm  # local import
            pval = float(2 * norm.sf(abs(tval))) if math.isfinite(tval) else np.nan
            alpha = float(beta[0])

        # strategy IR on the same sample (using only target dummy exposure)
        w = np.sign(coef) * df["x"].values
        r_strat = w * df["y"].values
        mu = float(np.nanmean(r_strat))
        sd = float(np.nanstd(r_strat, ddof=1))
        sr = mu / sd if sd > 0 else np.nan
        ir = float(sr * (252.0 ** 0.5)) if sr == sr else np.nan
        t_last = str(pd.to_datetime(df.index.max()))
        mu_pred_when_x1 = alpha + coef
        return coef, tval, pval, mu_pred_when_x1, ir, t_last

    def _choose_drop(regimes_list: list[int], target: int) -> int:
        if isinstance(multi_drop, int):
            return int(multi_drop) if int(multi_drop) in regimes_list else regimes_list[0]
        if multi_drop in ("min", "first"):
            return regimes_list[0]
        # "other": pick the next regime in sorted order (wrap around)
        i = regimes_list.index(target)
        return regimes_list[(i + 1) % len(regimes_list)]

    def _ols_hac_multi(y: pd.Series, dummies: pd.DataFrame, target_col: str):
        """Multi-dummy OLS (drop one regime), HAC; report stats for target_col.

        dummies: columns are active regime dummy columns (after drop), all aligned to y.
        """
        y = pd.Series(y).astype(float)
        X = dummies.astype(float)
        df = (
            pd.concat([y.rename("y"), X], axis=1)
            .replace([np.inf, -np.inf], np.nan)
            .dropna()
        )
        if df.shape[0] < max(50, 7) or df[target_col].sum() < 5:
            return None
        if method == "statsmodels":
            if sm is None:
                raise RuntimeError("statsmodels not available")
            Xc = sm.add_constant(df[X.columns], has_constant="add")
            res = sm.OLS(df["y"], Xc, missing="drop").fit(
                cov_type="HAC", cov_kwds={"maxlags": int(hac_lags)}
            )
            coef = float(res.params.get(target_col, np.nan))
            tval = float(res.tvalues.get(target_col, np.nan))
            pval = float(res.pvalues.get(target_col, np.nan))
            alpha = float(res.params.get("const", np.nan))
        else:  # pragma: no cover (keep for parity)
            # Fall back to statsmodels path for multi if numpy requested
            if sm is None:
                raise RuntimeError("statsmodels not available")
            Xc = sm.add_constant(df[X.columns], has_constant="add")
            res = sm.OLS(df["y"], Xc, missing="drop").fit(
                cov_type="HAC", cov_kwds={"maxlags": int(hac_lags)}
            )
            coef = float(res.params.get(target_col, np.nan))
            tval = float(res.tvalues.get(target_col, np.nan))
            pval = float(res.pvalues.get(target_col, np.nan))
            alpha = float(res.params.get("const", np.nan))

        # Strategy IR uses target exposure only
        w = np.sign(coef) * df[target_col].values
        r_strat = w * df["y"].values
        mu = float(np.nanmean(r_strat))
        sd = float(np.nanstd(r_strat, ddof=1))
        sr = mu / sd if sd > 0 else np.nan
        ir = float(sr * (252.0 ** 0.5)) if sr == sr else np.nan
        t_last = str(pd.to_datetime(df.index.max()))
        mu_pred_when_x1 = alpha + coef
        return coef, tval, pval, mu_pred_when_x1, ir, t_last

    # One job per (factor, horizon) to reduce pickling overhead
    def _process_factor_h(fac: str, h: int) -> list[dict]:
        rows_local: list[dict] = []
        r = R[fac].astype(float)
        y_full = future_sum(r, int(h)).dropna()
        if y_full.empty:
            return rows_local
        Lh = Lw.reindex(y_full.index)
        for m in Lh.columns:
            lab = pd.to_numeric(Lh[m], errors="coerce")
            if lab.dropna().empty:
                continue
            regimes = sorted({int(v) for v in pd.unique(lab.dropna())})
            for rid in regimes:
                for LAG in lags:
                    if regression == "single":
                        x_full = (lab.shift(int(LAG)) == rid).astype(float)
                    else:
                        d_all = {rr: (lab.shift(int(LAG)) == rr).astype(float) for rr in regimes}
                        drop_r = _choose_drop(regimes, rid)
                        cols = [f"reg_{rr}" for rr in regimes if rr != drop_r]
                        X_multi = pd.DataFrame({f"reg_{rr}": d_all[rr] for rr in regimes if rr != drop_r})
                        target_col = f"reg_{rid}" if rid != drop_r else None
                    for split_name, sidx in (("train", tr_idx), ("val", va_idx), ("test", te_idx)):
                        y = y_full.reindex(sidx).dropna()
                        if y.empty:
                            continue
                        if regression == "single":
                            x = x_full.reindex(y.index)
                            res = _ols_hac_single(y, x)
                            if res is None:
                                continue
                            coef, tval, pval, mu_pred, ir, t_last = res
                        else:
                            if target_col is None:
                                continue
                            Xm = X_multi.reindex(y.index)
                            res = _ols_hac_multi(y, Xm, target_col)
                            if res is None:
                                continue
                            coef, tval, pval, mu_pred, ir, t_last = res
                        ds, de = split_info(split_name)
                        rows_local += [
                            dict(split=split_name, data_freq=data_freq or "NA", date_start=ds, date_end=de, time=t_last,
                                 model_id=f"reglab_{m}", model_version_id="v1", model_owner_id="regimes_lab", hyper_id="h0",
                                 target_universe=target_universe, target_name=fac, regime_id=str(rid), horizon=int(h), lag=int(LAG),
                                 metric_name="t_stat_hac", metric_value=float(tval)),
                            dict(split=split_name, data_freq=data_freq or "NA", date_start=ds, date_end=de, time=t_last,
                                 model_id=f"reglab_{m}", model_version_id="v1", model_owner_id="regimes_lab", hyper_id="h0",
                                 target_universe=target_universe, target_name=fac, regime_id=str(rid), horizon=int(h), lag=int(LAG),
                                 metric_name="p_val_hac", metric_value=float(pval)),
                            dict(split=split_name, data_freq=data_freq or "NA", date_start=ds, date_end=de, time=t_last,
                                 model_id=f"reglab_{m}", model_version_id="v1", model_owner_id="regimes_lab", hyper_id="h0",
                                 target_universe=target_universe, target_name=fac, regime_id=str(rid), horizon=int(h), lag=int(LAG),
                                 metric_name="ols_coef", metric_value=float(coef)),
                            dict(split=split_name, data_freq=data_freq or "NA", date_start=ds, date_end=de, time=t_last,
                                 model_id=f"reglab_{m}", model_version_id="v1", model_owner_id="regimes_lab", hyper_id="h0",
                                 target_universe=target_universe, target_name=fac, regime_id=str(rid), horizon=int(h), lag=int(LAG),
                                 metric_name="ols_mu", metric_value=float(mu_pred)),
                            dict(split=split_name, data_freq=data_freq or "NA", date_start=ds, date_end=de, time=t_last,
                                 model_id=f"reglab_{m}", model_version_id="v1", model_owner_id="regimes_lab", hyper_id="h0",
                                 target_universe=target_universe, target_name=fac, regime_id=str(rid), horizon=int(h), lag=int(LAG),
                                 metric_name="ir", metric_value=float(ir)),
                        ]
        return rows_local

    # Run in parallel over (factor, horizon)
    tasks = [(fac, int(h)) for fac in R.columns for h in horizons]
    rows: list[dict] = []
    if n_jobs and n_jobs != 1:
        try:
            from joblib import Parallel, delayed  # type: ignore
            parts = Parallel(n_jobs=n_jobs, prefer="processes")(
                delayed(_process_factor_h)(fac, h) for fac, h in tasks
            )
            for p in parts:
                rows.extend(p)
        except Exception:
            # Fallback to sequential if joblib unavailable or errors
            for fac, h in tasks:
                rows.extend(_process_factor_h(fac, h))
    else:
        for fac, h in tasks:
            rows.extend(_process_factor_h(fac, h))

    return pl.from_pandas(pd.DataFrame(rows))
