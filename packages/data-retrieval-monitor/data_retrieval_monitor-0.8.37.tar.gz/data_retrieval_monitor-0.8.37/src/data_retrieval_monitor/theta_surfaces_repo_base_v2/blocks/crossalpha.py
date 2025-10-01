
from __future__ import annotations
from pathlib import Path
import os
from typing import Iterable, Optional
import polars as pl

ID_KEYS = [
    "time","model_id","model_version_id","model_owner_id","hyper_id",
    "target_universe","target_name","regime_id","horizon","lag"
]

class CrossAlphaBlock:
    """Polars-first Cross-Alpha aggregator with lazy evaluation.

    Stores sources as LazyFrames (scan_parquet or provided frames). Provides methods to
    compute composite scores, expected surfaces, pivot tables, and summaries without
    eagerly loading all data unless requested.
    """
    def __init__(self) -> None:
        self._sources: list[pl.LazyFrame] = []
        self._lf_cache: Optional[pl.LazyFrame] = None

    # ---- Ingestion ----
    def extend_parquet(self, paths: Iterable[str]) -> "CrossAlphaBlock":
        for p in paths:
            if os.path.exists(p):
                self._sources.append(pl.scan_parquet(p))
        self._lf_cache = None
        return self

    def extend_frames(self, frames: Iterable[pl.DataFrame | pl.LazyFrame]) -> "CrossAlphaBlock":
        for f in frames:
            lf = f.lazy() if isinstance(f, pl.DataFrame) else f
            self._sources.append(lf)
        self._lf_cache = None
        return self

    # ---- Accessors ----
    def master_lazy(self) -> pl.LazyFrame:
        if self._lf_cache is not None:
            return self._lf_cache
        if not self._sources:
            self._lf_cache = pl.DataFrame({}).lazy()
        else:
            self._lf_cache = pl.concat(self._sources)
        return self._lf_cache

    def to_frame(self) -> pl.DataFrame:
        return self.master_lazy().collect()

    # ---- Operations ----
    def with_scores(self, weights: dict[str, float], *, out_col: str = "score") -> pl.LazyFrame:
        """Compute composite per-ID score and attach back to tall rows.

        score(group) = sum_m w[m] * metric_value[m]
        where groups are keyed by ID_KEYS.
        """
        lf = self.master_lazy()
        w = pl.DataFrame({"metric_name": list(weights.keys()), "w": list(weights.values())}).lazy()
        contrib = lf.join(w, on="metric_name", how="left").with_columns(
            (pl.col("metric_value") * pl.col("w").fill_null(0.0)).alias("__contrib__")
        )
        sc = contrib.group_by(ID_KEYS).agg(pl.col("__contrib__").sum().alias(out_col))
        return lf.join(sc, on=ID_KEYS, how="left")

    def expected(self,
                 *,
                 prob: pl.LazyFrame | pl.DataFrame,
                 join_on: Iterable[str] = ("horizon",),
                 prob_col: str = "prob",
                 cadence_mins: int = 30) -> pl.LazyFrame:
        """Attach expected_metric_value and delta_metric_value using prob surfaces and add timing columns.

        - Expects tall rows with (metric_name, metric_value).
        - prob should have columns including `join_on` and a numeric `prob_col`.
        - exec_time = time + lag*cadence; realization_time = exec_time + horizon*cadence
        """
        lf = self.master_lazy()
        plf = prob.lazy() if isinstance(prob, pl.DataFrame) else prob
        df = lf.join(plf, on=list(join_on), how="left")
        cadence_sec = int(cadence_mins) * 60
        out = (
            df.with_columns([
                (pl.col("metric_value") * pl.col(prob_col).fill_null(0.5)).alias("expected_metric_value"),
                (pl.col("metric_value") * 0 + 1).alias("__one__"),  # ensure numeric
            ])
              .with_columns((pl.col("expected_metric_value") - pl.col("metric_value")).alias("delta_metric_value"))
              .with_columns([
                  (pl.col("time") + pl.duration(seconds=cadence_sec) * pl.col("lag")).alias("exec_time"),
                  (pl.col("time") + pl.duration(seconds=cadence_sec) * (pl.col("lag") + pl.col("horizon"))).alias("realization_time"),
              ])
              .drop(["__one__"])
        )
        return out

    def metrics_wide(self, *, index_cols: list[str] | None = None) -> pl.DataFrame:
        """Pivot tall metrics to wide columns. Eager collect for pivot."""
        if index_cols is None:
            index_cols = ID_KEYS
        df = self.to_frame()
        w = df.pivot(values="metric_value", index=index_cols, columns="metric_name", aggregate_function="first")
        if "score" in df.columns and "score" not in w.columns:
            w = w.join(df.select(index_cols + ["score"]).unique(), on=index_cols, how="left")
        return w

    # ---- Utilities ----
    def summary(self, *, head: int = 5) -> str:
        try:
            df = self.master_lazy().head(head).collect()
            total = self.master_lazy().select(pl.len()).collect().item()
        except Exception:
            df = pl.DataFrame({}); total = 0
        s = [f"CrossAlphaBlock: sources={len(self._sources)} rows≈{total}\n"]
        if total:
            s.append(str(df))
        return "".join(s)

    def save(self, path: str | os.PathLike, *, kind: str = "cross_alpha") -> None:
        from .persist import save_parquet_with_meta
        df = self.to_frame()
        save_parquet_with_meta(df, str(path), {"kind": kind})

    def slice_regime(self, regime_id: str) -> pl.LazyFrame:
        """Return a lazy slice filtered to a single regime_id."""
        return self.master_lazy().filter(pl.col("regime_id") == regime_id)

def combine_alpha_parquets(paths: list[str]) -> pl.DataFrame:
    """Back-compat helper; prefer CrossAlphaBlock.extend_parquet()."""
    cab = CrossAlphaBlock().extend_parquet(paths)
    return cab.to_frame()

def build_from_folder(folder: str | os.PathLike) -> pl.DataFrame:
    """Back-compat helper; prefer CrossAlphaBlock with extend_parquet()."""
    folder = Path(folder)
    files = [str(f) for f in folder.glob("*.parquet") if f.name.startswith("m")]
    return CrossAlphaBlock().extend_parquet(files).to_frame()

def with_scores(df: pl.DataFrame, weights: dict[str, float], *, out_col: str = "score") -> pl.DataFrame:
    """Add a composite score = sum_k w_k * metric_k. p-values are mapped to -log(p) implicitly by negative weights.
    Expects tall format (metric_name, metric_value). Returns df with an added 'score' per (model,target,regime,horizon,lag,time).
    """
    w = pl.DataFrame({"metric_name": list(weights.keys()), "w": list(weights.values())})
    sc = (df.join(w, on="metric_name", how="left")
            .with_columns((pl.col("metric_value") * pl.col("w").fill_null(0.0)).alias("contrib"))
            .group_by(["time","model_id","model_version_id","model_owner_id","hyper_id","target_universe","target_name","regime_id","horizon","lag"]) 
            .agg(pl.col("contrib").sum().alias(out_col)))
    return df.join(sc, on=["time","model_id","model_version_id","model_owner_id","hyper_id","target_universe","target_name","regime_id","horizon","lag"], how="left")

def metrics_wide(df: pl.DataFrame, *, index_cols: list[str] | None = None) -> pl.DataFrame:
    """Pivot tall metric rows to wide columns for convenience."""
    if index_cols is None:
        index_cols = ["time","model_id","model_version_id","model_owner_id","hyper_id","target_universe","target_name","regime_id","horizon","lag"]
    w = df.pivot(values="metric_value", index=index_cols, columns="metric_name", aggregate_function="first")
    # keep score if already computed in df
    if "score" in df.columns and "score" not in w.columns:
        w = w.join(df.select(index_cols + ["score"]).unique(), on=index_cols, how="left")
    return w

def metric_table(df: pl.DataFrame, *, metric: str, value_col: str = "metric_value") -> pl.DataFrame:
    """Lag x horizon table for a given metric (mean aggregate)."""
    sub = df.filter(pl.col("metric_name") == metric)
    return sub.pivot(index="lag", columns="horizon", values=value_col, aggregate_function="mean").sort("lag")
