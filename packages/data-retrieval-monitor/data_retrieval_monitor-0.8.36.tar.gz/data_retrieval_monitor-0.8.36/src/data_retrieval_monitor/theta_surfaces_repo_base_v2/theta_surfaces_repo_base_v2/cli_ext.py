
from __future__ import annotations
import argparse, polars as pl, json
from blocks.persist import save_parquet_with_meta

def filter_crossalpha():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--threshold", type=float, default=0.0)
    ap.add_argument("--config", required=True, help="weights json for score: e.g., {'t_stat':1.0,'sharpe':0.5}")
    ap.add_argument("--topk", type=int, default=2)
    args = ap.parse_args()

    ca = pl.read_parquet(args.input)
    weights = json.loads(open(args.config).read())
    w = pl.DataFrame({"metric_name": list(weights.keys()), "w": list(weights.values())})
    sc = (ca.join(w, on="metric_name", how="left")
            .with_columns((pl.col("metric_value") * pl.col("w").fill_null(0.0)).alias("contrib"))
            .group_by(["model_id","target_universe","target_name","regime_id","horizon","lag"])
            .agg(pl.col("contrib").sum().alias("score")))
    ca2 = ca.join(sc, on=["model_id","target_universe","target_name","regime_id","horizon","lag"], how="left")

    # Split passed vs failed by threshold
    passed = ca2.filter(pl.col("score") >= args.threshold)
    failed = ca2.filter(pl.col("score") < args.threshold)

    # Sort everything that passed (global order by score desc, stable on keys)
    passed_sorted = passed.sort(["score","model_id","target_universe","target_name"], descending=[True,False,False,False])

    # Also produce a top-k per (model,target) view for convenience (no global sort required here)
    id_regime = ["model_id","target_universe","target_name","regime_id"]
    id_target = ["model_id","target_universe","target_name"]
    best_per_regime = (
        passed.group_by(id_regime)
              .agg(pl.max("score").alias("score_regime"))
    )
    ranked = (
        best_per_regime
        .with_columns(
            pl.col("score_regime")
              .rank(method="dense", descending=True)
              .over(id_target)
              .alias("rk")
        )
        .filter(pl.col("rk") <= args.topk)
        .select(id_regime)
    )
    topk_view = passed.join(ranked, on=id_regime, how="inner")

    # Save outputs: main = passed_sorted; also sidecars = *_topk, *_failed
    from pathlib import Path
    save_parquet_with_meta(passed_sorted, args.output, {"kind":"cross_alpha_passed_sorted"})
    outp = Path(args.output)
    save_parquet_with_meta(topk_view, str(outp.with_name(outp.stem + "_topk" + outp.suffix)), {"kind":"cross_alpha_passed_topk"})
    save_parquet_with_meta(failed,    str(outp.with_name(outp.stem + "_failed" + outp.suffix)), {"kind":"cross_alpha_failed"})

    print("\n=== Cross-Alpha (passed & sorted, head) ===")
    print(passed_sorted.head(10))
    print("\n=== Cross-Alpha (passed top-{} per model×target, head) ===".format(args.topk))
    print(topk_view.head(10))
    print("\n=== Cross-Alpha (failed < threshold, head) ===")
    print(failed.head(10))

def theta_from_crossalpha():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--theta-config", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--priority-mode", choices=["current_only","ordered"], default="current_only")
    args = ap.parse_args()

    ca = pl.read_parquet(args.input)
    cfg = json.loads(open(args.theta_config).read())
    cfg_horizons = cfg["theta_cfg"]["horizons"]
    cs = float(cfg["theta_cfg"].get("control_sensitivity", 0.2))
    alloc_grid = cfg.get("alloc_grid", {"AAPL":[-1.0,0.0,1.0]})
    # Harmonize horizons with what's present in Cross-Alpha
    ca_horizons = ca.select("horizon").unique().sort("horizon")["horizon"].to_list()
    # Use intersection if any overlap, otherwise fall back to CA horizons
    inter = sorted(list(set(cfg_horizons).intersection(set(ca_horizons))))
    horizons = inter if inter else ca_horizons

    # derive state from CA (best per model,target)
    id_cols = ["model_id","model_version_id","model_owner_id","hyper_id","target_universe","target_name","regime_id"]
    best = (ca.group_by(id_cols).agg(pl.max("score").alias("score"))
              .sort(["model_id","target_universe","target_name","score"], descending=[False,False,False,True]))
    state = best.with_columns([
        (pl.col("model_id")+":"+pl.col("target_universe")+":"+pl.col("target_name")+":"+pl.col("regime_id")).alias("theta_state_id")
    ])
    # build prob surfaces
    rows = []
    for r in state.iter_rows(named=True):
        for a in alloc_grid.get("AAPL", [-1.0,0.0,1.0]):
            for h in horizons:
                base = 0.6
                prob = max(0.0, min(1.0, base + cs * a * min(1.0, h/120.0)))
                rows += [
                    {"theta_state_id": r["theta_state_id"], "asset": "AAPL", "alloc": a, "horizon": h, "theta_metric": "prob_on", "theta_value": prob},
                    {"theta_state_id": r["theta_state_id"], "asset": "AAPL", "alloc": a, "horizon": h, "theta_metric": "confidence", "theta_value": 1.0 - (2.0*prob*(1-prob))},
                ]
    out = pl.DataFrame(rows)
    from blocks.persist import save_parquet_with_meta
    save_parquet_with_meta(out, args.output, {"kind":"theta_ctrl_v1"})
    print("\n=== Theta Control Surfaces (head) ===")
    print(out.head(10))

if __name__ == "__main__":
    import sys
    cmd = sys.argv[1]
    sys.argv = [sys.argv[0]] + sys.argv[2:]
    if cmd == "filter-crossalpha":
        filter_crossalpha()
    elif cmd == "theta-from-crossalpha":
        theta_from_crossalpha()
    else:
        raise SystemExit("Usage: cli_ext.py [filter-crossalpha|theta-from-crossalpha] ...")
