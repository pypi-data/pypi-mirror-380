
from __future__ import annotations
import polars as pl
from dataclasses import dataclass, field
from .trader import TraderBlock, TraderConfig

@dataclass
class BlockSolverConfig:
    name: str = "solver"
    max_total_gross: float | None = None
    share_proxy_portfolios: bool = True  # allow sharing proxy/mimic outputs between traders

@dataclass
class BlockSolver:
    cfg: BlockSolverConfig
    traders: list[TraderBlock] = field(default_factory=list)

    def run(self, *, expected_surfaces: pl.DataFrame, signal_type_map: dict[str,str] | None = None) -> pl.DataFrame:
        """Fan-out expected surfaces to each trader (by universe), aggregate allocations, and enforce global caps.
        expected_surfaces must include columns: target_universe, target_name, [metric_expected|score], time, horizon, lag
        signal_type_map: optional map universe-> {'raw'|'residual'}
        Output: combined allocations with columns: trader, asset_id, w_adj
        """
        results = []
        for t in self.traders:
            sig = (signal_type_map or {}).get(t.cfg.universe, "raw")
            df_u = expected_surfaces.filter(pl.col("target_universe")==t.cfg.universe)
            if df_u.is_empty():
                continue
            w = t.decide(expected_surfaces=df_u, signal_type=sig, time_col="time")
            results.append(w.with_columns([pl.lit(t.cfg.name).alias("trader")]))
        if not results:
            return pl.DataFrame({"trader":[], "asset_id":[], "w_adj":[]})
        allocs = pl.concat(results)

        # Global gross cap
        if self.cfg.max_total_gross is not None:
            gross = allocs.select(pl.col("w_adj").abs().sum()).item()
            if gross > self.cfg.max_total_gross + 1e-12 and gross > 0:
                scale = self.cfg.max_total_gross / gross
                allocs = allocs.with_columns((pl.col("w_adj") * scale).alias("w_adj"))
        return allocs
