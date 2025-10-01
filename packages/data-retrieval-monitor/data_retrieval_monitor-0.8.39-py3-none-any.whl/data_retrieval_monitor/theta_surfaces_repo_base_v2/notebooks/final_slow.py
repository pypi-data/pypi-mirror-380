# Setup imports and sys.path

from __future__ import annotations
import sys, pathlib as plib
root = plib.Path('__file__').resolve().parents[3]
sys.path.insert(0, str(root / 'src'))

import numpy as np, pandas as pd, polars as pl
import statsmodels.api as sm
from analytics.regimes_lab.data import prepare as rl_prepare
from analytics.regimes_lab.configs import TRAIN_FRAC, VAL_FRAC
from analytics.theta_surfaces_repo_base_v2.model_zoo.regimes_lab_bridge import build_labels_regimes_lab
from analytics.theta_surfaces_repo_base_v2.blocks.persist import save_parquet_with_meta
import plotly.graph_objects as go
import plotly.io as pio

from typing import Dict, List, Tuple, Iterable, Optional

# Load dataset (returns and indicators)
R, IND = rl_prepare()
R = R.copy(); IND = IND.copy()
R.index = pd.to_datetime(R.index); IND.index = pd.to_datetime(IND.index)
idx = R.index
# Compute data frequency
if len(idx) >= 2:
    dt_med = pd.Series(idx).diff().median()
    mins = dt_med.total_seconds()/60.0 if pd.notna(dt_med) else None
    if mins is None:
        data_freq = 'NA'
    elif abs(mins - 1440) < 1e-6:
        data_freq = '1D'
    elif abs(mins - 390) < 10:
        data_freq = '6.5H'
    else:
        data_freq = f'{int(mins)}m'
else:
    data_freq = 'NA'
# Split bounds (train/val/test)
T = len(idx)
n_tr = int(TRAIN_FRAC * T)
n_va = int(VAL_FRAC * T)
te0 = n_tr + n_va
tr_idx = idx[:n_tr]
va_idx = idx[n_tr:te0]
te_idx = idx[te0:]
print('Data frequency:', data_freq)
print('TRAIN:', (tr_idx.min(), tr_idx.max()), 'n=', len(tr_idx))
print('VALIDATION:', (va_idx.min(), va_idx.max()), 'n=', len(va_idx))
print('TEST:', (te_idx.min(), te_idx.max()), 'n=', len(te_idx))


# Build regimes labels (long) for all models on IND
df_lbl = pl.from_pandas(IND.reset_index().rename(columns={'index':'time'}))
df_lbl = df_lbl.with_columns(pl.lit('GLOBAL').alias('asset_id'))
labels = build_labels_regimes_lab(df=df_lbl, time_col='time', feature_cols=list(IND.columns), asset_col='asset_id', split_tag='with_splits')
print('Labels rows:', labels.height)
labels.head(10)


# ==============================
# Multi-OLS HAC (fast) pipeline
# ==============================


# ---------- helpers ----------
def forward_sum(y: pd.Series, H: int) -> pd.Series:
    """Rolling H-step forward sum (overlapping)."""
    v = pd.to_numeric(y, errors="coerce").values.astype(float)
    if H <= 1:
        return pd.Series(v, index=y.index)
    s = np.cumsum(v)
    out = s[H-1:] - np.r_[0.0, s[:-H]]
    return pd.Series(out, index=y.index[H-1:])

def build_label_panel_no_agg(labels_long: pl.DataFrame, full_index: pd.DatetimeIndex) -> pd.DataFrame:
    """
    One regime per (time, model). Forward-fill across time to avoid all-NaN after lag/reindex.
    """
    if labels_long is None or labels_long.is_empty():
        raise ValueError("labels_long is empty.")
    L = labels_long.select(['time','model_name','regime_code']).to_pandas().copy()
    L['time'] = pd.to_datetime(L['time'])
    # one row per (time, model)
    dup = L.duplicated(['time','model_name'], keep=False)
    if dup.any():
        # In case there are duplicates, take the *mode* per (time, model) to collapse.
        L = (L.groupby(['time','model_name'])['regime_code']
               .agg(lambda s: pd.Series(s).mode().iloc[0] if not pd.Series(s).mode().empty else np.nan)
               .reset_index())
    Lw = L.pivot(index='time', columns='model_name', values='regime_code').sort_index()
    Lw = Lw.apply(pd.to_numeric, errors='coerce')
    # Align to full returns index and forward-fill so shifted labels aren't all NaN
    Lw = Lw.reindex(pd.Index(full_index, name='time')).ffill()
    return Lw


def split_indices(idx: pd.DatetimeIndex, TRAIN_FRAC: float, VAL_FRAC: float):
    T = len(idx)
    n_tr = int(TRAIN_FRAC*T)
    n_va = int(VAL_FRAC*T)
    te0  = n_tr + n_va
    return idx[:n_tr], idx[n_tr:te0], idx[te0:]

def split_info(which, tr_idx, va_idx, te_idx):
    if which=='train': a,b = tr_idx.min(), tr_idx.max()
    elif which=='val': a,b = va_idx.min(), va_idx.max()
    else: a,b = te_idx.min(), te_idx.max()
    return str(pd.to_datetime(a)), str(pd.to_datetime(b))
def nw_maxlags(T: int, H: int, hac_lags: int):
    rule = int(np.floor(4 * (max(T,1)/100.0)**(2.0/9.0)))
    return max(int(hac_lags), int(H)-1, rule)

def fit_hac(y: pd.Series, X: pd.DataFrame, H: int, hac_lags: int):
    maxlags = nw_maxlags(len(y), int(H), int(hac_lags))
    return sm.OLS(y, X, missing='drop').fit(
        cov_type='HAC',
        cov_kwds={'maxlags': maxlags, 'use_correction': True},
    )

# ---------- design matrix ----------
def make_multi_dummy_block(labL: pd.Series, regimes: List[int], baseline: Optional[int]) -> Tuple[pd.DataFrame, Dict[int, Optional[str]]]:
    """Dummies for a single model; drop baseline; return (block, rid->name or None for baseline)."""
    v = pd.to_numeric(labL, errors='coerce')
    name_by_rid: Dict[int, Optional[str]] = {}
    cols: List[pd.Series] = []
    if not regimes:
        return pd.DataFrame(index=labL.index), {}
    if baseline is None:
        baseline = min(regimes)
    for rid in regimes:
        if rid == baseline:
            name_by_rid[rid] = None
        else:
            nm = f"R{rid}"
            name_by_rid[rid] = nm
            cols.append((v == rid).astype(float).rename(nm))
    X = pd.concat(cols, axis=1) if cols else pd.DataFrame(index=labL.index)
    X = X.fillna(0.0)
    return X, name_by_rid

def build_full_design(Lh: pd.DataFrame, lag: int) -> Tuple[pd.DataFrame, Dict[str, Dict[int, Optional[str]]]]:
    """All (model, regime) dummies (except baseline per model) + const."""
    Llag = Lh.shift(int(lag))
    X_blocks = []
    name_map: Dict[str, Dict[int, Optional[str]]] = {}
    for m in Llag.columns:
        s = pd.to_numeric(Llag[m], errors='coerce')
        regs = sorted(v for v in pd.unique(s.dropna()))
        if not regs:
            continue
        Xb, nm = make_multi_dummy_block(s, regs, baseline=min(regs))
        name_map[m] = nm  # keeps baseline entry even if block has zero cols
        if Xb.shape[1] > 0:
            Xb.columns = [f"{m}|{c}" for c in Xb.columns]
            X_blocks.append(Xb)
    X_full = pd.concat(X_blocks, axis=1) if X_blocks else pd.DataFrame(index=Lh.index)
    X_full = sm.add_constant(X_full, has_constant='add').fillna(0.0)
    return X_full, name_map

def split_indices(idx: pd.DatetimeIndex, TRAIN_FRAC: float, VAL_FRAC: float):
    T = len(idx)
    n_tr = int(TRAIN_FRAC*T)
    n_va = int(VAL_FRAC*T)
    te0  = n_tr + n_va
    return idx[:n_tr], idx[n_tr:te0], idx[te0:]

def split_info(which, tr_idx, va_idx, te_idx):
    if which=='train': a,b = tr_idx.min(), tr_idx.max()
    elif which=='val': a,b = va_idx.min(), va_idx.max()
    else: a,b = te_idx.min(), te_idx.max()
    return str(pd.to_datetime(a)), str(pd.to_datetime(b))

def nw_maxlags(T: int, H: int, hac_lags: int):
    # a robust, safe choice that scales; also respects overlap (H-1)
    rule = int(np.floor(4 * (max(T,1)/100.0)**(2.0/9.0)))
    return max(int(hac_lags), int(H)-1, rule)

def fit_hac(y: pd.Series, X: pd.DataFrame, H: int, hac_lags: int):
    maxlags = nw_maxlags(len(y), int(H), int(hac_lags))
    return sm.OLS(y, X, missing='drop').fit(
        cov_type='HAC',
        cov_kwds={'maxlags': maxlags, 'use_correction': True},
    )

# ---------- design matrix ----------
def make_multi_dummy_block(labL: pd.Series, regimes: List[int], baseline: Optional[int]) -> Tuple[pd.DataFrame, Dict[int, Optional[str]]]:
    """
    Build dummy block for a single model with given lagged labels `labL`.
    Baseline regime is dropped (None in name map). Returns (X_block, name_by_rid).
    """
    # ensure numeric int regime codes
    v = pd.to_numeric(labL, errors='coerce')
    name_by_rid: Dict[int, Optional[str]] = {}
    cols: List[pd.Series] = []
    if len(regimes) == 0:
        return pd.DataFrame(index=labL.index), {}
    if baseline is None:
        # drop minimum regime id as baseline by default
        baseline = min(regimes)
    for rid in regimes:
        if rid == baseline:
            name_by_rid[rid] = None
            continue
        name = f"R{rid}"
        name_by_rid[rid] = name
        cols.append((v == rid).astype(float).rename(name))
    if cols:
        X = pd.concat(cols, axis=1).fillna(0.0)
    else:
        X = pd.DataFrame(index=labL.index)
    return X, name_by_rid

def build_full_design(
    Lh: pd.DataFrame,                # time × model (int regimes)
    lag: int,
    scope: str = "within_model",     # 'within_model' or 'across_models'
) -> Tuple[pd.DataFrame, Dict[str, Dict[int, Optional[str]]]]:
    """
    Build a *full* multi-OLS design matrix with all dummies to be available in one shot.
    Returns:
      X_full: DataFrame with columns "{model}|{Rk}" excluding baselines, index aligned to Lh.index
      name_map: model -> {rid -> local_name or None if baseline}
    """
    assert scope in ("within_model", "across_models")
    # lag labels
    Llag = Lh.shift(int(lag))
    X_blocks = []
    name_map: Dict[str, Dict[int, Optional[str]]] = {}
    for m in Llag.columns:
        s = pd.to_numeric(Llag[m], errors='coerce')
        regs = sorted(v for v in pd.unique(s.dropna()))
        if not regs:
            continue
        # baseline: within each model, drop min(regime)
        Xb, nm = make_multi_dummy_block(s, regs, baseline=min(regs))
        name_map[m] = nm
        if Xb.shape[1] > 0:
            Xb.columns = [f"{m}|{c}" for c in Xb.columns]
            X_blocks.append(Xb)
    X_full = pd.concat(X_blocks, axis=1) if X_blocks else pd.DataFrame(index=Lh.index)
    X_full = sm.add_constant(X_full, has_constant='add')
    return X_full.fillna(0.0), name_map

# ---------- metrics emission ----------
def add_metric(rows: List[dict], base: dict, name: str, value: float):
    rows.append({**base, "metric_name": name, "metric_value": float(value) if pd.notna(value) else np.nan})

def per_regime_effects_from_full_fit(res, model: str, rid: int, name_map_model: Dict[int, Optional[str]]) -> Tuple[float, float, float, float]:
    name = name_map_model.get(rid, None)
    params = res.params; tvals = res.tvalues; pvals = res.pvalues
    const  = float(params.get("const", np.nan))
    if name is None:
        # baseline regime: effect 0; μ = const
        return 0.0, np.nan, np.nan, const
    full_name = f"{model}|{name}"
    beta = float(params.get(full_name, np.nan))
    t    = float(tvals.get(full_name, np.nan))
    p    = float(pvals.get(full_name, np.nan))
    mu   = const + beta
    return beta, t, p, mu

# ---------- main ----------
def build_alpha_hac_splits_multi_fast(
    R: pd.DataFrame,
    labels_long: pl.DataFrame,
    horizons: Iterable[int],
    lags: Iterable[int],
    *,
    TRAIN_FRAC: float = 0.6,
    VAL_FRAC: float = 0.2,
    hac_lags: int = 5,
    data_freq: str = "1D",
    target_universe: str = "US_EQ",
    emit_single: bool = False,         # off by default
    min_obs: int = 50,
    min_hits: int = 5,
    debug: bool = True,
) -> pl.DataFrame:
    """
    For each (factor, H, L, split) fit ONE HAC-OLS with *all* model-regime dummies (minus baselines).
    Now:
      • labels are forward-filled before alignment (so lag doesn’t blank everything),
      • we allow a constant-only fit (so you still get μ for baseline regimes),
      • we keep the ≥5 “ones” guard only when non-const dummies exist.
    """
    rows: List[dict] = []

    # (A) strict per-model panel, forward-filled on the full R.index
    Lw_all = build_label_panel_no_agg(labels_long, full_index=R.index)

    for fac in R.columns:
        r = pd.to_numeric(R[fac], errors='coerce')
        idx = r.index
        tr_idx, va_idx, te_idx = split_indices(idx, TRAIN_FRAC, VAL_FRAC)

        if debug:
            print(f"\n[MULTI] Factor={fac}")
        for H in horizons:
            y_full = forward_sum(r, int(H)).dropna()
            # align labels to y_full times (already ffilled on full index)
            Lh = Lw_all.reindex(y_full.index)

            for LAG in lags:
                X_full, name_map = build_full_design(Lh, lag=int(LAG))
                if debug:
                    # quick visibility: how many models/regimes appear after shift?
                    obs = {m: sorted(k for k in name_map[m].keys()) for m in name_map}
                    print(f"  H={H}, L={LAG}: models={list(obs.keys())}")

                for split_name, sidx in (('train', tr_idx), ('val', va_idx), ('test', te_idx)):
                    y = y_full.reindex(sidx).dropna()
                    if y.empty:
                        continue
                    Xs = X_full.reindex(y.index).fillna(0.0)

                    has_nonconst = (Xs.shape[1] > 1)
                    k = Xs.shape[1]
                    if len(y) < max(min_obs, (k + 5 if has_nonconst else min_obs)):
                        # Not enough observations
                        continue

                    # Guard on hits only when we actually have dummy columns
                    if has_nonconst:
                        ones_total = float(Xs.drop(columns=['const'], errors='ignore').sum().sum())
                        if ones_total < min_hits:
                            # too few activated dummies across all columns
                            continue

                    try:
                        res = fit_hac(y, Xs, H, hac_lags)
                    except Exception:
                        continue

                    ds, de = split_info(split_name, tr_idx, va_idx, te_idx)
                    t_last = str(pd.to_datetime(y.index.max()))

                    # Emit per-model regimes (including baseline via name_map)
                    for m, rid_map in name_map.items():
                        for rid in sorted(rid_map.keys()):
                            beta, t, p, mu = per_regime_effects_from_full_fit(res, m, rid, rid_map)
                            base = dict(
                                split=split_name, data_freq=data_freq, date_start=ds, date_end=de, time=t_last,
                                model_id=f"reglab_{m}", model_version_id='v1', model_owner_id='regimes_lab', hyper_id='h0',
                                target_universe=target_universe, target_name=fac, regime_id=str(rid),
                                horizon=int(H), lag=int(LAG),
                            )
                            add_metric(rows, base, "beta_multi",        beta)
                            add_metric(rows, base, "mu_multi",          mu)
                            add_metric(rows, base, "t_stat_hac_multi",  t)
                            add_metric(rows, base, "p_val_hac_multi",   p)

                    # Optionally (off by default) emit single-dummy legacy stats here…
                    if emit_single and has_nonconst:
                        for m in Lh.columns:
                            s_lab = pd.to_numeric(Lh[m], errors='coerce').shift(int(LAG))
                            regs = sorted(v for v in pd.unique(s_lab.dropna()))
                            if not regs:
                                continue
                            for rid in regs:
                                x_full = (s_lab == rid).astype(float)
                                Xs1 = pd.concat([pd.Series(1.0, index=y.index, name="const"),
                                                 x_full.reindex(y.index).fillna(0.0).rename("x")], axis=1)
                                if Xs1['x'].sum() < min_hits:
                                    continue
                                try:
                                    res1 = fit_hac(y, Xs1, H, hac_lags)
                                except Exception:
                                    continue
                                coef = float(res1.params.get('x', np.nan))
                                t1   = float(res1.tvalues.get('x', np.nan))
                                p1   = float(res1.pvalues.get('x', np.nan))
                                mu1  = float(res1.params.get('const', np.nan) + coef)

                                # IR (same formula as before)
                                w = np.sign(coef) * Xs1['x'].values
                                r_strat = w * y.values
                                mu_sr = float(np.nanmean(r_strat))
                                sd_sr = float(np.nanstd(r_strat, ddof=1))
                                sr = mu_sr / sd_sr if sd_sr>0 else np.nan
                                ir = float(sr * np.sqrt(252.0)) if pd.notna(sr) else np.nan

                                base = dict(
                                    split=split_name, data_freq=data_freq, date_start=ds, date_end=de, time=t_last,
                                    model_id=f"reglab_{m}", model_version_id='v1', model_owner_id='regimes_lab', hyper_id='h0',
                                    target_universe=target_universe, target_name=fac, regime_id=str(rid),
                                    horizon=int(H), lag=int(LAG),
                                )
                                add_metric(rows, base, "t_stat_hac", t1)
                                add_metric(rows, base, "p_val_hac",  p1)
                                add_metric(rows, base, "beta",       coef)
                                add_metric(rows, base, "mu_single",  mu1)
                                add_metric(rows, base, "ir",         ir)

    return pl.from_pandas(pd.DataFrame(rows))


# Build alpha (HAC) with splits

horizons = [5, 10, 20]
lags = [1, 2, 5]

alpha_split = build_alpha_hac_splits_multi_fast(
    R, labels, horizons, lags,
    hac_lags=5,
    target_universe='US_EQ',
    emit_single=False,   # keep False so we don't double-compute legacy stuff
    min_obs=50,
    min_hits=5,
    debug=True
)

# -*- coding: utf-8 -*-

# ========== Imports & Path ==========
import sys, pathlib as plib, re, json
from typing import Dict, Tuple, List, Iterable, Optional

root = plib.Path('__file__').resolve().parents[3]
sys.path.insert(0, str(root / 'src'))



from analytics.regimes_lab.data import prepare as rl_prepare
from analytics.regimes_lab.configs import TRAIN_FRAC, VAL_FRAC
from analytics.theta_surfaces_repo_base_v2.model_zoo.regimes_lab_bridge import build_labels_regimes_lab

# ========== Data ==========
R, IND = rl_prepare()
R = R.copy(); IND = IND.copy()
R.index = pd.to_datetime(R.index); IND.index = pd.to_datetime(IND.index)
idx = R.index

# Frequency & splits
if len(idx) >= 2:
    dt_med = pd.Series(idx).diff().median()
    mins = dt_med.total_seconds()/60.0 if pd.notna(dt_med) else None
    if mins is None: data_freq = 'NA'
    elif abs(mins - 1440) < 1e-6: data_freq = '1D'
    elif abs(mins - 390) < 10: data_freq = '6.5H'
    else: data_freq = f'{int(mins)}m'
else:
    data_freq = 'NA'

T = len(idx)
n_tr = int(TRAIN_FRAC * T)
n_va = int(VAL_FRAC * T)
te0 = n_tr + n_va
tr_idx, va_idx, te_idx = idx[:n_tr], idx[n_tr:te0], idx[te0:]

print("=== ENV VERSIONS ===")
print("python:", sys.version.split()[0])
try:
    import pandas, polars, plotly
    print("pandas:", pandas.__version__)
    print("polars:", polars.__version__)
    print("plotly:", plotly.__version__)
except Exception:
    pass

print("=== SPLITS ===")
print('Data frequency:', data_freq)
print('TRAIN:', (tr_idx.min(), tr_idx.max()), 'n=', len(tr_idx))
print('VALIDATION:', (va_idx.min(), va_idx.max()), 'n=', len(va_idx))
print('TEST:', (te_idx.min(), te_idx.max()), 'n=', len(te_idx))

# Labels
df_lbl = pl.from_pandas(IND.reset_index().rename(columns={'index':'time'}))
df_lbl = df_lbl.with_columns(pl.lit('GLOBAL').alias('asset_id'))
labels = build_labels_regimes_lab(df=df_lbl, time_col='time', feature_cols=list(IND.columns),
                                  asset_col='asset_id', split_tag='with_splits')
print('Labels rows:', labels.height)
print(labels.select(['time','asset_id','model_name','regime_code']).head(10))

# ========== Helpers ==========
def _norm_rid_str(v) -> str:
    try: return str(int(float(v)))
    except Exception: return str(v)

def _split_bounds(which):
    if which=='train': a,b = tr_idx.min(), tr_idx.max()
    elif which=='val': a,b = va_idx.min(), va_idx.max()
    else: a,b = te_idx.min(), te_idx.max()
    return str(pd.to_datetime(a)), str(pd.to_datetime(b))

def future_sum(y: pd.Series, h: int) -> pd.Series:
    h = int(h)
    if h <= 1: return y
    v = pd.to_numeric(y, errors='coerce').values.astype(float)
    s = np.cumsum(np.nan_to_num(v))
    out = s[h-1:] - np.r_[0.0, s[:-h]]
    return pd.Series(out, index=y.index[h-1:])

def _labels_panel_full(labels_long: pl.DataFrame, full_index: pd.DatetimeIndex) -> pd.DataFrame:
    """Pivot to time×model and forward-fill on full index so lagging doesn't nuke data."""
    L = labels_long.select(['time','model_name','regime_code']).to_pandas().copy()
    L['time'] = pd.to_datetime(L['time'])
    if L.duplicated(['time','model_name'], keep=False).any():
        L = (L.groupby(['time','model_name'])['regime_code']
               .agg(lambda s: pd.Series(s).mode().iloc[0] if not pd.Series(s).mode().empty else np.nan)
               .reset_index())
    Lw = L.pivot(index='time', columns='model_name', values='regime_code').sort_index()
    Lw = Lw.apply(pd.to_numeric, errors='coerce')
    Lw = Lw.reindex(pd.Index(full_index, name='time')).ffill()
    return Lw

# ========== Multi-OLS HAC (fast) ==========
def nw_maxlags(T: int, H: int, hac_lags: int):
    rule = int(np.floor(4 * (max(T,1)/100.0)**(2.0/9.0)))
    return max(int(hac_lags), int(H)-1, rule)

def fit_hac(y: pd.Series, X: pd.DataFrame, H: int, hac_lags: int):
    maxlags = nw_maxlags(len(y), int(H), int(hac_lags))
    return sm.OLS(y, X, missing='drop').fit(
        cov_type='HAC',
        cov_kwds={'maxlags': maxlags, 'use_correction': True},
    )

def make_block(labL: pd.Series) -> tuple[pd.DataFrame, Dict[int, Optional[str]]]:
    s = pd.to_numeric(labL, errors='coerce')
    regs = sorted(v for v in pd.unique(s.dropna()))
    name_by_rid: Dict[int, Optional[str]] = {}
    cols = []
    if not regs:
        return pd.DataFrame(index=s.index), {}
    baseline = min(regs)
    for rid in regs:
        if rid == baseline:
            name_by_rid[rid] = None
        else:
            nm = f"R{rid}"
            name_by_rid[rid] = nm
            cols.append((s == rid).astype(float).rename(nm))
    X = pd.concat(cols, axis=1) if cols else pd.DataFrame(index=s.index)
    return X.fillna(0.0), name_by_rid

def build_full_design(Lh: pd.DataFrame, lag: int):
    Llag = Lh.shift(int(lag))
    X_blocks = []; name_map: Dict[str, Dict[int, Optional[str]]] = {}
    for m in Llag.columns:
        Xb, nm = make_block(Llag[m])
        name_map[m] = nm  # keep map even if baseline-only
        if Xb.shape[1] > 0:
            Xb.columns = [f"{m}|{c}" for c in Xb.columns]
            X_blocks.append(Xb)
    X_full = pd.concat(X_blocks, axis=1) if X_blocks else pd.DataFrame(index=Lh.index)
    X_full = sm.add_constant(X_full, has_constant='add').fillna(0.0)
    return X_full, name_map

def per_regime_from_fit(res, model: str, rid: int, map_m: Dict[int, Optional[str]]):
    nm = map_m.get(rid, None)
    params, tvals, pvals = res.params, res.tvalues, res.pvalues
    const = float(params.get('const', np.nan))
    if nm is None:  # baseline
        return 0.0, np.nan, np.nan, const
    full = f"{model}|{nm}"
    beta = float(params.get(full, np.nan))
    t    = float(tvals.get(full, np.nan))
    p    = float(pvals.get(full, np.nan))
    mu   = const + beta
    return beta, t, p, mu

def add_metric(rows: List[dict], base: dict, name: str, value: float):
    rows.append({**base, "metric_name": name, "metric_value": float(value) if pd.notna(value) else np.nan})

def build_alpha_multi_hac(
    R: pd.DataFrame, labels_long: pl.DataFrame,
    horizons: Iterable[int], lags: Iterable[int],
    *, hac_lags: int = 5, min_obs: int = 50, min_hits: int = 5,
    emit_single: bool = False,  # legacy toggle
) -> pl.DataFrame:
    rows: List[dict] = []
    Lw_all = _labels_panel_full(labels_long, R.index)

    for fac in R.columns:
        r = pd.to_numeric(R[fac], errors='coerce')
        idx = r.index

        for H in horizons:
            y_full = future_sum(r, int(H)).dropna()
            Lh = Lw_all.reindex(y_full.index)

            for LAG in lags:
                X_full, name_map = build_full_design(Lh, lag=int(LAG))

                for split_name, sidx in (('train', tr_idx), ('val', va_idx), ('test', te_idx)):
                    y = y_full.reindex(sidx).dropna()
                    if y.empty: continue
                    Xs = X_full.reindex(y.index).fillna(0.0)
                    k  = Xs.shape[1]

                    # --- feasibility: allow const-only models ---
                    has_nonconst = any(c != 'const' for c in Xs.columns)
                    if has_nonconst:
                        # needs enough obs and enough "hits"
                        if len(y) < max(min_obs, k + 5): continue
                        # hits only on non-const columns
                        if Xs.drop(columns=['const'], errors='ignore').sum().sum() < min_hits: continue
                    else:
                        # const-only: just need reasonable obs to estimate intercept
                        if len(y) < max(20, 5): continue

                    try:
                        res = fit_hac(y, Xs, H, hac_lags)
                    except Exception:
                        continue

                    ds, de = _split_bounds(split_name)
                    t_last = str(pd.to_datetime(y.index.max()))
                    base_common = dict(split=split_name, data_freq=data_freq, date_start=ds, date_end=de, time=t_last,
                                       model_version_id='v1', model_owner_id='regimes_lab', hyper_id='h0',
                                       target_universe='US_EQ', target_name=fac, horizon=int(H), lag=int(LAG))

                    # per-regime emission from single full fit
                    for m, rid_map in name_map.items():
                        for rid in sorted(rid_map.keys()):
                            beta, t, p, mu = per_regime_from_fit(res, m, rid, rid_map)
                            base = dict(**base_common, model_id=f"reglab_{m}", regime_id=_norm_rid_str(rid))
                            add_metric(rows, base, "beta_multi",        beta)
                            add_metric(rows, base, "mu_multi",          mu)
                            add_metric(rows, base, "t_stat_hac_multi",  t)
                            add_metric(rows, base, "p_val_hac_multi",   p)

                    # optional legacy single-dummy
                    if emit_single and has_nonconst:
                        for m in Lh.columns:
                            lab = pd.to_numeric(Lh[m], errors='coerce').shift(int(LAG))
                            regs = sorted(v for v in pd.unique(lab.dropna()))
                            if not regs: continue
                            for rid in regs:
                                x = (lab == rid).astype(float).reindex(y.index).fillna(0.0)
                                X1 = sm.add_constant(x.rename('x'), has_constant='add')
                                if X1['x'].sum() < min_hits: continue
                                try:
                                    r1 = fit_hac(y, X1, H, hac_lags)
                                except Exception:
                                    continue
                                coef = float(r1.params.get('x', np.nan))
                                t1   = float(r1.tvalues.get('x', np.nan))
                                p1   = float(r1.pvalues.get('x', np.nan))
                                mu1  = float(r1.params.get('const', np.nan) + coef)
                                w = np.sign(coef) * X1['x'].values
                                pnl = w * y.values
                                sd = float(np.nanstd(pnl, ddof=1)); sr = (np.nanmean(pnl) / sd) if sd>0 else np.nan
                                ir = float(sr * np.sqrt(252.0)) if pd.notna(sr) else np.nan
                                base = dict(**base_common, model_id=f"reglab_{m}", regime_id=_norm_rid_str(rid))
                                add_metric(rows, base, "t_stat_hac", t1)
                                add_metric(rows, base, "p_val_hac",  p1)
                                add_metric(rows, base, "ir",         ir)

    return pl.from_pandas(pd.DataFrame(rows))

# ===== Run alpha build =====
horizons = [5, 10, 20]
lags = [1, 2, 5]
alpha_split = build_alpha_multi_hac(R, labels, horizons, lags, hac_lags=5, min_obs=40, min_hits=5, emit_single=False)
print("Alpha (split) rows:", alpha_split.height)

# ================= UI/HTML (with fixes) =================
# Filters now apply to ANY metric listed here; omit metric to not filter it.
FILTERS = {
    # examples; change freely — anything you put here will be applied
    "t_stat_hac_multi": (">=", 0.0),
    "p_val_hac_multi": ("<=", 1.01),
    # legacy examples:
    "t_stat_hac": (">=", 1.96),
    "p_val_hac": ("<=", 0.05),
    "ir": (">=", 0.10),
}

BASE_METRICS  = ["t_stat_hac", "p_val_hac", "ir"]
MULTI_METRICS = ["t_stat_hac_multi", "p_val_hac_multi", "beta_multi", "mu_multi"]
METRIC_ALIASES = {
    "t_stat_hac": "HAC t-stat (1D)",
    "p_val_hac": "HAC p-value (1D)",
    "ir": "Information Ratio",
    "t_stat_hac_multi": "HAC t-stat (Multi-OLS)",
    "p_val_hac_multi": "HAC p-value (Multi-OLS)",
    "beta_multi": "OLS Coef (Multi-OLS)",
    "mu_multi": "OLS μ (Multi-OLS)",
}
METRICS_SELECTED = MULTI_METRICS + BASE_METRICS  # rendered order

DEFAULT_MAX_ITEMS_PER_CELL = 6
ABBREV_REGLAB_PREFIX = True
METRICS_LAYOUT_COLS = "auto"
SCOPE = {"factors": None, "models": None, "regimes": None, "horizons": None, "lags": None}
TIME_FMT = "%Y-%m-%d %H:%M"; TIME_FMT_DAILY = "%Y-%m-%d"
PLOTLY_INCLUDE = "full"
SHADE_OPACITY = 0.22
SHADE_STRONG = {"0":"#d4d4d8","1":"#fde68a","2":"#bfdbfe","3":"#bbf7d0","4":"#fecaca","5":"#e9d5ff","6":"#fcd34d","7":"#c7d2fe"}
OUT_DIR = plib.Path("regimes_stats_html"); OUT_DIR.mkdir(parents=True, exist_ok=True)
FIXED_CHART_HEIGHT = 340  # keep fixed to avoid layout shifts

def _sanitize_id(s: str) -> str: return re.sub(r"[^A-Za-z0-9_]+", "_", s)
def _fmt_dt_by_freq(x, data_freq: str):
    try: ts = pd.to_datetime(x)
    except Exception: return str(x)
    return ts.strftime(TIME_FMT_DAILY if isinstance(data_freq, str) and data_freq.upper() in ("1D","D","DAILY") else TIME_FMT)
def _fmt_filters(filters: dict) -> str:
    sym = {">=":"≥",">":"›","<=":"≤","<":"‹","==":"="}
    parts = []
    for k,(op,val) in filters.items():
        vv = f"{float(val):.2f}" if isinstance(val,(int,float)) else str(val)
        parts.append(f"{METRIC_ALIASES.get(k,k)} {sym.get(op,op)} {vv}")
    return "; ".join(parts) if parts else "none"
def _fmt_scope(scope: dict) -> str:
    items = []
    for k in ["factors","models","regimes","horizons","lags"]:
        v = scope.get(k)
        if v: items.append(f"{k}={list(v)}")
    return "none" if not items else "; ".join(items)
def split2(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.when(pl.col("split").is_in(["train","val"])).then(pl.lit("trainval")).otherwise(pl.col("split")).alias("split2")
    )
def _pivot_wide(df: pl.DataFrame) -> pl.DataFrame:
    key = ["target_name","model_id","regime_id","horizon","lag","split","split2","data_freq","date_start","date_end","time"]
    try: return df.pivot(index=key, on="metric_name", values="metric_value", aggregate_function="mean")
    except TypeError: return df.pivot(index=key, columns="metric_name", values="metric_value", aggregate_function="mean")
def _apply_filters(wide: pl.DataFrame, filters: dict[str, tuple[str, float]]) -> pl.DataFrame:
    if not filters: return wide
    expr = None
    for m,(op,val) in filters.items():
        if m not in wide.columns: continue
        c = pl.col(m)
        cond = {"<=":(c<=float(val)), "<":(c<float(val)), ">=":(c>=float(val)), ">":(c>float(val)), "==":(c==float(val))}[op]
        expr = cond if expr is None else (expr & cond)
    return wide.filter(expr) if expr is not None else wide
def _scope_filter(df: pl.DataFrame, scope: dict) -> pl.DataFrame:
    out = df
    if scope.get("factors"):  out = out.filter(pl.col("target_name").is_in(scope["factors"]))
    if scope.get("models"):   out = out.filter(pl.col("model_id").is_in(scope["models"]))
    if scope.get("regimes"):  out = out.filter(pl.col("regime_id").cast(pl.Utf8).is_in([str(x) for x in scope["regimes"]]))
    if scope.get("horizons"): out = out.filter(pl.col("horizon").is_in([int(x) for x in scope["horizons"]]))
    if scope.get("lags"):     out = out.filter(pl.col("lag").is_in([int(x) for x in scope["lags"]]))
    return out

CELLLIST_CSS = """
.celllist { line-height:1.45; }
.celllist .item { margin:2px 0; }
.celllist .m { font-weight:600; color:#111827; }
.celllist .rg { color:#6b7280; margin-left:4px; }
.celllist .v { font-variant-numeric:tabular-nums; background:#eef2ff; color:#3730a3; padding:0 4px; border-radius:4px; margin-left:6px; }
.celllist .top1 .v { background:#dcfce7; color:#166534; }
"""

def _style_table(df: pd.DataFrame, title: str, subtitle: str) -> str:
    if df.empty:
        return f'<div style="font-family:Inter,Arial,sans-serif;color:#444;"><h4>{title}</h4><div style="color:#6b7280;">{subtitle}</div><em>No entries passed thresholds</em></div>'
    styler = (
        df.style
        .set_caption(f'{title}<br><span style="font-weight:400;color:#6b7280;">{subtitle}</span>')
        .set_table_styles([
            {'selector':'caption','props':'caption-side:top;font-weight:600;padding:4px 0;'},
            {'selector':'th','props':'background:#f5f7fb;color:#333;font-weight:600;padding:6px;border:1px solid #e6e9ef;'},
            {'selector':'td','props':'padding:6px;border:1px solid #e6e9ef;vertical-align:top;'},
            {'selector':'table','props':'border-collapse:collapse;font-family:Inter,Arial,sans-serif;font-size:13px;'},
        ])
        .format(escape=None)
    )
    return styler.to_html()

def _string_table(df_wide_factor_split: pl.DataFrame, metric: str) -> pd.DataFrame:
    if df_wide_factor_split.is_empty() or metric not in df_wide_factor_split.columns:
        return pd.DataFrame()
    df = df_wide_factor_split.filter(pl.col(metric).is_not_null())
    model_disp = (
        pl.when(pl.lit(ABBREV_REGLAB_PREFIX) & pl.col("model_id").str.starts_with("reglab_"))
        .then(pl.col("model_id").str.replace("^reglab_", ""))
        .otherwise(pl.col("model_id"))
    )
    entry_expr = pl.concat_str(
        [pl.lit('<div class="item"><span class="m">'), model_disp,
         pl.lit('</span> <span class="rg">R'), pl.col("regime_id").cast(pl.Utf8), pl.lit("</span>"),
         pl.lit(' <span class="v">'), pl.col(metric).round(3).cast(pl.Utf8), pl.lit("</span></div>")],
        separator=""
    ).alias("entry_html")
    asc = metric.lower().startswith("p_val")
    tmp = df.with_columns([entry_expr])
    agg = (
        tmp.group_by(["lag","horizon"])
           .agg([ pl.col("entry_html").sort_by(pl.col(metric), descending=not asc).alias("entries") ])
           .with_columns([
               pl.col("entries").list.first().str.replace('<div class="item">','<div class="item top1">').alias("top1"),
               pl.col("entries").list.slice(1).list.join("").alias("tail")
           ])
           .with_columns([ pl.concat_str([pl.lit('<div class="celllist">'), pl.col("top1"), pl.col("tail"), pl.lit("</div>")], separator="").alias("cell") ])
           .select(["lag","horizon","cell"]).sort(["lag","horizon"])
    )
    table_pl = agg.pivot(index="lag", columns="horizon", values="cell", aggregate_function="first").sort("lag")
    dfp = table_pl.to_pandas()
    if "lag" in dfp.columns: dfp = dfp.set_index("lag")
    try: cols_sorted = sorted(dfp.columns, key=lambda x: int(x))
    except Exception: cols_sorted = sorted(dfp.columns)
    dfp = dfp.reindex(cols_sorted, axis=1)
    dfp.index.name = "Lag"; dfp.columns.name = "Horizon"
    return dfp

# ---- shading + right-axis helpers ----
def _edges_from_index(idx: pd.DatetimeIndex) -> pd.DatetimeIndex:
    idx = pd.to_datetime(idx); t = idx.view("int64")
    if len(t) < 2: edges = np.array([t[0], t[0]], dtype=np.int64)
    else:
        mids = (t[:-1] + t[1:]) // 2
        left = t[0] - (mids[0] - t[0]); right = t[-1] + (t[-1] - mids[-1])
        edges = np.concatenate([[left], mids, [right]])
    return pd.to_datetime(edges)

def _labels_series_aligned(labels_long: pl.DataFrame, model_name: str, index_like: pd.DatetimeIndex) -> pd.Series:
    want = [model_name]
    if not model_name.startswith("reglab_"): want.append(f"reglab_{model_name}")
    else: want.append(model_name[7:])
    sub = (labels_long.filter(pl.col("model_name").is_in(want)).select(["time","model_name","regime_code"]).sort("time"))
    if sub.is_empty(): return pd.Series(index=index_like, dtype="object")
    for w in want:
        tmp = sub.filter(pl.col("model_name")==w).select(["time","regime_code"]).to_pandas()
        if not tmp.empty:
            tmp["time"] = pd.to_datetime(tmp["time"])
            s = tmp.dropna(subset=["regime_code"]).set_index("time")["regime_code"].astype(str).sort_index()
            return s.reindex(index_like.union(s.index)).sort_index().ffill().reindex(index_like)
    return pd.Series(index=index_like, dtype="object")

def _available_models_and_regimes(*dfs: pl.DataFrame):
    models, regimes = set(), set()
    for df in dfs:
        if df.is_empty(): continue
        for m in df.select("model_id").to_series().to_list():
            base = m[7:] if str(m).startswith("reglab_") else str(m); models.add(base)
        for r in df.select("regime_id").to_series().to_list():
            regimes.add(_norm_rid_str(r))
    return sorted(models), sorted(regimes, key=lambda x: int(re.sub(r"\D","", x) or 0))

def _available_lags_horizons(*dfs: pl.DataFrame):
    lags, hors = set(), set()
    for df in dfs:
        if df.is_empty(): continue
        lags |= set(df.select("lag").to_series().to_list())
        hors |= set(df.select("horizon").to_series().to_list())
    return sorted(int(x) for x in lags), sorted(int(x) for x in hors)

def _avg_metric_series_by_cell(factor: str, table_subset: pl.DataFrame, metric: str,
                               split_label: str, labels_long: pl.DataFrame) -> Dict[Tuple[int,int], pd.Series]:
    if not (isinstance(R, pd.DataFrame) and factor in R.columns): return {}
    idx = pd.to_datetime(R.index)
    if table_subset.is_empty() or metric not in table_subset.columns: return {}
    df = (table_subset.select(['model_id','regime_id','lag','horizon',metric])
          .filter(pl.col(metric).is_not_null()).to_pandas())
    if df.empty: return {}
    out: Dict[Tuple[int,int], pd.Series] = {}
    for _, row in df.iterrows():
        model_id = str(row['model_id'])
        base = model_id[7:] if model_id.startswith('reglab_') else model_id
        rid  = _norm_rid_str(row['regime_id'])
        lag  = int(row['lag']); hor = int(row['horizon']); val = float(row[metric])
        labs = _labels_series_aligned(labels, base, idx).shift(lag)
        mask = labs.map(lambda v: _norm_rid_str(v)==rid).astype(float).reindex(idx).fillna(0.0)
        if mask.sum() == 0: continue
        series = pd.Series(val, index=idx) * mask
        key = (lag, hor)
        out[key] = series if key not in out else pd.concat([out[key], series], axis=1).mean(axis=1)
    return out

def _avg_metric_series_by_lag(factor: str, table_subset: pl.DataFrame, metric: str,
                              split_label: str, labels_long: pl.DataFrame) -> Dict[int, pd.Series]:
    by_cell = _avg_metric_series_by_cell(factor, table_subset, metric, split_label, labels_long)
    buckets: Dict[int, List[pd.Series]] = {}
    for (lag, _h), s in by_cell.items(): buckets.setdefault(lag, []).append(s)
    out: Dict[int, pd.Series] = {}
    for lag, lst in buckets.items(): out[lag] = pd.concat(lst, axis=1).mean(axis=1)
    return out

# ---- plot + controls ----
def _build_plot_html(fac: str, sub_tv_all: pl.DataFrame, sub_te_all: pl.DataFrame, plot_id: str) -> tuple[str,str]:
    # Left axis
    if not (isinstance(R, pd.DataFrame) and fac in R.columns):
        return ('<div style="color:#6b7280;">(Plot skipped: returns missing)</div>', "")
    s = pd.to_numeric(R[fac], errors="coerce").dropna()
    if s.empty: return ('<div style="color:#6b7280;">(Plot skipped: empty series)</div>', "")
    cum = s.cumsum(); idx = cum.index; edges = _edges_from_index(idx)

    models_all, regimes_all = _available_models_and_regimes(sub_tv_all, sub_te_all)
    # (fallback for shading even if tables are empty)
    if not models_all:
        models_all = sorted(list(set(labels.select("model_name").to_series().to_list())))
    label_cache = {m: _labels_series_aligned(labels, m, idx) for m in models_all}

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=cum.index, y=cum.values, mode="lines",
        name=f"{fac} cumulative", line=dict(width=2), yaxis="y1"))
    fig.update_layout(height=FIXED_CHART_HEIGHT)

    desired_metrics = [m for m in METRICS_SELECTED if (m in sub_tv_all.columns or m in sub_te_all.columns)]
    palette = ["#065f46","#6d28d9","#1d4ed8","#047857","#7c3aed","#b45309","#0e7490","#7f1d1d"]; ci = 0

    for metric in desired_metrics:
        if metric in sub_tv_all.columns:
            lag_avg = _avg_metric_series_by_lag(fac, sub_tv_all, metric, "TrainValid", labels)
            for lag, series in sorted(lag_avg.items()):
                fig.add_trace(go.Scatter(x=series.index, y=series.values, mode="lines",
                    name=f"{metric} (TrainValid, lag={lag}, h=ALL)", line=dict(width=1.7, dash="solid", color=palette[ci%len(palette)]),
                    yaxis="y2", visible=False)); ci += 1
            cells = _avg_metric_series_by_cell(fac, sub_tv_all, metric, "TrainValid", labels)
            for (lag, h), series in sorted(cells.items()):
                fig.add_trace(go.Scatter(x=series.index, y=series.values, mode="lines",
                    name=f"{metric} (TrainValid, lag={lag}, h={h})", line=dict(width=1.3, dash="dot", color=palette[ci%len(palette)]),
                    yaxis="y2", visible=False)); ci += 1
        if metric in sub_te_all.columns:
            lag_avg = _avg_metric_series_by_lag(fac, sub_te_all, metric, "Test", labels)
            for lag, series in sorted(lag_avg.items()):
                fig.add_trace(go.Scatter(x=series.index, y=series.values, mode="lines",
                    name=f"{metric} (Test, lag={lag}, h=ALL)", line=dict(width=1.7, dash="solid", color=palette[ci%len(palette)]),
                    yaxis="y2", visible=False)); ci += 1
            cells = _avg_metric_series_by_cell(fac, sub_te_all, metric, "Test", labels)
            for (lag, h), series in sorted(cells.items()):
                fig.add_trace(go.Scatter(x=series.index, y=series.values, mode="lines",
                    name=f"{metric} (Test, lag={lag}, h={h})", line=dict(width=1.3, dash="dot", color=palette[ci%len(palette)]),
                    yaxis="y2", visible=False)); ci += 1

    fig.update_layout(
        margin=dict(l=20,r=20,t=8,b=10), template="plotly_white",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        xaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
        yaxis=dict(title="Cumulative Return", showgrid=True, gridcolor="#e5e7eb"),
        yaxis2=dict(title="Average metric level", overlaying="y", side="right", showgrid=False, autorange=True),
        shapes=[]
    )
    html = pio.to_html(fig, include_plotlyjs=PLOTLY_INCLUDE, full_html=False, div_id=plot_id)

    # Controls
    all_lags, all_hors = _available_lags_horizons(sub_tv_all, sub_te_all)
    # fallback if tables are empty
    if not all_lags:
        all_lags = lags
    if not all_hors:
        all_hors = horizons

    metric_opts = "".join(f"<option value='{m}'>{METRIC_ALIASES.get(m,m)}</option>"
                          for m in METRICS_SELECTED if (m in sub_tv_all.columns or m in sub_te_all.columns))
    # if nothing selected (e.g., all filtered out), still offer multi metrics
    if not metric_opts:
        metric_opts = "".join(f"<option value='{m}'>{METRIC_ALIASES.get(m,m)}</option>" for m in METRICS_SELECTED)

    split_opts = "<option value='TrainValid'>TrainValid</option><option value='Test'>Test</option><option value='Both'>Both</option>"
    lag_opts  = "".join(f"<label style='margin-right:6px;'><input type='checkbox' class='{plot_id}_lag' value='{L}'/> {L}</label>" for L in all_lags)
    hor_opts  = "".join(f"<label style='margin-right:6px;'><input type='checkbox' class='{plot_id}_hor' value='{H}'/> {H}</label>" for H in all_hors)
    model_opts  = "".join(f"<option value='{m}'>{m}</option>" for m in sorted(label_cache.keys()))
    regimes_all = sorted({ _norm_rid_str(v) for v in labels.select("regime_code").to_series().to_list() })
    regime_opts = "".join(f"<option value='{r}'>R{r}</option>" for r in regimes_all)

    # Build shading shapes
    shapes_by_key: Dict[str, List[dict]] = {}
    for m, labs in label_cache.items():
        if labs is None or labs.dropna().empty: continue
        rids = sorted({_norm_rid_str(x) for x in labs.dropna().unique()})
        for rid in rids:
            segs = []
            v = labs.values; cur = None
            for i in range(len(v)):
                ok = (_norm_rid_str(v[i]) == rid)
                if ok and cur is None: cur = i
                if (not ok or i==len(v)-1) and cur is not None:
                    j = i if not ok else i+1
                    segs.append((edges[cur], edges[j])); cur = None
            color = SHADE_STRONG.get(str(rid), "#e5e7eb")
            key = f"{m}: R{rid}"
            lst = []
            for (x0,x1) in segs:
                lst.append(dict(type="rect", xref="x", yref="paper",
                                x0=str(pd.to_datetime(x0)), x1=str(pd.to_datetime(x1)),
                                y0=0, y1=1, fillcolor=color, opacity=SHADE_OPACITY, line={"width":0}, layer="below"))
            shapes_by_key[key] = lst

    # Regset index for “pick from table”
    def build_regset_index(df: pl.DataFrame):
        out = {}
        for m in METRICS_SELECTED:
            if m not in df.columns: out[m] = []; continue
            sub = df.filter(pl.col(m).is_not_null())
            if sub.is_empty(): out[m] = []; continue
            rows = sub.select(["model_id","regime_id","lag","horizon"]).unique().to_pandas()
            bucket = []
            for _, r in rows.iterrows():
                model_base = str(r["model_id"])
                if model_base.startswith("reglab_"): model_base = model_base[7:]
                key = f"{model_base}: R{_norm_rid_str(r['regime_id'])}"
                bucket.append({"key": key, "lag": int(r["lag"]), "hor": int(r["horizon"])})
            out[m] = bucket
        return out
    regset_index = {"TrainValid": build_regset_index(sub_tv_all), "Test": build_regset_index(sub_te_all)}

    # Boundaries for vertical lines
    def _bound_from_split(df: pl.DataFrame):
        if df.is_empty(): return None
        a = df.select("date_start").min().item()
        try: return pd.to_datetime(a).isoformat() if a is not None else None
        except: return None
    val_ts = _bound_from_split(sub_tv_all); test_ts = _bound_from_split(sub_te_all)

    controls_html = f"""
<div style="display:flex;flex-direction:column;gap:10px;margin:6px 0 10px 0;font-size:12px;">
  <div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap;">
    <span style="font-weight:700;color:#111827;">Regime shading</span>
    <label><input type='checkbox' id='{plot_id}_master'/> Enable</label>

    <span style="margin-left:8px;">Pick from table:</span>
    <select id='{plot_id}_metric'>{metric_opts}</select>
    <select id='{plot_id}_split_simple'>{split_opts}</select>
    <label>Lag:
      <select id='{plot_id}_lag_pick'>
        <option value='ALL'>ALL</option>{"".join(f"<option value='{L}'>{L}</option>" for L in all_lags)}
      </select>
    </label>
    <label>Horizon:
      <select id='{plot_id}_hor_pick'>
        <option value='ALL'>ALL</option>{"".join(f"<option value='{H}'>{H}</option>" for H in all_hors)}
      </select>
    </label>
    <button type='button' id='{plot_id}_btn_add_from_table'>Add</button>

    <span style="margin-left:8px;">Filter:</span>
    <label>Model
      <select id='{plot_id}_model' multiple size='5' style='min-width:140px'>{model_opts}</select>
    </label>
    <label>Regime
      <select id='{plot_id}_reg' multiple size='5' style='min-width:100px'>{regime_opts}</select>
    </label>
    <button type='button' id='{plot_id}_btn_add_filtered'>Add filtered</button>
    <button type='button' id='{plot_id}_btn_clear'>Clear</button>
  </div>

  <div id='{plot_id}_chips' style="display:flex;flex-wrap:wrap;gap:8px;margin-left:2px;"></div>

  <div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap;border-top:1px solid #e5e7eb;padding-top:8px;">
    <span style="font-weight:700;color:#111827;">Right-axis lines</span>
    <label><input type='radio' name='{plot_id}_mode' value='lag' checked/> Lag averages</label>
    <label><input type='radio' name='{plot_id}_mode' value='cell'/> Cell level</label>

    <span>Metric:</span>
    <select id='{plot_id}_right_metric'>{metric_opts}</select>

    <span>Split:</span>
    <select id='{plot_id}_right_split'>{split_opts}</select>

    <span>Lags:</span> {lag_opts}
    <button type='button' id='{plot_id}_lag_all'>All</button>
    <button type='button' id='{plot_id}_lag_none'>None</button>

    <span>Horizons:</span> {hor_opts}
    <button type='button' id='{plot_id}_hor_all'>All</button>
    <button type='button' id='{plot_id}_hor_none'>None</button>

    <button type='button' id='{plot_id}_btn_preview'>Preview</button>
    <button type='button' id='{plot_id}_btn_draw'>Draw</button>
    <button type='button' id='{plot_id}_btn_clear_right'>Clear</button>
  </div>
  <div id='{plot_id}_preview' style="font-family:monospace;color:#374151;"></div>

  <div style="display:flex;gap:16px;align-items:center;flex-wrap:wrap;border-top:1px solid #e5e7eb;padding-top:8px;">
    <span style="font-weight:700;color:#111827;">Chart options</span>
    <label>Items per cell:
      <input id='{plot_id}_maxitems' type='number' min='1' step='1' value='{DEFAULT_MAX_ITEMS_PER_CELL}' style='width:64px'/>
    </label>
    <label><input type='checkbox' id='{plot_id}_showVAL'/> Show VAL boundary</label>
    <label><input type='checkbox' id='{plot_id}_showTEST'/> Show TEST boundary</label>
  </div>
</div>
"""

    # JS — includes Test fallback for empty buckets
    js = """
<script>
(function(){
  var gd = document.getElementById('%PID%'); if (!gd) return;
  var byKey = %BYKEY%;
  var regRegistry = %REGREG%;
  var allKeys = Object.keys(byKey||{});
  var chipSet = new Set();

  function $id(x){ return document.getElementById(x); }
  function qsa(s){ return document.querySelectorAll(s); }

  function renderChips(){
    var el = $id('%PID%_chips'); el.innerHTML='';
    chipSet.forEach(function(k){
      var span = document.createElement('span');
      span.style.cssText='display:inline-flex;align-items:center;gap:6px;padding:2px 8px;border:1px solid #d1d5db;border-radius:999px;background:#fff;';
      span.textContent=k;
      var btn=document.createElement('button'); btn.textContent='×';
      btn.style.cssText='margin-left:6px;border:none;background:transparent;cursor:pointer;';
      btn.onclick=function(){ chipSet.delete(k); renderChips(); applyShade(); };
      span.appendChild(btn); el.appendChild(span);
    });
  }

  function applyShade(){
    var sh = [];
    var showV = $id('%PID%_showVAL').checked;
    var showT = $id('%PID%_showTEST').checked;
    var valTs = %VAL_TS%;
    var testTs = %TEST_TS%;
    if (showV && valTs) sh.push({type:'line', x0:valTs, x1:valTs, yref:'paper', y0:0, y1:1, line:{width:2, dash:'dash', color:'#1f77b4'}});
    if (showT && testTs) sh.push({type:'line', x0:testTs, x1:testTs, yref:'paper', y0:0, y1:1, line:{width:2, dash:'dash', color:'#d62728'}});
    if ($id('%PID%_master').checked) {
      chipSet.forEach(function(k){ (byKey[k]||[]).forEach(function(s){ sh.push(s); }); });
    }
    Plotly.relayout(gd, {shapes: sh});
  }

  function addFromTable(){
    var metric = $id('%PID%_metric').value;
    var split  = $id('%PID%_split_simple').value;
    var lag    = $id('%PID%_lag_pick').value;
    var hor    = $id('%PID%_hor_pick').value;
    var bucket = (regRegistry[split] && regRegistry[split][metric]) ? regRegistry[split][metric] : [];
    var added=0;

    // Fallback: if bucket empty (e.g., TEST filtered away), add ALL keys.
    if (!bucket || !bucket.length){
      allKeys.forEach(function(k){ chipSet.add(k); added++; });
    } else {
      for (var i=0;i<bucket.length;i++){
        var b = bucket[i];
        var ok = (lag==='ALL' || String(b.lag)===String(lag));
        ok = ok && (hor==='ALL' || String(b.hor)===String(hor));
        if (ok && byKey[b.key]) { chipSet.add(b.key); added++; }
      }
    }
    if (!added) { alert('No regimes matched your pick.'); return; }
    $id('%PID%_master').checked = true; renderChips(); applyShade();
  }

  function addFiltered(){
    var mods = Array.from($id('%PID%_model').selectedOptions).map(o=>o.value);
    var regs = Array.from($id('%PID%_reg').selectedOptions).map(o=>o.value.replace(/^R/,''));
    var added=0;
    Object.keys(byKey).forEach(function(k){
      var m = /^(.+):\\s*R(\\d+)/.exec(k);
      if (!m) return;
      var mk=m[1], rk=m[2];
      var okM = (mods.length===0) || (mods.indexOf(mk)!==-1);
      var okR = (regs.length===0) || (regs.indexOf(rk)!==-1);
      if (okM && okR) { chipSet.add(k); added++; }
    });
    if (!added) { alert('No regimes matched current filters.'); return; }
    $id('%PID%_master').checked = true; renderChips(); applyShade();
  }

  function clearAll(){ chipSet.clear(); renderChips(); applyShade(); }

  function clampAll(){
    var n = parseInt($id('%PID%_maxitems').value) || %MAX_ITEMS%;
    var grid = document.getElementById('metrics-grid'); if(!grid) return;
    grid.querySelectorAll('.celllist').forEach(function(cell){
      var items = cell.querySelectorAll('.item');
      items.forEach(function(it,i){ it.style.display = (i < n) ? '' : 'none'; });
    });
  }

  function parseName(name){
    var m = /^(.*?) \\((TrainValid|Test), lag=(\\d+), h=(ALL|\\d+)\\)/.exec(name);
    if (!m) return null;
    return {metric:m[1], split:m[2], lag:parseInt(m[3]), h:m[4]};
  }
  function setVisibleBy(fn){
    var d = gd.data||[], inds=[], vis=[];
    for (var i=0;i<d.length;i++){
      var nm=d[i].name||'';
      if (nm.indexOf('%FAC% cumulative')===0){ inds.push(i); vis.push(true); continue; }
      var info = parseName(nm);
      var on = info && fn(info, nm);
      inds.push(i); vis.push(!!on);
    }
    Plotly.restyle(gd, {visible:vis}, inds);
  }
  function lineSelectAll(kind, on){
    var cls = (kind==='lag') ? '.%PID%_lag' : '.%PID%_hor';
    qsa(cls).forEach(function(cb){ cb.checked = !!on; });
  }
  function drawRight(){
    var mode   = Array.from(document.getElementsByName('%PID%_mode')).find(x=>x.checked).value;
    var metric = $id('%PID%_right_metric').value;
    var split  = $id('%PID%_right_split').value;
    var lags = Array.from(qsa('.%PID%_lag')).filter(b=>b.checked).map(b=>parseInt(b.value));
    var hors = Array.from(qsa('.%PID%_hor')).filter(b=>b.checked).map(b=>parseInt(b.value));
    if (mode==='lag' && !lags.length) { setVisibleBy(()=>false); return; }
    if (mode==='cell' && (!lags.length && !hors.length)) { setVisibleBy(()=>false); return; }
    setVisibleBy(function(info){
      var isLag = (info.h==='ALL');
      if ((mode==='lag' && !isLag) || (mode==='cell' && isLag)) return false;
      if (info.metric !== metric) return false;
      if (split!=='Both' && info.split !== split) return false;
      if (lags.length && lags.indexOf(info.lag)===-1) return false;
      if (mode==='cell' && hors.length && (info.h==='ALL' || hors.indexOf(parseInt(info.h))===-1)) return false;
      return true;
    });
  }
  function clearRight(){ setVisibleBy(()=>false); }
  function previewRight(){
    var mode   = Array.from(document.getElementsByName('%PID%_mode')).find(x=>x.checked).value;
    var metric = $id('%PID%_right_metric').value;
    var split  = $id('%PID%_right_split').value;
    var lags = Array.from(qsa('.%PID%_lag')).filter(b=>b.checked).map(b=>parseInt(b.value));
    var hors = Array.from(qsa('.%PID%_hor')).filter(b=>b.checked).map(b=>parseInt(b.value));
    var d = gd.data||[], names=[];
    for (var i=0;i<d.length;i++){
      var info = parseName(d[i].name||''); if(!info) continue;
      var isLag = (info.h==='ALL');
      if ((mode==='lag' && !isLag) || (mode==='cell' && isLag)) continue;
      if (info.metric !== metric) continue;
      if (split!=='Both' && info.split !== split) continue;
      if (lags.length && lags.indexOf(info.lag)===-1) continue;
      if (mode==='cell' && hors.length && (info.h==='ALL' || hors.indexOf(parseInt(info.h))===-1)) continue;
      names.push(d[i].name);
    }
    $id('%PID%_preview').innerHTML = names.length ? ('Will draw:<br>'+names.join('<br>')) : '(no matching series)';
  }

  // wire
  $id('%PID%_btn_add_from_table').onclick = addFromTable;
  $id('%PID%_btn_add_filtered').onclick = addFiltered;
  $id('%PID%_btn_clear').onclick = clearAll;
  $id('%PID%_maxitems').oninput = clampAll;
  $id('%PID%_lag_all').onclick = function(){ lineSelectAll('lag', true); };
  $id('%PID%_lag_none').onclick = function(){ lineSelectAll('lag', false); };
  $id('%PID%_hor_all').onclick = function(){ lineSelectAll('hor', true); };
  $id('%PID%_hor_none').onclick = function(){ lineSelectAll('hor', false); };
  $id('%PID%_btn_preview').onclick = previewRight;
  $id('%PID%_btn_draw').onclick = drawRight;
  $id('%PID%_btn_clear_right').onclick = clearRight;
  $id('%PID%_master').onchange = applyShade;
  $id('%PID%_showVAL').onchange = applyShade;
  $id('%PID%_showTEST').onchange = applyShade;

  // init
  renderChips(); clampAll(); applyShade();
})();
</script>
""".replace("%PID%", plot_id)\
   .replace("%BYKEY%", json.dumps(shapes_by_key))\
   .replace("%REGREG%", json.dumps(regset_index))\
   .replace("%VAL_TS%", json.dumps(_fmt_dt_by_freq(sub_tv_all.select('date_start').min().item(), data_freq) if not sub_tv_all.is_empty() else None))\
   .replace("%TEST_TS%", json.dumps(_fmt_dt_by_freq(sub_te_all.select('date_start').min().item(), data_freq) if not sub_te_all.is_empty() else None))\
   .replace("%MAX_ITEMS%", str(DEFAULT_MAX_ITEMS_PER_CELL))\
   .replace("%FAC%", fac)

    return html, controls_html + js

# ===== Build pages =====
# ===== Build pages =====
# ===== Build pages =====
tv = split2(alpha_split)
tv = _scope_filter(tv, SCOPE)
wide_all = _pivot_wide(tv)
wide_tv  = _apply_filters(wide_all.filter(pl.col("split2")=="trainval"), FILTERS)
wide_te  = _apply_filters(wide_all.filter(pl.col("split2")=="test"), FILTERS)

# pick metrics actually present (order by your preferred list if defined)
KNOWN_METRICS = [
    "t_stat_hac", "p_val_hac", "ir",
    "t_stat_hac_multi", "p_val_hac_multi", "beta_multi", "mu_multi"
]
present_metrics = [m for m in KNOWN_METRICS if m in wide_all.columns]
# also include any extra metrics that slipped in (e.g., custom cells)
extra_metrics = [m for m in wide_all.columns if m not in (
    ['target_name','model_id','regime_id','horizon','lag','split','split2',
     'data_freq','date_start','date_end','time'] + present_metrics)]
present_metrics += extra_metrics

# factors available
factors = sorted(set(wide_all.select("target_name").to_series().to_list()))
print("present_metrics:", present_metrics)
print("n_factors:", len(factors))

# write one HTML per factor
index_rows = []
for fac in factors:
    sub_tv_all = wide_tv.filter(pl.col("target_name")==fac)
    sub_te_all = wide_te.filter(pl.col("target_name")==fac)

    def _rng(df):
        if df.is_empty(): return ("NA","NA","NA")
        fq = df.select("data_freq").head(1).item()
        ds = _fmt_dt_by_freq(df.select("date_start").min().item(), fq)
        de = _fmt_dt_by_freq(df.select("date_end").max().item(), fq)
        return (ds, de, fq)

    ds_tv, de_tv, fq_tv = _rng(sub_tv_all)
    ds_te, de_te, fq_te = _rng(sub_te_all)

    plot_id = f"plot_{_sanitize_id(fac)}"
    plot_html, controls_html = _build_plot_html(fac, sub_tv_all, sub_te_all, plot_id)

    sections = []
    sections = []
    for metric in present_metrics:
        df_table_tv = _string_table(sub_tv_all, metric)
        df_table_te = _string_table(sub_te_all, metric)

        alias = METRIC_ALIASES.get(metric, metric)
        title_tv = f"{alias} · {fac} · TrainValid"
        title_te = f"{alias} · {fac} · Test"
        subtitle_tv = f"Freq={fq_tv} · Range=[{ds_tv} .. {de_tv}]"
        subtitle_te = f"Freq={fq_te} · Range=[{ds_te} .. {de_te}]"

        html_tv = _style_table(df_table_tv, title_tv, subtitle_tv)
        html_te = _style_table(df_table_te, title_te, subtitle_te)

        sections.append(f"""
        <div class="metric-card" id="section-{_sanitize_id(metric)}" style="min-width:0;">
          <div style="display:flex;gap:8px;align-items:flex-start;">
            <div style="flex:1;min-width:0;">{html_tv}</div>
            <div style="flex:1;min-width:0;">{html_te}</div>
          </div>
        </div>
        """)

    # layout selector
    options = ["auto","1","2","3","4"]
    sel_html = f"""
<div style="display:flex;gap:16px;align-items:center;margin:6px 0 10px 0;">
  <div style="color:#111827;font-weight:600;">Layout:</div>
  <div>Columns:
    <select id="sel-metric-cols">
      {''.join([f'<option value="{o}">{o}</option>' for o in options])}
    </select>
    <span style="color:#6b7280;">(auto = all in one row)</span>
  </div>
</div>
"""

    # save page
    out_file = OUT_DIR / f"{fac}_trainvalid_test.html"
    out_file.write_text(f"""
<html>
<head>
  <meta charset="utf-8">
  <title>Data: {fac}</title>
  <style>
    {CELLLIST_CSS}
    .grid {{ display:grid; grid-template-columns: repeat({len(present_metrics) if METRICS_LAYOUT_COLS=='auto' else METRICS_LAYOUT_COLS}, minmax(0, 1fr)); gap:12px; }}
    button {{ font-size: 12px; padding: 4px 8px; border: 1px solid #d1d5db; background:#fff; border-radius:6px; cursor:pointer; }}
    button:hover {{ background:#f3f4f6; }}
    select {{ font-size:12px; }}
  </style>
</head>
<body style="margin:20px;font-family:Inter,Arial,sans-serif;color:#111827;">
  <h2 style="margin:0 0 6px 0;">Data: {fac}</h2>
  <div style="color:#374151;margin:0 0 8px 0;">
    Filters: {_fmt_filters(FILTERS)} · Scope: {_fmt_scope(SCOPE)}
  </div>

  <!-- Plot -->
  <div style="margin:8px 0 2px 0;">
    {plot_html}
    {controls_html}
  </div>

  <!-- Layout control -->
  {sel_html}

  <!-- Metric sections grid -->
  <div id="metrics-grid" class="grid">
    {''.join(sections)}
  </div>

<script>
function setMetricsCols(n) {{
  var grid = document.getElementById("metrics-grid"); if (!grid) return;
  if (n === 'auto') {{
    var cards = grid.querySelectorAll('.metric-card');
    grid.style.gridTemplateColumns = "repeat(" + cards.length + ", minmax(0, 1fr))";
  }} else {{
    grid.style.gridTemplateColumns = "repeat(" + n + ", minmax(0, 1fr))";
  }}
}}
(function() {{
  var sel = document.getElementById("sel-metric-cols"); if (!sel) return;
  setMetricsCols("{METRICS_LAYOUT_COLS}");
  sel.value = "{METRICS_LAYOUT_COLS}";
  sel.addEventListener('change', function(){{ setMetricsCols(this.value); }});
  // clamp items initially (in case per-plot JS hasn't run yet)
  var n = {DEFAULT_MAX_ITEMS_PER_CELL};
  document.querySelectorAll('.celllist').forEach(function(cell){{
    var it = cell.querySelectorAll('.item');
    it.forEach(function(e,i){{ e.style.display=(i<n)?'':'none'; }});
  }});
}})();
</script>

</body></html>
""", encoding="utf-8")

    index_rows.append((fac, out_file.name))

# write index
links = "\n".join(
    [f'<li><a href="{name}" style="text-decoration:none;color:#2563eb;">{fac}</a></li>'
     for fac, name in index_rows]
)
(OUT_DIR / "index.html").write_text(f"""
<html><head><meta charset="utf-8"><title>Regimes Tables Index</title></head>
<body style="margin:20px;font-family:Inter,Arial,sans-serif;color:#222;">
  <h1>Regimes Tables — Consolidated</h1>
  <p>Top: cumulative factor return. Use the panel to add <b>regime shading</b> (Add / Add filtered).
     Right axis: choose mode, metric, split, lags/horizons, Preview then Draw.
     Multi-OLS metrics are available alongside legacy 1-D HAC (if computed).</p>
  <ul>{links}</ul>
</body></html>
""", encoding="utf-8")

print(f"Saved HTML to: {OUT_DIR.resolve()} (open index.html)")