
from __future__ import annotations
import polars as pl
from dataclasses import dataclass, field
from .unwind import ResidualUnwinder
from .calendar import in_session, session_slice

@dataclass
class TraderConfig:
    name: str
    universe: str
    budget: float = 1.0
    risk_aversion: float | None = None
    max_gross: float | None = None
    max_turnover: float | None = None
    allow_short: bool = True
    session_window: str | None = None   # e.g., "open+30m" or "preclose-30m_to_close"
    # residual handling
    residual_mode: str = "auto"         # {"auto","off"} if "auto", use unwind when signal_type == "residual"
    reveal_mimic: bool = False          # permissions for preview

@dataclass
class TraderBlock:
    cfg: TraderConfig
    exposures: pl.DataFrame | None = None   # optional factor exposure table for unwinding
    positions_prev: pl.DataFrame | None = None  # previous holdings for turnover control

    def _gate_session(self, df: pl.DataFrame, *, time_col: str):
        if self.cfg.session_window:
            return session_slice(df, time_col=time_col, universe=self.cfg.universe, window=self.cfg.session_window)
        return in_session(df, time_col=time_col, universe=self.cfg.universe)

    def _apply_limits(self, weights: pl.DataFrame) -> pl.DataFrame:
        w = weights
        if not self.cfg.allow_short:
            w = w.with_columns(pl.col("w_adj").clip(lower=0.0))
        if self.cfg.max_gross is not None:
            gross = (w.select(pl.col("w_adj").abs().sum()).item())
            if gross > self.cfg.max_gross + 1e-12 and gross > 0:
                scale = self.cfg.max_gross / gross
                w = w.with_columns((pl.col("w_adj") * scale).alias("w_adj"))
        # normalize to budget
        s = w.select(pl.col("w_adj").sum()).item()
        if abs(s - self.cfg.budget) > 1e-9 and s != 0:
            w = w.with_columns((pl.col("w_adj") * (self.cfg.budget / s)).alias("w_adj"))
        return w

    def decide(self, *, expected_surfaces: pl.DataFrame, signal_type: str = "raw", time_col: str = "time") -> pl.DataFrame:
        """Convert expected metric surfaces into desired allocations.
        expected_surfaces columns (example): time, target_name, metric_expected, horizon, lag, score, etc.
        Strategy (demo):
          - For each target, pick horizon/lag with the best 'metric_expected' (highest t-stat/score)
          - Convert to a provisional desired weight in [-1,1] via tanh(score)
        Then:
          - If 'signal_type' == 'residual' and residual_mode=='auto', run ResidualUnwinder to produce tradable weights.
          - Apply limits (gross, shorts, budget, etc.).
        Returns: DataFrame with columns: asset_id (target_name), w_adj
        """
        df = expected_surfaces
        df = self._gate_session(df, time_col=time_col)
        if df.is_empty():
            return pl.DataFrame({"asset_id": [], "w_adj": []})

        # score proxy: prefer provided 'metric_expected' else 'score' if present
        metric = "metric_expected" if "metric_expected" in df.columns else ("score" if "score" in df.columns else None)
        if metric is None:
            raise ValueError("expected_surfaces needs 'metric_expected' or 'score'")

        # Ensure time is datetime
        if df.schema.get(time_col) not in (pl.Datetime,):
            try:
                df = df.with_columns(pl.col(time_col).cast(pl.Datetime))
            except Exception:
                pass
        # Use the latest timestamp available (single decision slice)
        t_latest = df.select(pl.col(time_col).max()).item()
        df_latest = df.filter(pl.col(time_col) == t_latest)
        # Ignore lag 0 (cannot act immediately)
        if "lag" in df_latest.columns:
            df_latest = df_latest.filter(pl.col("lag") >= 1)
        if df_latest.is_empty():
            return pl.DataFrame({"asset_id": [], "w_adj": []})

        # argmax per asset within the latest slice
        best = (df_latest.group_by("target_name")
                  .agg(pl.all().sort_by(metric, descending=True).first())
                  .select(["target_name", metric])
                  .rename({"target_name":"asset_id", metric:"alpha"}))

        # map alpha -> provisional weight [-1,1]
        w0 = best.with_columns((pl.col("alpha").tanh()).alias("w0")).select(["asset_id","w0"])

        if signal_type == "residual" and self.cfg.residual_mode == "auto":
            if self.exposures is None:
                # Without exposures, fall back to raw weights
                weights = w0.rename({"w0":"w_adj"})
            else:
                # If exposures are time-varying, pick the latest slice
                exp = self.exposures
                if "time" in exp.columns:
                    # ensure timezone consistency between exposures.time and df_latest[time_col]
                    dtype_exp = exp.schema.get("time")
                    dtype_df = df_latest.schema.get(time_col)
                    tz = getattr(dtype_df, "time_zone", None)
                    if tz:
                        try:
                            if getattr(dtype_exp, "time_zone", None) is None:
                                exp = exp.with_columns(pl.col("time").dt.replace_time_zone(tz))
                            elif getattr(dtype_exp, "time_zone", None) != tz:
                                exp = exp.with_columns(pl.col("time").dt.convert_time_zone(tz))
                        except Exception:
                            pass
                    # align to latest decision time
                    # if multiple times <= t_latest exist, choose exact match first, else take max <= t_latest
                    exp_exact = exp.filter(pl.col("time") == t_latest)
                    if exp_exact.is_empty():
                        t_avail = exp.filter(pl.col("time") <= t_latest).select(pl.max("time")).item()
                        exp = exp.filter(pl.col("time") == t_avail) if t_avail is not None else exp.head(0)
                    else:
                        exp = exp_exact
                # Unwind to factor-neutral tradable weights
                rw = ResidualUnwinder(permissions={"reveal_mimic": self.cfg.reveal_mimic})
                weights = rw.neutralize_to_factors(exposures=exp, desired_weights=w0, budget=self.cfg.budget)
        else:
            weights = w0.rename({"w0":"w_adj"})

        # Limits & normalization
        weights = self._apply_limits(weights)
        return weights

    def decide_over_time(self, *, expected_surfaces: pl.DataFrame, signal_type: str = "raw", time_col: str = "time") -> pl.DataFrame:
        """Compute allocations for every timepoint instead of a single latest slice.

        Strategy mirrors `decide` per time slice:
          - Gate to session
          - Ignore lag < 1
          - For each (time, target), pick the best horizon/lag by metric_expected or score
          - Map alpha -> provisional weight via tanh(alpha)
          - If residual requested and exposures provided, neutralize per time using ResidualUnwinder
          - Apply per-time limits (gross, shorts, budget)

        Returns DataFrame: columns [time, asset_id, w_adj]
        """
        df = expected_surfaces
        df = self._gate_session(df, time_col=time_col)
        if df.is_empty():
            return pl.DataFrame({"time": [], "asset_id": [], "w_adj": []})

        # metric to use
        metric = "metric_expected" if "metric_expected" in df.columns else ("score" if "score" in df.columns else None)
        if metric is None:
            raise ValueError("expected_surfaces needs 'metric_expected' or 'score'")

        # Ensure datetime type
        if df.schema.get(time_col) not in (pl.Datetime,):
            try:
                df = df.with_columns(pl.col(time_col).cast(pl.Datetime))
            except Exception:
                pass

        # ignore lag < 1
        if "lag" in df.columns:
            df = df.filter(pl.col("lag") >= 1)
        if df.is_empty():
            return pl.DataFrame({"time": [], "asset_id": [], "w_adj": []})

        # best per (time, asset)
        # Uses dense sort and first to emulate argmax per group
        best = (
            df.group_by([time_col, "target_name"])  # choose best horizon/lag per time, asset
              .agg(pl.all().sort_by(metric, descending=True).first())
              .select([time_col, "target_name", metric])
              .rename({"target_name": "asset_id", metric: "alpha"})
        )
        # provisional weights via tanh
        w0 = best.with_columns((pl.col("alpha").tanh()).alias("w0")).select([time_col, "asset_id", "w0"]).sort([time_col, "asset_id"])

        # Residual neutralization (if requested) requires solving per time slice
        if signal_type == "residual" and self.cfg.residual_mode == "auto" and self.exposures is not None:
            rows: list[pl.DataFrame] = []
            times = w0.select(pl.col(time_col).unique()).to_series().sort().to_list()
            rw = ResidualUnwinder(permissions={"reveal_mimic": self.cfg.reveal_mimic})
            exp = self.exposures
            # normalize timezone of exposures to match df time column
            if "time" in exp.columns:
                dtype_exp = exp.schema.get("time"); dtype_df = df.schema.get(time_col)
                tz = getattr(dtype_df, "time_zone", None)
                if tz:
                    try:
                        if getattr(dtype_exp, "time_zone", None) is None:
                            exp = exp.with_columns(pl.col("time").dt.replace_time_zone(tz))
                        elif getattr(dtype_exp, "time_zone", None) != tz:
                            exp = exp.with_columns(pl.col("time").dt.convert_time_zone(tz))
                    except Exception:
                        pass
            for t in times:
                w0_t = w0.filter(pl.col(time_col) == t).select(["asset_id", "w0"])  # desired raw weights at time t
                if "time" in (exp.columns if exp is not None else []):
                    exp_exact = exp.filter(pl.col("time") == t)
                    if exp_exact.is_empty():
                        t_avail = exp.filter(pl.col("time") <= t).select(pl.max("time")).item()
                        exp_t = exp.filter(pl.col("time") == t_avail) if t_avail is not None else exp.head(0)
                    else:
                        exp_t = exp_exact
                else:
                    exp_t = exp
                wt = rw.neutralize_to_factors(exposures=exp_t, desired_weights=w0_t, budget=self.cfg.budget)
                wt = self._apply_limits(wt).with_columns(pl.lit(t).alias(time_col))
                rows.append(wt.select([time_col, "asset_id", "w_adj"]))
            return pl.concat(rows).sort([time_col, "asset_id"]) if rows else pl.DataFrame({"time": [], "asset_id": [], "w_adj": []})

        # Vectorized per-time limits for raw (or no exposures)
        weights = w0.rename({"w0": "w_adj"})
        # allow_short gate
        if not self.cfg.allow_short:
            weights = weights.with_columns(pl.col("w_adj").clip(lower_bound=0.0))
        # max_gross scaling per time
        if self.cfg.max_gross is not None:
            gross = weights.group_by(time_col).agg((pl.col("w_adj").abs().sum()).alias("__gross__"))
            weights = weights.join(gross, on=time_col, how="left").with_columns(
                pl.when((pl.col("__gross__") > self.cfg.max_gross) & (pl.col("__gross__") > 0))
                  .then(pl.col("w_adj") * (pl.lit(self.cfg.max_gross) / pl.col("__gross__")))
                  .otherwise(pl.col("w_adj")).alias("w_adj")
            ).drop("__gross__")
        # budget normalization per time
        if self.cfg.budget is not None:
            s = weights.group_by(time_col).agg((pl.col("w_adj").sum()).alias("__sum__"))
            weights = weights.join(s, on=time_col, how="left").with_columns(
                pl.when((pl.col("__sum__") != 0))
                  .then(pl.col("w_adj") * (pl.lit(self.cfg.budget) / pl.col("__sum__")))
                  .otherwise(pl.col("w_adj")).alias("w_adj")
            ).drop("__sum__")
        return weights
