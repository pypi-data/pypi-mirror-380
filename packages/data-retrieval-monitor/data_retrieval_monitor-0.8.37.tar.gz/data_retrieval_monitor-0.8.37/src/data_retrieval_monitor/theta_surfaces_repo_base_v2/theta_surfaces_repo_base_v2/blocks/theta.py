
from __future__ import annotations
import polars as pl
from dataclasses import dataclass
import numpy as np

@dataclass
class ThetaConfig:
    regimes: list[str]  # unused in v2 derived/external mode; kept for compat
    horizons: list[int]
    base_transitions: dict[str, list[float]] | dict = None
    control_sensitivity: float = 0.0

@dataclass
class ThetaBlock:
    name: str
    cfg: ThetaConfig

    def surfaces_with_control(self, *, state_now: pl.DataFrame, alloc_grid: dict[str, list[float]], earliest_trade_in: int) -> pl.DataFrame:
        # Build prob_on/confidence surfaces per theta_state_id × horizon × alloc choice
        rows = []
        horizons = self.cfg.horizons
        cs = float(self.cfg.control_sensitivity or 0.0)
        for row in state_now.iter_rows(named=True):
            sid = row["theta_state_id"]
            for asset, grid in alloc_grid.items():
                for a in grid:
                    for h in horizons:
                        base = 0.6  # demo base prob
                        prob = base + cs * float(a) * min(1.0, h/120.0)
                        prob = max(0.0, min(1.0, prob))
                        conf = 1.0 - (2.0*prob*(1.0-prob))  # 1 - normalized entropy proxy
                        rows.append({
                            "theta_state_id": sid,
                            "asset": asset,
                            "alloc": a,
                            "horizon": h,
                            "theta_metric": "prob_on",
                            "theta_value": prob,
                            "earliest_trade_in": earliest_trade_in
                        })
                        rows.append({
                            "theta_state_id": sid,
                            "asset": asset,
                            "alloc": a,
                            "horizon": h,
                            "theta_metric": "confidence",
                            "theta_value": conf,
                            "earliest_trade_in": earliest_trade_in
                        })
        return pl.DataFrame(rows)
