from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import pandas as pd
import polars as pl
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np
from plotly.utils import PlotlyJSONEncoder
import json
from scipy import stats

DEFAULT_FILTERS: Dict[str, Tuple[str, float]] = {
    "t_stat_hac": (">=", 1.96),
    "p_val_hac": ("<=", 0.05),
    "ir": (">=", 0.10),
}


def split2(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.when(pl.col("split").is_in(["train", "val"]))
        .then(pl.lit("trainval"))
        .otherwise(pl.col("split"))
        .alias("split2")
    )


def _pivot_wide(df: pl.DataFrame) -> pl.DataFrame:
    key = [
        "target_name",
        "model_id",
        "regime_id",
        "horizon",
        "lag",
        "split",
        "split2",
        "data_freq",
        "date_start",
        "date_end",
        "time",
    ]
    try:
        return df.pivot(index=key, on="metric_name", values="metric_value", aggregate_function="mean")
    except TypeError:
        return df.pivot(index=key, columns="metric_name", values="metric_value", aggregate_function="mean")


def _apply_filters(wide: pl.DataFrame, filters: Dict[str, Tuple[str, float]]) -> pl.DataFrame:
    expr = None
    for m, (op, val) in filters.items():
        c = pl.col(m)
        if op == ">=":
            cond = c >= float(val)
        elif op == ">":
            cond = c > float(val)
        elif op == "<=":
            cond = c <= float(val)
        elif op == "<":
            cond = c < float(val)
        elif op == "==":
            cond = c == float(val)
        else:
            raise ValueError(f"Unsupported operator: {op}")
        expr = cond if expr is None else (expr & cond)
    return wide.filter(expr) if expr is not None else wide


def _scope_filter(df: pl.DataFrame, scope: Dict) -> pl.DataFrame:
    out = df
    if scope.get("factors"):
        out = out.filter(pl.col("target_name").is_in(scope["factors"]))
    if scope.get("models"):
        out = out.filter(pl.col("model_id").is_in(scope["models"]))
    if scope.get("regimes"):
        out = out.filter(
            pl.col("regime_id").cast(pl.Utf8).is_in([str(x) for x in scope["regimes"]])
        )
    if scope.get("horizons"):
        out = out.filter(pl.col("horizon").is_in([int(x) for x in scope["horizons"]]))
    if scope.get("lags"):
        out = out.filter(pl.col("lag").is_in([int(x) for x in scope["lags"]]))
    return out


def _fmt_filters(filters: Dict[str, Tuple[str, float]], aliases: Dict[str, str]) -> str:
    sym = {">=": "≥", ">": "›", "<=": "≤", "<": "‹", "==": "="}
    parts: List[str] = []
    for k, (op, val) in filters.items():
        name = aliases.get(k, k)
        try:
            vv = f"{float(val):.2f}"
        except Exception:
            vv = str(val)
        parts.append(f"{name} {sym.get(op, op)} {vv}")
    return "; ".join(parts) if parts else "none"


def _split_ranges(wide_all_fac: pl.DataFrame) -> List[Tuple[pd.Timestamp, pd.Timestamp, str]]:
    out: List[Tuple[pd.Timestamp, pd.Timestamp, str]] = []
    for sp in ["train", "val", "test"]:
        sub = wide_all_fac.filter(pl.col("split") == sp)
        if sub.is_empty():
            continue
        a = sub.select("date_start").min().item()
        b = sub.select("date_end").max().item()
        if a is None or b is None:
            continue
        out.append((pd.to_datetime(a), pd.to_datetime(b), sp))
    return out


def _regime_segments(labels_long: pl.DataFrame, model_name: Optional[str]) -> List[Tuple[pd.Timestamp, pd.Timestamp, str]]:
    if labels_long is None or labels_long.is_empty():
        return []
    want = (
        model_name if (model_name and model_name.startswith("reglab_")) else f"reglab_{model_name}"
    ) if model_name else labels_long.select("model_name").unique().to_series().to_list()[0]
    lab = labels_long.filter(pl.col("model_name") == want).select(["time", "regime_code"]).sort("time")
    if lab.is_empty():
        return []
    df = lab.to_pandas()
    df["time"] = pd.to_datetime(df["time"])
    df = df.dropna(subset=["regime_code"])
    if df.empty:
        return []
    times = df["time"].to_numpy()
    regs = df["regime_code"].astype(str).to_numpy()
    segs: List[Tuple[pd.Timestamp, pd.Timestamp, str]] = []
    start = times[0]
    prev = regs[0]
    for i in range(1, len(df)):
        if regs[i] != prev:
            segs.append((pd.Timestamp(start), pd.Timestamp(times[i]), str(prev)))
            start, prev = times[i], regs[i]
    segs.append((pd.Timestamp(start), pd.Timestamp(times[-1]), str(prev)))
    return segs


def _sanitize_id(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]+", "_", s)


def _string_table(
    df_wide_factor_split: pl.DataFrame,
    metric: str,
    idprefix: str,
    abbrev_reglab_prefix: bool = True,
) -> pd.DataFrame:
    """Return a Lag×Horizon grid of HTML strings; each cell contains stacked entries with an expander."""
    if df_wide_factor_split.is_empty() or metric not in df_wide_factor_split.columns:
        return pd.DataFrame()

    df = df_wide_factor_split.filter(pl.col(metric).is_not_null())

    model_show = (
        pl.when(pl.lit(abbrev_reglab_prefix) & pl.col("model_id").str.starts_with("reglab_"))
        .then(pl.col("model_id").str.replace("^reglab_", ""))
        .otherwise(pl.col("model_id"))
        .alias("model_show")
    )
    asc = metric.lower().startswith("p_val")

    tmp = (
        df.with_columns([model_show])
        .sort(["lag", "horizon", metric], descending=[False, False, not asc])
        .with_columns(
            [
                pl.concat_str(
                    [
                        pl.lit('<div class="it item"><span class="m">'),
                        pl.col("model_show"),
                        pl.lit('</span> <span class="rg">R'),
                        pl.col("regime_id"),
                        pl.lit('</span>'),
                        pl.lit(' <span class="v">'),
                        pl.col(metric).round(3).cast(pl.Utf8),
                        pl.lit("</span></div>"),
                    ],
                    separator="",
                ).alias("it_html")
            ]
        )
    )

    agg = (
        tmp.group_by(["lag", "horizon"]).agg([pl.col("it_html").alias("items"), pl.len().alias("n_total")])
        .with_columns(
            [
                pl.concat_str(
                    [
                        pl.lit(_sanitize_id(idprefix)),
                        pl.lit("_l"),
                        pl.col("lag").cast(pl.Utf8),
                        pl.lit("_h"),
                        pl.col("horizon").cast(pl.Utf8),
                    ],
                    separator="",
                ).alias("cell_id")
            ]
        )
    )

    agg = agg.with_columns(
        [
            pl.concat_str(
                [
                    pl.lit('<div class="celllist" id="'),
                    pl.col("cell_id"),
                    pl.lit('">'),
                    pl.col("items").list.join(""),
                    pl.when(pl.col("n_total") > 1)
                    .then(
                        pl.concat_str(
                            [
                                pl.lit('<div class="item more" data-n="'),
                                (pl.col("n_total") - 1).cast(pl.Utf8),
                                pl.lit('" onclick=toggleCellMore(this)>+'),
                                (pl.col("n_total") - 1).cast(pl.Utf8),
                                pl.lit(" more</div>"),
                            ],
                            separator="",
                        )
                    )
                    .otherwise(pl.lit("")),
                    pl.lit("</div>"),
                ],
                separator="",
            ).alias("cell")
        ]
    )

    table_pl = agg.pivot(index="lag", columns="horizon", values="cell", aggregate_function="first").sort("lag")
    dfp = table_pl.to_pandas()
    if "lag" in dfp.columns:
        dfp = dfp.set_index("lag")
    try:
        cols_sorted = sorted(dfp.columns, key=lambda x: int(x))
    except Exception:
        cols_sorted = sorted(dfp.columns)
    dfp = dfp.reindex(cols_sorted, axis=1)
    dfp.index.name = "Lag"
    dfp.columns.name = "Horizon"
    return dfp


def _style_table(df: pd.DataFrame, title: str, subtitle: str) -> str:
    if df.empty:
        return (
            f'<div style="font-family:Inter,Arial,sans-serif;color:#444;"><h4>{title}</h4>'
            f'<div style="color:#6b7280;">{subtitle}</div><em>No entries passed thresholds</em></div>'
        )
    styler = (
        df.style.set_caption(
            f'{title}<br><span style="font-weight:400;color:#6b7280;">{subtitle}</span>'
        )
        .set_table_styles(
            [
                {
                    "selector": "caption",
                    "props": "caption-side:top;font-weight:600;padding:4px 0;",
                },
                {
                    "selector": "th",
                    "props": "background:#f5f7fb;color:#333;font-weight:600;padding:6px;border:1px solid #e6e9ef;",
                },
                {
                    "selector": "td",
                    "props": "padding:6px;border:1px solid #e6e9ef;vertical-align:top;",
                },
                {
                    "selector": "table",
                    "props": "border-collapse:collapse;font-family:Inter,Arial,sans-serif;font-size:13px;",
                },
            ]
        )
        .format(escape=None)
    )
    return styler.to_html()


def _build_plot_html(
    fac: str,
    R: pd.DataFrame,
    wide_all: pl.DataFrame,
    labels_long: Optional[pl.DataFrame],
    plot_id: str,
    split_colors: Dict[str, str],
    shade_colors: Dict[str, str],
    shade_opacity: float = 0.12,
) -> Tuple[str, str]:
    if not isinstance(R, pd.DataFrame) or fac not in R.columns:
        return ("<div style=\"color:#6b7280;\">(Plot skipped: R not available)</div>", "")
    s = pd.to_numeric(R[fac], errors="coerce").dropna()
    if s.empty:
        return ("<div style=\"color:#6b7280;\">(Plot skipped)</div>", "")

    cum = (s.cumsum().pipe(pd.Series).apply(np.exp) - 1.0)
    cum.index = s.index
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=cum.index,
            y=cum.values,
            mode="lines",
            name=f"{fac} cumulative",
            line=dict(color="#2563eb", width=2),
        )
    )

    splits = _split_ranges(wide_all.filter(pl.col("target_name") == fac))
    shapes_splits = []
    for (x0, x1, sp) in splits:
        color = split_colors.get(sp, "#f3f4f6")
        shapes_splits.append(
            dict(
                type="rect",
                xref="x",
                yref="paper",
                x0=str(pd.to_datetime(x0)),
                x1=str(pd.to_datetime(x1)),
                y0=0,
                y1=1,
                fillcolor=color,
                opacity=0.18,
                line={"width": 0},
                layer="below",
            )
        )
    for (_, x1, sp) in splits:
        fig.add_vline(x=pd.to_datetime(x1), line_width=1, line_dash="dot", line_color="#9ca3af")

    # pick the most frequent model in TV for shading
    chosen_model: Optional[str] = None
    try:
        cm = (
            wide_all.filter(pl.col("target_name") == fac)
            .filter(pl.col("split2") == "trainval")
            .group_by("model_id")
            .len()
            .sort("len", descending=True)
            .select("model_id")
            .to_series()
            .to_list()
        )
        chosen_model = (str(cm[0]) if cm else None)
    except Exception:
        chosen_model = None
    chosen_model_name = (
        chosen_model[7:] if (chosen_model and str(chosen_model).startswith("reglab_")) else chosen_model
    )

    segs = _regime_segments(labels_long, chosen_model_name) if labels_long is not None else []
    shapes_regimes_by_rid: Dict[str, List[Dict]] = {}
    palette = ["#fde68a", "#bfdbfe", "#bbf7d0", "#fecaca", "#e9d5ff", "#d4d4d8", "#bae6fd", "#fecdd3"]
    for (x0, x1, rid) in segs:
        color = shade_colors.get(str(rid)) or palette[int(str(rid)) % len(palette)]
        if not color.startswith("#"):
            color = "#" + color.lstrip("#")
        shapes_regimes_by_rid.setdefault(str(rid), []).append(
            dict(
                type="rect",
                xref="x",
                yref="paper",
                x0=str(pd.to_datetime(x0)),
                x1=str(pd.to_datetime(x1)),
                y0=0,
                y1=1,
                fillcolor=color,
                opacity=shade_opacity,
                line={"width": 0},
                layer="below",
            )
        )

    fig.update_layout(
        margin=dict(l=20, r=20, t=8, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        xaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
        yaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
        template="plotly_white",
        height=360,
        shapes=shapes_splits + sum(shapes_regimes_by_rid.values(), []),
        showlegend=True,
    )

    # ✅ Use Plotly’s encoder (handles numpy arrays, timestamps, etc.)
    spec = fig.to_plotly_json()
    data_json   = json.dumps(spec["data"],   cls=PlotlyJSONEncoder)
    layout_json = json.dumps(spec["layout"], cls=PlotlyJSONEncoder)
    cfg_json    = json.dumps({"responsive": True})

    container = f'<div id="{plot_id}" style="width:100%;height:360px;"></div>'
    boot = (
        f"<script>(function(){{"
        f"  Plotly.newPlot('{plot_id}', {data_json}, {layout_json}, {cfg_json});"
        f"}})();</script>"
    )
    # toggles per rid
    rids = sorted(shapes_regimes_by_rid.keys(), key=lambda x: int(re.sub(r"\D", "", x)) if re.sub(r"\D", "", x) else 0)
    chips = " ".join(
        [f'<label><input type="checkbox" class="{plot_id}_chk_rid" data-rid="{rid}" checked onchange="applyRegimeToggles_{plot_id}()"> R{rid}</label>' for rid in rids]
    )
    toggles = (
        "<div style=\"display:flex;gap:12px;align-items:center;margin:6px 0 8px 0;\">"
        f"  <label><input type=\"checkbox\" id=\"{plot_id}_chk_master\" checked onchange=\"applyRegimeToggles_{plot_id}()\"> Regime shading</label>"
        f"  <span style=\"color:#6b7280;\">model: {chosen_model_name or 'auto'}</span>"
        "  <span style=\"margin-left:16px;color:#374151;\">Regimes:</span>"
        f"  <span style=\"display:flex;flex-wrap:wrap;gap:8px;\">{chips}</span>"
        "</div>"
        "<script>(function(){"
        f"  var gd=document.getElementById('{plot_id}');"
        f"  var shapesSplits={json.dumps(shapes_splits)};"
        f"  var shapesReg={json.dumps(shapes_regimes_by_rid)};"
        f"  window.applyRegimeToggles_{plot_id}=function(){{"
        "    var out=shapesSplits.slice();"
        f"    var master=document.getElementById('{plot_id}_chk_master');"
        "    if(master && master.checked){"
        f"      document.querySelectorAll('.{plot_id}_chk_rid').forEach(function(cb){{"
        "        if(cb.checked){var rid=cb.getAttribute('data-rid'); if(shapesReg[rid]) out=out.concat(shapesReg[rid]);}"
        "      });"
        "    }"
        "    Plotly.relayout(gd,{shapes:out});"
        "  };"
        f"  window.applyRegimeToggles_{plot_id}();"
        "})();</script>"
    )
    return container + boot, toggles


def run(
    alpha_split: pl.DataFrame,
    R: pd.DataFrame,
    labels_long: Optional[pl.DataFrame],
    out_dir: Path,
    filters: Dict[str, Tuple[str, float]] = DEFAULT_FILTERS,
    metrics_selected: Sequence[str] = ("t_stat_hac", "ir", "p_val_hac"),
    metric_aliases: Optional[Dict[str, str]] = None,
    abbrev_reglab_prefix: bool = True,
):
    out_dir.mkdir(parents=True, exist_ok=True)
    aliases = {
        "t_stat_hac": "HAC t-stat",
        "p_val_hac": "HAC p-value",
        "ir": "Information Ratio",
    }
    if metric_aliases:
        aliases.update(metric_aliases)

    tv = split2(alpha_split)
    wide_all = _pivot_wide(tv)
    wide_tv = _apply_filters(wide_all.filter(pl.col("split2") == "trainval"), filters)
    wide_te = _apply_filters(wide_all.filter(pl.col("split2") == "test"), filters)

    present_metrics = [m for m in metrics_selected if m in wide_all.columns]
    factors = sorted(set(wide_all.select("target_name").to_series().to_list()))
    split_colors = {"train": "#ecfdf5", "val": "#fef3c7", "test": "#fee2e2"}
    shade_colors = {"0": "#d4d4d8", "1": "#fde68a", "2": "#bfdbfe", "3": "#bbf7d0", "4": "#fecaca", "5": "#e9d5ff"}

    index_rows: List[Tuple[str, str]] = []
    for fac in factors:
        sub_tv_all = wide_tv.filter(pl.col("target_name") == fac)
        sub_te_all = wide_te.filter(pl.col("target_name") == fac)

        def _rng(df: pl.DataFrame):
            if df.is_empty():
                return ("NA", "NA", "NA")
            ds = df.select("date_start").min().item()
            de = df.select("date_end").max().item()
            fq = df.select("data_freq").head(1).item()
            return (str(ds), str(de), str(fq))

        ds_tv, de_tv, fq_tv = _rng(sub_tv_all)
        ds_te, de_te, fq_te = _rng(sub_te_all)

        plot_id = f"plot_{_sanitize_id(fac)}"
        plot_html, toggles_html = _build_plot_html(
            fac, R, wide_all, labels_long, plot_id, split_colors, shade_colors
        )

        sections: List[str] = []
        for metric in present_metrics:
            alias = aliases.get(metric, metric)
            idprefix_tv = f"{_sanitize_id(fac)}_{_sanitize_id(metric)}_tv"
            idprefix_te = f"{_sanitize_id(fac)}_{_sanitize_id(metric)}_te"
            df_table_tv = _string_table(sub_tv_all, metric, idprefix_tv, abbrev_reglab_prefix)
            df_table_te = _string_table(sub_te_all, metric, idprefix_te, abbrev_reglab_prefix)

            title_tv = f"Metric: {alias}, Data: {fac}, Train+Validation"
            title_te = f"Metric: {alias}, Data: {fac}, Test"
            subtitle_tv = f"Freq={fq_tv} · Range=[{ds_tv} .. {de_tv}]"
            subtitle_te = f"Freq={fq_te} · Range=[{ds_te} .. {de_te}]"
            html_tv = _style_table(df_table_tv, title_tv, subtitle_tv)
            html_te = _style_table(df_table_te, title_te, subtitle_te)

            combined = (
                f"""
<div class="metric-card" id="section-{_sanitize_id(metric)}" style="min-width:0;">
  <div style="display:flex;gap:6px;align-items:flex-start;">
    <div style="flex:1;min-width:0;">{html_tv}</div>
    <div style="flex:1;min-width:0;">{html_te}</div>
  </div>
</div>
"""
            )
            sections.append(combined)

        controls_html = (
            """
<div style="display:flex;gap:16px;align-items:center;margin:6px 0 8px 0;">
  <div style="color:#111827;font-weight:600;">Layout:</div>
  <div>Columns:
    <select id="sel-metric-cols">
      <option value="auto">auto</option><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option>
    </select>
  </div>
  <div>Items per cell:
    <select id="sel-items-per-cell">
      <option value="3">3</option><option value="5">5</option><option value="10">10</option><option value="all">all</option>
    </select>
  </div>
</div>
"""
        )

        page_js = (
            """
<script>
function applyItemsPerCell(K){
  const cells=document.querySelectorAll('.celllist');
  cells.forEach(cell=>{
    const items=cell.querySelectorAll('.it');
    const more=cell.querySelector('.item.more');
    const total=items.length;
    if(K==='all'){
      items.forEach(el=>el.style.display=''); if(more) more.style.display='none';
    } else {
      const k=parseInt(K,10);
      items.forEach((el,idx)=>el.style.display=(idx<Math.max(1,k))?'':'none');
      if(more){ const rest=Math.max(0,total-Math.max(1,k)); more.style.display=rest>0?'':'none'; more.innerText=rest>0?('+'+rest+' more'):''; more.setAttribute('data-n', rest); }
    }
  });
}
function toggleCellMore(el){
  var cell = el.closest('.celllist'); if(!cell) return;
  const items = cell.querySelectorAll('.it');
  const more  = cell.querySelector('.item.more');
  const expanded = (more && more.innerText==='show less');
  if(!expanded){ items.forEach(el=>el.style.display=''); if(more) more.innerText='show less'; }
  else {
    const sel=document.getElementById('sel-items-per-cell'); const K=sel?sel.value:'6';
    const k=(K==='all')?Number.POSITIVE_INFINITY:parseInt(K,10);
    let shown=0; items.forEach(el=>{ if(shown<Math.max(1,k)){el.style.display=''; shown+=1;} else {el.style.display='none';} });
    if(more){ const rest=Math.max(0, items.length-Math.max(1,k)); more.innerText= rest>0?('+'+rest+' more'):''; }
  }
}
function setMetricsCols(n){ const grid=document.getElementById('metrics-grid'); if(!grid) return; if(n==='auto'){ const cards=grid.querySelectorAll('.metric-card'); grid.style.gridTemplateColumns='repeat('+cards.length+', minmax(0,1fr))'; } else { grid.style.gridTemplateColumns='repeat('+n+', minmax(0,1fr))'; } }
function initPage(defCols, defItems){ const selCols=document.getElementById('sel-metric-cols'); if(selCols){ setMetricsCols(defCols); selCols.value=defCols; selCols.addEventListener('change', function(){ setMetricsCols(this.value); }); } const selItems=document.getElementById('sel-items-per-cell'); if(selItems){ applyItemsPerCell(defItems); selItems.value=defItems; selItems.addEventListener('change', function(){ applyItemsPerCell(this.value); }); } }
</script>
"""
        )

        html = (
            f"""
<html>
<head>
  <meta charset="utf-8"><title>Data Name: {fac}</title>
  <style>.grid {{ display:grid; grid-template-columns: repeat({len(present_metrics)}, minmax(0,1fr)); gap:12px; }}</style>
</head>
<body style="margin:20px;font-family:Inter,Arial,sans-serif;color:#111827;">
  <h2 style="margin:0 0 6px 0;">Data Name: {fac}</h2>
  <div style="margin:8px 0 2px 0;">{plot_html}{toggles_html}</div>
  {controls_html}
  <div id="metrics-grid" class="grid">{''.join(sections)}</div>
  {page_js}
  <script>initPage("auto", "5");</script>
</body>
</html>
"""
        )

        out = out_dir / f"{fac}_trainval_test.html"
        out.write_text(html, encoding="utf-8")
        index_rows.append((fac, out.name))

    links = "\n".join(
        [f'<li><a href="{name}" style="text-decoration:none;color:#2563eb;">{fac}</a></li>' for fac, name in index_rows]
    )
    index_html = (
        f"""
<html><head><meta charset="utf-8"><title>Regimes Tables Index</title></head>
<body style="margin:20px;font-family:Inter,Arial,sans-serif;color:#222;">
  <h1>Regimes Tables — Consolidated</h1>
  <ul>{links}</ul>
</body></html>
"""
    )
    (out_dir / "index.html").write_text(index_html, encoding="utf-8")
    return out_dir
