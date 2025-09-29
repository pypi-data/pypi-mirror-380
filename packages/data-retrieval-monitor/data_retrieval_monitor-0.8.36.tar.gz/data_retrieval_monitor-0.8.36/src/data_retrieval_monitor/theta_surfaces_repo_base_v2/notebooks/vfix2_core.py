# -*- coding: utf-8 -*-
from __future__ import annotations

import json, re, math, pathlib as plib
from typing import Dict

import numpy as np
import pandas as pd
import polars as pl
import plotly.graph_objects as go
import plotly.io as pio

# ====================== Config / toggles ======================
ENABLE_RIGHT_AXIS_OVERLAY = True
AUTO_ADD_DAILY_OVERLAY   = True

# ====================== Knobs ======================
FILTERS = {"t_stat_hac": (">=", 1.96), "p_val_hac": ("<=", 0.05), "ir": (">=", 0.10)}

METRIC_ALIASES = {
    "t_stat_hac": "HAC t-stat (1D)",
    "p_val_hac": "HAC p-value (1D)",
    "ir": "Information Ratio",
    "beta": "OLS Coef (1D)",
    "mu_single": "OLS μ (1D)",
    "t_stat_hac_multi": "HAC t-stat (Multi-OLS)",
    "p_val_hac_multi": "HAC p-value (Multi-OLS)",
    "beta_multi": "OLS Coef (Multi-OLS)",
    "mu_multi": "OLS μ (Multi-OLS)",
    "custom_score1__t_stat_hac_multi": "Custom1 t-stat (Multi-OLS)",
    "custom_score1__p_val_hac_multi": "Custom1 p (Multi-OLS)",
    "custom_score1__beta_multi": "Custom1 Coef (Multi-OLS)",
    "custom_score1__mu_multi": "Custom1 μ (Multi-OLS)",
    "custom_score2__t_stat_hac_multi": "Custom2 t-stat (Multi-OLS)",
    "custom_score2__p_val_hac_multi": "Custom2 p (Multi-OLS)",
    "custom_score2__beta_multi": "Custom2 Coef (Multi-OLS)",
    "custom_score2__mu_multi": "Custom2 μ (Multi-OLS)",
}

METRICS_SELECTED = [
    "t_stat_hac_multi","p_val_hac_multi","beta_multi","mu_multi",
    "custom_score1__t_stat_hac_multi","custom_score1__p_val_hac_multi","custom_score1__beta_multi","custom_score1__mu_multi",
    "custom_score2__t_stat_hac_multi","custom_score2__p_val_hac_multi","custom_score2__beta_multi","custom_score2__mu_multi",
    "t_stat_hac","p_val_hac","beta","mu_single","ir",
]

DEFAULT_MAX_ITEMS_PER_CELL = 6
METRICS_LAYOUT_COLS = "auto"  # 'auto' or '1'/'2'/'3'/'4'

SCOPE = {"factors": None, "models": None, "regimes": None, "horizons": None, "lags": None}

TIME_FMT = "%Y-%m-%d %H:%M"
TIME_FMT_DAILY = "%Y-%m-%d"
PLOTLY_INCLUDE = "full"

SHADE_OPACITY = 0.22
SHADE_STRONG = {"0":"#d4d4d8","1":"#fde68a","2":"#bfdbfe","3":"#bbf7d0","4":"#fecaca","5":"#e9d5ff","6":"#c7f9cc","7":"#ffd6a5"}

OUT_DIR = plib.Path("regimes_stats_html_vfix2"); OUT_DIR.mkdir(parents=True, exist_ok=True)

# ====================== Helper utils ======================
def _sanitize_id(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]+", "_", s)

def _fmt_dt_by_freq(x, data_freq: str):
    try:
        ts = pd.to_datetime(x)
    except Exception:
        return str(x)
    if isinstance(data_freq, str) and data_freq.upper() in ("1D","D","DAILY"):
        return ts.strftime(TIME_FMT_DAILY)
    return ts.strftime(TIME_FMT)

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
        pl.when(pl.col("split").is_in(["train","val"]))
        .then(pl.lit("trainval"))
        .otherwise(pl.col("split"))
        .alias("split2")
    )

def _pivot_wide(df: pl.DataFrame) -> pl.DataFrame:
    key = ["target_name","model_id","regime_id","horizon","lag","split","split2","data_freq","date_start","date_end","time"]
    try:
        wide = df.pivot(index=key, on="metric_name", values="metric_value", aggregate_function="mean")
    except TypeError:
        wide = df.pivot(index=key, columns="metric_name", values="metric_value", aggregate_function="mean")
    if len(wide.columns) != len(set(wide.columns)):
        seen: Dict[str,int] = {}
        newcols = []
        for c in wide.columns:
            if c not in seen: seen[c]=1; newcols.append(c)
            else: seen[c]+=1; newcols.append(f"{c}__dup{seen[c]}")
        wide.columns = newcols
    return wide

def _apply_filters(wide: pl.DataFrame, filters: dict[str, tuple[str, float]]) -> pl.DataFrame:
    if not filters: return wide
    expr = None
    for m,(op,val) in filters.items():
        if m not in wide.columns:
            continue
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

def _norm_rid_to_str(x) -> str:
    if x is None: return ""
    if isinstance(x, (int, np.integer)):
        return str(int(x))
    if isinstance(x, (float, np.floating)) and not math.isnan(x):
        xi = int(round(float(x)))
        if abs(float(x) - xi) < 1e-9:
            return str(xi)
        return str(x).rstrip("0").rstrip(".")
    s = str(x).strip()
    if re.fullmatch(r"\d+(\.0+)?", s):
        return s.split(".",1)[0]
    return s

# ====================== Table builder ======================
CELLLIST_CSS = """
.celllist { line-height:1.45; }
.celllist .item { margin:2px 0; }
.celllist .m { font-weight:600; color:#111827; }
.celllist .rg { color:#6b7280; margin-left:4px; }
.celllist .v { font-variant-numeric:tabular-nums; background:#eef2ff; color:#3730a3; padding:0 4px; border-radius:4px; margin-left:6px; }
.celllist .top1 .v { background:#dcfce7; color:#166534; }
.morelink { display:block; margin-top:3px; font-size:12px; color:#2563eb; text-decoration:none; }
.morelink:hover { text-decoration:underline; }
"""

def _companions_for(metric: str) -> tuple[str|None, str|None]:
    if metric in ("t_stat_hac","p_val_hac","beta","mu_single","ir"):
        return ("beta", "mu_single")
    if metric in ("t_stat_hac_multi","p_val_hac_multi","beta_multi","mu_multi"):
        return ("beta_multi", "mu_multi")
    if "__" in metric:
        head, tail = metric.split("__", 1)
        if any(tail.startswith(x) for x in ("t_stat_hac_multi","p_val_hac_multi","beta_multi","mu_multi")):
            return (f"{head}__beta_multi", f"{head}__mu_multi")
    return (None, None)

def _string_table(df_wide_factor_split: pl.DataFrame, metric: str, idprefix: str) -> str:
    if df_wide_factor_split.is_empty() or metric not in df_wide_factor_split.columns:
        return f"<em>No entries (metric {metric} missing)</em>"

    beta_col, mu_col = _companions_for(metric)
    cols = ['model_id','regime_id','lag','horizon',metric]
    if beta_col and beta_col in df_wide_factor_split.columns:
        cols.append(beta_col)
    if mu_col and mu_col in df_wide_factor_split.columns:
        cols.append(mu_col)
    # de-duplicate while preserving order and ensure presence
    present = set(df_wide_factor_split.columns)
    dedup_cols = []
    seen = set()
    for c in cols:
        if c in present and c not in seen:
            dedup_cols.append(c)
            seen.add(c)
    dfsub = df_wide_factor_split.select(dedup_cols)
    if dfsub.is_empty():
        return "<em>No entries</em>"
    pdf = dfsub.to_pandas()
    pdf = pdf[pdf[metric].notna()]
    if pdf.empty:
        return f"<em>No entries (all values for {metric} are null)</em>"

    asc = metric.lower().startswith('p_val')
    pdf = pdf.sort_values(metric, ascending=asc)

    def fmt_model(x):
        xs = str(x)
        return xs[7:] if xs.startswith('reglab_') else xs
    def fmt_reg(x):
        return 'R'+_norm_rid_to_str(x)

    cells = {}
    for (lag,hor), g in pdf.groupby(['lag','horizon'], sort=True):
        items = []
        for _, r in g.iterrows():
            sval = float(r[metric])
            extras=[]
            if beta_col and beta_col in r and pd.notna(r[beta_col]): extras.append(f"β={float(r[beta_col]):.3f}")
            if mu_col and mu_col in r and pd.notna(r[mu_col]):       extras.append(f"μ={float(r[mu_col]):.3f}")
            extras_html = (' <span class="rg">(' + ', '.join(extras) + ')</span>') if extras else ''
            line = (
                "<div class='item'>"
                + "<span class='m'>"+fmt_model(r['model_id'])+"</span> "
                + "<span class='rg'>"+fmt_reg(r['regime_id'])+"</span> "
                + f"<span class='v'>{sval:.3f}</span>"
                + extras_html
                + "</div>"
            )
            items.append(line)
        if items:
            items[0]=items[0].replace("class='item'", "class='item top1'", 1)
            cid=f"{idprefix}_cell_{lag}_{hor}"
            cell_html = (
                f"<div class='celllist' data-expanded='0' id='{cid}'>" + ''.join(items) + "</div>"
                f"<a href='#' class='morelink' onclick=\"return toggleCellItems('{cid}', this);\">View more</a>"
            )
        else:
            cell_html = ""
        cells[(int(lag),int(hor))] = cell_html

    lags = sorted({k[0] for k in cells})
    hors = sorted({k[1] for k in cells})
    if not lags or not hors:
        return f"<em>No entries (no lag/horizon combinations found for {metric})</em>"

    html = []
    html.append("<table style='border-collapse:collapse;font-family:Inter,Arial,sans-serif;font-size:13px;'>")
    html.append("<thead><tr>")
    html.append("<th style='background:#f5f7fb;color:#333;font-weight:600;padding:6px;border:1px solid #e6e9ef;'>Lag</th>")
    for h in hors:
        html.append(f"<th style='background:#f5f7fb;color:#333;font-weight:600;padding:6px;border:1px solid #e6e9ef;'>{h}</th>")
    html.append("</tr></thead><tbody>")
    for lag in lags:
        html.append("<tr>")
        html.append(f"<td style='padding:6px;border:1px solid #e6e9ef;vertical-align:top;'>{lag}</td>")
        for h in hors:
            cell = cells.get((lag,h), "")
            html.append(f"<td style='padding:6px;border:1px solid #e6e9ef;vertical-align:top;'>{cell}</td>")
        html.append("</tr>")
    html.append("</tbody></table>")
    return "".join(html)

# ====================== Shading helpers ======================
def _edges_from_index(idx: pd.DatetimeIndex) -> pd.DatetimeIndex:
    idx = pd.to_datetime(idx); t = idx.view("int64")
    if len(t) < 2:
        edges = np.array([t[0], t[0]], dtype=np.int64)
    else:
        mids = (t[:-1] + t[1:]) // 2
        left = t[0] - (mids[0] - t[0]); right = t[-1] + (t[-1] - mids[-1])
        edges = np.concatenate([[left], mids, [right]])
    return pd.to_datetime(edges)

def _labels_series_aligned(labels_long: pl.DataFrame, model_name: str, index_like: pd.DatetimeIndex) -> pd.Series:
    if labels_long is None or labels_long.is_empty():
        return pd.Series(index=index_like, dtype="object")
    want = [model_name]
    if not model_name.startswith("reglab_"):
        want.append(f"reglab_{model_name}")
    else:
        want.append(model_name[7:])
    sub = (labels_long.filter(pl.col("model_name").is_in(want))
           .select(["time","model_name","regime_code"])
           .sort("time"))
    if sub.is_empty():
        return pd.Series(index=index_like, dtype="object")
    for w in want:
        tmp = sub.filter(pl.col("model_name")==w).select(["time","regime_code"]).to_pandas()
        if not tmp.empty:
            tmp["time"] = pd.to_datetime(tmp["time"])
            s = tmp.dropna(subset=["regime_code"]).set_index("time")["regime_code"].map(_norm_rid_to_str).sort_index()
            return s.reindex(index_like.union(s.index)).sort_index().ffill().reindex(index_like)
    return pd.Series(index=index_like, dtype="object")

def _segments_equal(series: pd.Series, want: str, edges: pd.DatetimeIndex):
    v = series.values
    segs, cur = [], None
    for i in range(len(v)):
        curv = None if (v[i] is None or (isinstance(v[i], float) and np.isnan(v[i]))) else str(v[i])
        ok = (curv == want)
        if ok:
            if cur is None: cur = i
        else:
            if cur is not None:
                segs.append((edges[cur], edges[i])); cur = None
    if cur is not None:
        segs.append((edges[cur], edges[len(v)]))
    return segs

def _available_models_and_regimes(*dfs: pl.DataFrame):
    models, regimes = set(), set()
    for df in dfs:
        if df.is_empty(): continue
        for m in df.select("model_id").to_series().to_list():
            base = m[7:] if str(m).startswith("reglab_") else str(m)
            models.add(base)
        for r in df.select("regime_id").to_series().to_list():
            regimes.add(_norm_rid_to_str(r))
    def keynum(x):
        d = re.sub(r"\D","", x)
        return int(d) if d else 0
    return sorted(models), sorted(regimes, key=keynum)

def _available_lags_horizons(*dfs: pl.DataFrame):
    lags, hors = set(), set()
    for df in dfs:
        if df.is_empty(): continue
        lags |= set(df.select("lag").to_series().to_list())
        hors |= set(df.select("horizon").to_series().to_list())
    return sorted(int(x) for x in lags), sorted(int(x) for x in hors)

# ====================== Plot + Panel ======================
def _build_plot_html(fac: str,
                     sub_tv_all: pl.DataFrame,
                     sub_te_all: pl.DataFrame,
                     plot_id: str,
                     R_df: pd.DataFrame) -> tuple[str,str,str]:
    # Left axis: cumulative return
    if not (isinstance(R_df, pd.DataFrame) and fac in R_df.columns):
        return ('<div style="color:#6b7280;">(Plot skipped: returns missing)</div>', "", "")
    s = pd.to_numeric(R_df[fac], errors="coerce").dropna()
    if s.empty:
        return ('<div style="color:#6b7280;">(Plot skipped: empty series)</div>', "", "")
    cum = s.cumsum()
    idx = cum.index
    edges = _edges_from_index(idx)

    models_all, regimes_all = _available_models_and_regimes(sub_tv_all, sub_te_all)
    label_cache = {m: _labels_series_aligned(labels, m, idx) for m in models_all}

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=cum.index, y=cum.values, mode="lines",
        name=f"{fac} cumulative", line=dict(width=2), yaxis="y1",
        hovertemplate="%{x|%Y-%m-%d}<br>"+fac+" cumulative: %{y:.3f}<extra></extra>"
    ))
    if ENABLE_RIGHT_AXIS_OVERLAY:
        fig.update_layout(yaxis2=dict(title="Daily Return", overlaying="y", side="right", showgrid=False))

    fig.update_layout(
        margin=dict(l=20,r=20,t=8,b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        xaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
        yaxis=dict(title="Cumulative Return", showgrid=True, gridcolor="#e5e7eb"),
        template="plotly_white", height=430, shapes=[]
    )
    html_plot = pio.to_html(fig, include_plotlyjs=PLOTLY_INCLUDE, full_html=False, div_id=plot_id)

    # Controls
    all_lags, all_hors = _available_lags_horizons(sub_tv_all, sub_te_all)
    metric_opts = "".join(
        f"<option value='{m}'>"+METRIC_ALIASES.get(m,m)+"</option>"
        for m in METRICS_SELECTED if (m in sub_tv_all.columns or m in sub_te_all.columns)
    )
    split_opts = "<option value='TrainValid'>TrainValid</option><option value='Test'>Test</option>"
    lag_opts   = "<option value='ALL'>ALL</option>" + "".join(f"<option value='{L}'>"+str(L)+"</option>" for L in all_lags)
    hor_opts   = "<option value='ALL'>ALL</option>" + "".join(f"<option value='{H}'>"+str(H)+"</option>" for H in all_hors)
    model_opts  = "".join(f"<option value='{m}'>"+m+"</option>" for m in models_all)
    # Normalize again just in case (defensive against unexpected types)
    regimes_norm = [ _norm_rid_to_str(r) for r in regimes_all ]
    regime_opts = "".join(f"<option value='{r}'>R{r}</option>" for r in regimes_norm)

    overlay_block = ""
    if ENABLE_RIGHT_AXIS_OVERLAY:
        overlay_block = """
      <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;border-top:1px solid #e5e7eb;padding-top:8px;">
        <span style="font-weight:700;color:#111827;">Right axis overlay</span>
        <select id="__PID___overlay">
          <option value="none">None</option>
          <option value="daily" selected>Daily returns</option>
        </select>
        <button type="button" id="__PID___apply_overlay">Apply</button>
        <button type="button" id="__PID___clear_overlay">Clear</button>
      </div>
        """

    controls_tpl = r"""
<div style="display:flex;gap:16px;align-items:flex-start;flex-wrap:wrap;">
  <div style="flex:2;min-width:320px;">__PLOT__</div>
  <div style="flex:1;min-width:300px;border:1px solid #e5e7eb;border-radius:8px;padding:10px;">
    <div style="display:flex;flex-direction:column;gap:10px;font-size:12px;">
      <div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap;">
        <span style="font-weight:700;color:#111827;">Regime shading</span>
        <label><input type='checkbox' id='__PID___master'/> Enable</label>
      </div>

      <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;">
        <span style="font-weight:600;">Pick from table:</span>
        <select id='__PID___metric'>__METRIC_OPTS__</select>
        <select id='__PID___split_simple'>__SPLIT_OPTS__</select>
        <label>Lag: <select id='__PID___lag_pick'>__LAG_OPTS__</select></label>
        <label>Horizon: <select id='__PID___hor_pick'>__HOR_OPTS__</select></label>
        <button type='button' id='__PID___btn_add_from_table'>Add</button>
      </div>

      <div style="display:flex;gap:8px;align-items:flex-start;flex-wrap:wrap;">
        <span style="font-weight:600;">Filter:</span>
        <label>Model <select id='__PID___model' multiple size='6' style='min-width:140px'>__MODEL_OPTS__</select></label>
        <label>Regime <select id='__PID___reg' multiple size='6' style='min-width:100px'>__REG_OPTS__</select></label>
        <div style="display:flex;flex-direction:column;gap:6px;">
          <button type='button' id='__PID___btn_add_filtered'>Add filtered</button>
          <button type='button' id='__PID___btn_clear'>Clear</button>
        </div>
      </div>

      <div id='__PID___chips' style="display:flex;flex-wrap:wrap;gap:8px;margin:4px 0;"></div>

      <div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap;border-top:1px solid #e5e7eb;padding-top:8px;">
        <span style="font-weight:700;color:#111827;">Chart options</span>
        <label>Items per cell:
          <input id='__PID___maxitems' type='number' min='1' step='1' value='__MAX_ITEMS__' style='width:64px'/>
        </label>
        <button type='button' id='__PID___btn_expand_all'>Expand all</button>
        <button type='button' id='__PID___btn_collapse_all'>Collapse all</button>
        <label><input type='checkbox' id='__PID___showVAL'/> Show VAL boundary</label>
        <label><input type='checkbox' id='__PID___showTEST'/> Show TEST boundary</label>
      </div>

__OVERLAY_BLOCK__

      <div style="font-size:11px;color:#6b7280;border-top:1px dashed #e5e7eb;padding-top:8px;">
        <div><b>Diagnostics</b></div>
        <div id='__PID___diag'></div>
      </div>
    </div>
  </div>
</div>
"""
    panel_html = (controls_tpl
        .replace("__PLOT__", html_plot)
        .replace("__PID__", plot_id)
        .replace("__METRIC_OPTS__", metric_opts)
        .replace("__SPLIT_OPTS__", split_opts)
        .replace("__LAG_OPTS__", lag_opts)
        .replace("__HOR_OPTS__", hor_opts)
        .replace("__MODEL_OPTS__", model_opts)
        .replace("__REG_OPTS__", regime_opts)
        .replace("__MAX_ITEMS__", str(DEFAULT_MAX_ITEMS_PER_CELL))
        .replace("__OVERLAY_BLOCK__", overlay_block)
    )

    # Build shapes_by_key
    shapes_by_key: dict[str, list[dict]] = {}
    for m in models_all:
        labs = label_cache[m]
        if labs is None or labs.dropna().empty: continue
        rids = sorted({_norm_rid_to_str(x) for x in labs.dropna().unique()})
        for rid in rids:
            segs = _segments_equal(labs, rid, edges)
            if not segs: continue
            color = SHADE_STRONG.get(str(rid), "#e5e7eb")
            key = f"{m}: R{rid}"
            lst = []
            for (x0,x1) in segs:
                lst.append(dict(
                    type="rect", xref="x", yref="paper",
                    x0=pd.to_datetime(x0).isoformat(), x1=pd.to_datetime(x1).isoformat(),
                    y0=0, y1=1, fillcolor=color, opacity=SHADE_OPACITY,
                    line={"width":0}, layer="below"
                ))
            shapes_by_key[key] = lst

    # Registry
    def build_regset_index(df: pl.DataFrame):
        out = {}
        for m in METRICS_SELECTED:
            if m not in df.columns: out[m]=[]; continue
            sub = df.filter(pl.col(m).is_not_null())
            if sub.is_empty(): out[m]=[]; continue
            rows = sub.select(["model_id","regime_id","lag","horizon"]).unique().to_pandas()
            bucket = []
            for _, r in rows.iterrows():
                model_base = str(r["model_id"])
                if model_base.startswith("reglab_"): model_base = model_base[7:]
                rid = _norm_rid_to_str(r["regime_id"])
                key = f"{model_base}: R{rid}"
                if key in shapes_by_key:
                    bucket.append({"key": key, "lag": int(r["lag"]), "hor": int(r["horizon"])})
            out[m] = bucket
        return out

    regset_index = {
        "TrainValid": build_regset_index(sub_tv_all),
        "Test":       build_regset_index(sub_te_all),
    }

    def _bound_from_split(df: pl.DataFrame):
        if df.is_empty(): return None
        a = df.select("date_start").min().item()
        try: return pd.to_datetime(a).isoformat() if a is not None else None
        except: return None

    val_ts = _bound_from_split(sub_tv_all)
    test_ts = _bound_from_split(sub_te_all)

    overlay_json = {
        "x": [pd.to_datetime(x).isoformat() for x in s.index],
        "ret": [float(y) for y in s.values],
        "auto": bool(AUTO_ADD_DAILY_OVERLAY and ENABLE_RIGHT_AXIS_OVERLAY),
    } if ENABLE_RIGHT_AXIS_OVERLAY else None

    # Build-time debug snapshot
    # - present models from labels cache
    # - sample of shapes_by_key
    # - bucket counts by split/metric
    bucket_counts = {
        "TrainValid": {m: len(v) for m, v in regset_index["TrainValid"].items()},
        "Test": {m: len(v) for m, v in regset_index["Test"].items()},
    }
    dbg_snapshot = {
        "shape_keys_ct": len(shapes_by_key),
        "shape_keys_sample": list(shapes_by_key.keys())[:8],
        "models_from_labels": list(label_cache.keys()),
        "regimes_dropdown": regimes_norm,
        "all_lags": all_lags,
        "all_horizons": all_hors,
        "bucket_counts": bucket_counts,
    }

    # JS
    js_tpl = r"""
<script>
function toggleCellItems(cid, linkEl){
  try {
    var cell = document.getElementById(cid); if (!cell) return false;
    var expanded = cell.getAttribute('data-expanded') === '1';
    var nEl = document.getElementById('__PID___maxitems');
    var n = parseInt(nEl && nEl.value) || __MAX_ITEMS__;
    var items = cell.querySelectorAll('.item');
    if (expanded) {
      for (var i=0;i<items.length;i++) items[i].style.display = (i < n) ? '' : 'none';
      cell.setAttribute('data-expanded','0');
      if (linkEl) linkEl.textContent = 'View more';
    } else {
      for (var i=0;i<items.length;i++) items[i].style.display = '';
      cell.setAttribute('data-expanded','1');
      if (linkEl) linkEl.textContent = 'View less';
    }
    return false;
  } catch(e){ console.error(e); return false; }
}

document.addEventListener('DOMContentLoaded', function(){
  try {
    var gd = document.getElementById('__PID__');
    if (!gd) { console.warn('__PID__ plot div not found'); return; }

    var byKey = __BYKEY__;
    var regRegistry = __REGREG__;
    var dbgSnapshot = __DBG_SNAPSHOT__;
    var valTs = __VAL_TS__;
    var testTs = __TEST_TS__;
    var overlay = __OVERLAY_JSON__;
    var chipSet = new Set();

    function $id(id) { return document.getElementById(id); }
    function diag(msg){
      var el = $id('__PID___diag'); if (!el) return;
      var p = document.createElement('div'); p.textContent = msg; el.appendChild(p);
      console.log('[__PID__]', msg);
    }

    function countBuckets(regset){ var n=0; for (var k in regset){ if (regset[k]) n += regset[k].length; } return n; }
    // Initial diagnostics
    diag('TrainValid buckets total: ' + countBuckets(regRegistry.TrainValid));
    diag('Test buckets total: ' + countBuckets(regRegistry.Test));
    try {
      var msel=$id('__PID___model'); var rsel=$id('__PID___reg');
      if (msel) diag('Model options: '+Array.from(msel.options).map(o=>o.value).join(', '));
      if (rsel) diag('Regime options: '+Array.from(rsel.options).map(o=>o.textContent).join(', '));
      diag('Shapes-by-key count='+Object.keys(byKey).length+' sample='+Object.keys(byKey).slice(0,8).join(' | '));
      diag('Bucket counts (TrainValid): '+JSON.stringify(dbgSnapshot.bucket_counts.TrainValid));
      diag('Bucket counts (Test): '+JSON.stringify(dbgSnapshot.bucket_counts.Test));
    } catch(e) { console.warn('init diag failed', e); }

    function renderChips(){
      var el = $id('__PID___chips'); if (!el) return;
      el.innerHTML='';
      chipSet.forEach(function(k){
        var badge = document.createElement('span');
        badge.style.cssText='display:inline-flex;align-items:center;gap:6px;padding:2px 8px;border:1px solid #d1d5db;border-radius:999px;background:#fff;';
        badge.textContent=k;
        var x=document.createElement('button'); x.textContent='×';
        x.style.cssText='margin-left:6px;border:none;background:transparent;cursor:pointer;';
        x.onclick=function(){ chipSet.delete(k); renderChips(); applyShade(); };
        badge.appendChild(x);
        el.appendChild(badge);
      });
    }

    function applyShade(){
      var sh=[];
      var showV = $id('__PID___showVAL') && $id('__PID___showVAL').checked;
      var showT = $id('__PID___showTEST') && $id('__PID___showTEST').checked;
      if (showV && valTs) sh.push({type:'line', x0:valTs, x1:valTs, yref:'paper', y0:0, y1:1, line:{width:2, dash:'dash', color:'#1f77b4'}, layer:'above'});
      if (showT && testTs) sh.push({type:'line', x0:testTs, x1:testTs, yref:'paper', y0:0, y1:1, line:{width:2, dash:'dash', color:'#d62728'}, layer:'above'});

      var master = $id('__PID___master');
      if (master && master.checked) {
        chipSet.forEach(function(k){
          var lst = byKey[k] || [];
          for (var i=0;i<lst.length;i++) sh.push(lst[i]);
        });
      }
      try { Plotly.relayout(gd, {shapes: sh}); } catch(e){ console.error(e); }
      var keys = [];
      chipSet.forEach(function(k){ keys.push(k); });
      diag('applyShade: shapes='+sh.length+' chips='+chipSet.size+' keys_sample='+(keys.slice(0,5).join(' | ')));
    }

    function addFromTable(){
      var metric = $id('__PID___metric').value;
      var split  = $id('__PID___split_simple').value;
      var lag    = $id('__PID___lag_pick').value;
      var hor    = $id('__PID___hor_pick').value;
      var bucket = (regRegistry[split] && regRegistry[split][metric]) ? regRegistry[split][metric] : [];
      diag('addFromTable: metric='+metric+' split='+split+' bucket_len='+(bucket?bucket.length:0)+' lag='+lag+' hor='+hor);
      if (bucket && bucket.length){
        var sample = bucket.slice(0,5).map(b=>b.key+':(L'+b.lag+',H'+b.hor+')');
        diag('addFromTable: bucket sample: '+sample.join(', '));
      }
      var added=0;
      var reasons={lag:0,hor:0,missing:0};
      for (var i=0;i<bucket.length;i++){
        var b=bucket[i];
        var okLag=(lag==='ALL'||String(b.lag)===String(lag));
        var okHor=(hor==='ALL'||String(b.hor)===String(hor));
        if (okLag && okHor){
          if (byKey[b.key]) { chipSet.add(b.key); added++; }
          else { diag('addFromTable: key missing in shapes_by_key -> '+b.key); reasons.missing++; }
        } else {
          if (!okLag) reasons.lag++;
          if (!okHor) reasons.hor++;
        }
      }
      if (!added){
        alert('No regimes matched your pick.');
        diag('addFromTable: nothing added; reasons='+JSON.stringify(reasons));
        return;
      }
      var master=$id('__PID___master'); if (master) master.checked=true;
      diag('addFromTable: added '+added+' keys; chips='+chipSet.size);
      renderChips(); applyShade();
    }

    function addFiltered(){
      var modSel = $id('__PID___model'); var regSel = $id('__PID___reg');
      var mods = modSel ? Array.from(modSel.selectedOptions).map(o=>o.value) : [];
      var regs = regSel ? Array.from(regSel.selectedOptions).map(o=>o.value.replace(/^R/,'')) : [];
      diag('addFiltered: mods='+JSON.stringify(mods)+' regs='+JSON.stringify(regs));
      var added=0; var considered=0;
      Object.keys(byKey).forEach(function(k){
        var m=/^(.+):\s*R(.*)$/.exec(k); if (!m) return;
        var mk=m[1], rk=m[2];
        var okM=(mods.length===0)||(mods.indexOf(mk)!==-1);
        var okR=(regs.length===0)||(regs.indexOf(rk)!==-1);
        considered++;
        if (okM && okR) { chipSet.add(k); added++; }
      });
      if (!added){ alert('No regimes matched current filters.'); diag('addFiltered: 0 added; considered '+considered); return; }
      var master=$id('__PID___master'); if (master) master.checked=true;
      diag('addFiltered: +'+added+' keys; chips='+chipSet.size);
      renderChips(); applyShade();
    }

    function clearAll(){ chipSet.clear(); renderChips(); applyShade(); diag('clearAll'); }

    function clampAll(){
      var nEl=$id('__PID___maxitems'); var n=parseInt(nEl && nEl.value) || __MAX_ITEMS__;
      var grid=document.getElementById('metrics-grid'); if(!grid) return;
      var lists=grid.querySelectorAll('.celllist');
      if(!lists.length){ setTimeout(clampAll, 30); return; }
      lists.forEach(function(cell){
        var items=cell.querySelectorAll('.item');
        for (var i=0;i<items.length;i++) items[i].style.display=(i<n)?'':'none';
        cell.setAttribute('data-expanded','0');
      });
      diag('clampAll: n='+n+' lists='+lists.length);
    }
    function expandAll(){
      var grid=document.getElementById('metrics-grid'); if(!grid) return;
      grid.querySelectorAll('.celllist').forEach(function(cell){
        var items=cell.querySelectorAll('.item');
        for (var i=0;i<items.length;i++) items[i].style.display='';
        cell.setAttribute('data-expanded','1');
      });
      diag('expandAll');
    }
    function collapseAll(){
      var nEl=$id('__PID___maxitems'); var n=parseInt(nEl && nEl.value) || __MAX_ITEMS__;
      var grid=document.getElementById('metrics-grid'); if(!grid) return;
      grid.querySelectorAll('.celllist').forEach(function(cell){
        var items=cell.querySelectorAll('.item');
        for (var i=0;i<items.length;i++) items[i].style.display=(i<n)?'':'none';
        cell.setAttribute('data-expanded','0');
      });
      diag('collapseAll to '+n);
    }

    // Right-axis overlay
    function applyOverlay(kind){
      try {
        var toDrop=[];
        (gd.data||[]).forEach(function(tr,i){ if(tr.yaxis==='y2') toDrop.push(i); });
        if(toDrop.length) Plotly.deleteTraces(gd, toDrop);
      } catch(e){ console.error(e); }
      if(kind==='daily' && overlay){
        var tr={ x:overlay.x, y:overlay.ret, mode:'lines', name:'Daily return', yaxis:'y2',
                 hovertemplate:'%{x}<br>ret: %{y:.4f}<extra></extra>' };
        try { Plotly.addTraces(gd, [tr]); } catch(e) { console.error(e); }
        diag('overlay: daily pts='+(overlay.ret?overlay.ret.length:0)+' x='+ (overlay.x?overlay.x.length:0));
      } else { diag('overlay: none'); }
    }
    function clearOverlay(){
      try {
        var toDrop=[]; (gd.data||[]).forEach(function(tr,i){ if(tr.yaxis==='y2') toDrop.push(i); });
        if(toDrop.length) Plotly.deleteTraces(gd, toDrop);
        diag('overlay cleared: removed '+toDrop.length);
      } catch(e){ console.error(e); }
    }

    // Wire
    var B = [
      ['__PID___btn_add_from_table', addFromTable],
      ['__PID___btn_add_filtered', addFiltered],
      ['__PID___btn_clear', clearAll],
      ['__PID___apply_overlay', function(){ var sel=$id('__PID___overlay'); applyOverlay(sel?sel.value:'none'); }],
      ['__PID___clear_overlay', clearOverlay]
    ];
    B.forEach(function(x){ var el=$id(x[0]); if(el) el.addEventListener('click', x[1]); });

    ['__PID___master','__PID___showVAL','__PID___showTEST'].forEach(function(id){
      var el=$id(id); if(el) el.addEventListener('change', applyShade);
    });
    var mx=$id('__PID___maxitems'); if(mx){ mx.addEventListener('input', clampAll); setTimeout(clampAll, 60); }

    if (overlay && overlay.auto) { applyOverlay('daily'); }

    // Per-plot layout binder
    function setMetricsCols(n) {
      var grid=document.getElementById('metrics-grid'); if(!grid) return;
      if (n==='auto') {
        var cards=grid.querySelectorAll('.metric-card');
        grid.style.gridTemplateColumns='repeat('+(cards.length||1)+', minmax(0, 1fr))';
      } else {
        grid.style.gridTemplateColumns='repeat('+n+', minmax(0, 1fr))';
      }
    }
    var sel=document.getElementById('sel-metric-cols');
    if (sel){
      sel.addEventListener('change', function(){ setMetricsCols(this.value); diag('setMetricsCols change -> '+this.value); });
      setTimeout(function(){ diag('setMetricsCols init -> '+sel.value); setMetricsCols(sel.value); }, 80);
      var grid=document.getElementById('metrics-grid');
      if (grid){
        var mo=new MutationObserver(function(){ diag('setMetricsCols mutation -> '+sel.value+' current='+getComputedStyle(grid).gridTemplateColumns); setMetricsCols(sel.value); });
        mo.observe(grid, {childList:true, subtree:true});
      }
    }

    diag('ready');
  } catch(e){ console.error(e); }
});

// Page-level layout binder (extra-safe)
(function(){
  function setCols(){
    var sel=document.getElementById('sel-metric-cols');
    var grid=document.getElementById('metrics-grid');
    if(!sel||!grid) return;
    var n=sel.value;
    if(n==='auto'){
      var cards=grid.querySelectorAll('.metric-card');
      grid.style.gridTemplateColumns='repeat('+(cards.length||1)+', minmax(0, 1fr))';
    } else {
      grid.style.gridTemplateColumns='repeat('+n+', minmax(0, 1fr))';
    }
  }
  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded', function(){ setTimeout(setCols, 50); });
  } else { setTimeout(setCols, 50); }
  window.addEventListener('resize', setCols);
})();
</script>
"""
    js_html = (js_tpl
        .replace("__PID__", plot_id)
        .replace("__BYKEY__", json.dumps(shapes_by_key))
        .replace("__REGREG__", json.dumps(regset_index))
        .replace("__VAL_TS__", json.dumps(val_ts))
        .replace("__TEST_TS__", json.dumps(test_ts))
        .replace("__OVERLAY_JSON__", json.dumps(overlay_json))
        .replace("__DBG_SNAPSHOT__", json.dumps(dbg_snapshot))
        .replace("__MAX_ITEMS__", str(DEFAULT_MAX_ITEMS_PER_CELL))
    )
    dbg_json = json.dumps(dbg_snapshot)
    return panel_html, js_html, dbg_json

def build_html(alpha_split: pl.DataFrame,
               labels_long: pl.DataFrame,
               R_df: pd.DataFrame,
               out_dir: plib.Path = OUT_DIR):
    global labels  # used by shading helpers
    labels = labels_long

    tv = split2(alpha_split)
    tv = _scope_filter(tv, SCOPE)
    wide_all = _pivot_wide(tv)
    wide_tv  = _apply_filters(wide_all.filter(pl.col("split2")=="trainval"), FILTERS)
    wide_te  = _apply_filters(wide_all.filter(pl.col("split2")=="test"), FILTERS)

    present_metrics = [m for m in METRICS_SELECTED if m in wide_all.columns]
    factors = sorted(set(wide_all.select("target_name").to_series().to_list()))

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
        panel_html, js_html, dbg_json = _build_plot_html(fac, sub_tv_all, sub_te_all, plot_id, R_df)

        sections = []
        for metric in present_metrics:
            alias = METRIC_ALIASES.get(metric, metric)
            idprefix_tv = f"{_sanitize_id(fac)}_{_sanitize_id(metric)}_tv"
            idprefix_te = f"{_sanitize_id(fac)}_{_sanitize_id(metric)}_te"
            html_tv = _string_table(sub_tv_all, metric, idprefix_tv)
            html_te = _string_table(sub_te_all, metric, idprefix_te)
            subtitle_tv = f"Freq={fq_tv} · Range=[{ds_tv} .. {de_tv}]"
            subtitle_te = f"Freq={fq_te} · Range=[{ds_te} .. {de_te}]"

            sections.append(f"""
            <div class="metric-card" id="section-{_sanitize_id(metric)}" style="min-width:0;">
              <div style="font-weight:600;margin-bottom:4px;">{alias}</div>
              <div style="display:flex;gap:8px;align-items:flex-start;">
                <div style="flex:1;min-width:0;">
                  <div style="color:#6b7280;margin-bottom:4px;">{subtitle_tv}</div>
                  {html_tv}
                </div>
                <div style="flex:1;min-width:0;">
                  <div style="color:#6b7280;margin-bottom:4px;">{subtitle_te}</div>
                  {html_te}
                </div>
              </div>
            </div>
            """)

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

        out_file = out_dir / f"{fac}_trainvalid_test.html"
        page_html = f"""
<html>
<head>
  <meta charset="utf-8">
  <title>Data: {fac}</title>
  <style>
    {CELLLIST_CSS}
    .grid {{ display:grid; grid-template-columns: repeat(1, minmax(0, 1fr)); gap:12px; }}
    button {{ font-size: 12px; padding: 4px 8px; border: 1px solid #d1d5db; background:#fff; border-radius:6px; cursor:pointer; }}
    button:hover {{ background:#f3f4f6; }}
    select {{ font-size:12px; }}
    th, td {{ vertical-align: top; }}
  </style>
</head>
<body style="margin:20px;font-family:Inter,Arial,sans-serif;color:#111827;">
  <h2 style="margin:0 0 6px 0;">Data: {fac}</h2>
  <div style="color:#374151;margin:0 0 8px 0;">
    Filters: {_fmt_filters(FILTERS)} · Scope: {_fmt_scope(SCOPE)}
  </div>

  <!-- Quick diagnostics (build-time) -->
  <div style="background:#f9fafb;border:1px solid #e5e7eb;padding:8px;border-radius:8px;margin-bottom:8px;color:#374151;font-size:12px;">
    <div><b>Diagnostics (build-time)</b></div>
    <div>Factor: {fac}</div>
    <div>TrainValid rows: {sub_tv_all.height} · Test rows: {sub_te_all.height}</div>
    <div>Present metrics: {", ".join(present_metrics)}</div>
    <div>Plot debug: {dbg_json}</div>
  </div>

  <!-- Plot + right panel -->
  {panel_html}

  <!-- Layout control -->
  {sel_html}

  <!-- Metric sections -->
  <div style="color:#6b7280;margin:4px 0 8px 0;">Metrics rendered: {", ".join([METRIC_ALIASES.get(m,m) for m in present_metrics])}</div>
  <div id="metrics-grid" class="grid">
    {''.join(sections)}
  </div>

  <!-- JS -->
  {js_html}
</body></html>
"""
        out_file.write_text(page_html, encoding="utf-8")
        index_rows.append((fac, out_file.name))

    links = "\n".join([f'<li><a href="{name}" style="text-decoration:none;color:#2563eb;">{fac}</a></li>' for fac,name in index_rows])
    (out_dir / "index.html").write_text(f"""
<html><head><meta charset="utf-8"><title>Regimes Tables Index</title></head>
<body style="margin:20px;font-family:Inter,Arial,sans-serif;color:#222;">
  <h1>Regimes Tables — Consolidated</h1>
  <p>Top: cumulative factor return. Use the right panel to add <b>regime shading</b> (Enable, then Add).
     Right axis overlay: daily returns (auto-added). Items-per-cell hides overflow (live).</p>
  <ul>{links}</ul>
</body></html>
""", encoding="utf-8")
    print(f"Saved HTML to: {out_dir.resolve()} (open index.html)")
