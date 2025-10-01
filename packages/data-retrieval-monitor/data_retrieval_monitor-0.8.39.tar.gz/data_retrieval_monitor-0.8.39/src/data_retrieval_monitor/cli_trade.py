
from __future__ import annotations
import argparse, polars as pl, json
from blocks.trader import TraderBlock, TraderConfig
from blocks.solver import BlockSolver, BlockSolverConfig

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--expected", required=True, help="Expected pre-trade surfaces (parquet)")
    ap.add_argument("--exposures", help="Factor exposures (parquet) for residual unwinding")
    ap.add_argument("--output", required=True, help="Output allocations parquet")
    ap.add_argument("--global-gross", type=float, default=2.0)
    ap.add_argument("--residual-universes", nargs="*", default=["US_EQ","UK_EQ"])
    args = ap.parse_args()

    expd = pl.read_parquet(args.expected)

    exposures = None
    if args.exposures:
        exposures = pl.read_parquet(args.exposures)

    # Two demo traders (US & UK)
    t_us = TraderBlock(cfg=TraderConfig(name="trader_us", universe="US_EQ", budget=1.0, max_gross=1.2, allow_short=True, residual_mode="auto", session_window=None),
                       exposures=exposures)
    t_uk = TraderBlock(cfg=TraderConfig(name="trader_uk", universe="UK_EQ", budget=1.0, max_gross=1.2, allow_short=True, residual_mode="auto", session_window=None),
                       exposures=exposures)

    solver = BlockSolver(cfg=BlockSolverConfig(name="global", max_total_gross=args.global_gross), traders=[t_us,t_uk])

    sigmap = {u:"residual" for u in args.residual_universes}
    allocs = solver.run(expected_surfaces=expd, signal_type_map=sigmap)
    allocs.write_parquet(args.output)
    print(allocs.head(20))

if __name__ == "__main__":
    main()
