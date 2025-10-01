
from __future__ import annotations
import argparse, json, polars as pl, os, glob
from blocks.alpha import AlphaBlock
from blocks.persist import save_parquet_with_meta

def fit_alpha():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    cfg = json.loads(open(args.config).read())
    df = AlphaBlock.fit_from_csv(config=cfg)
    save_parquet_with_meta(df, args.output, {"kind":"alpha"})
    print("\n=== Alpha (head) ===")
    print(df.head(10))

def build_crossalpha():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-folder", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    files = [f for f in glob.glob(os.path.join(args.input_folder, "*.parquet")) if os.path.basename(f).startswith("m")]
    if not files:
        raise SystemExit("no alpha parquet files found")
    df = pl.concat([pl.read_parquet(f) for f in files])
    save_parquet_with_meta(df, args.output, {"kind":"cross_alpha"})
    print("\n=== Cross-Alpha (head) ===")
    print(df.head(10))

def expected():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cross-alpha", required=True)
    ap.add_argument("--theta-surfaces", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--mode", choices=["full","production"], default="full",
                    help="full = all times; production = only latest time slice")
    ap.add_argument("--cadence-mins", type=int, default=30, help="data cadence in minutes (exec_time = time + lag*cadence; realization_time = exec_time + horizon*cadence)")
    args = ap.parse_args()
    ca = pl.read_parquet(args.cross_alpha)
    th = pl.read_parquet(args.theta_surfaces)

    # Ensure time is proper datetime
    if ca.schema.get("time") not in (pl.Datetime,):
        try:
            ca = ca.with_columns(pl.col("time").cast(pl.Datetime))
        except Exception:
            pass

    # 1) Join prob_on from theta (horizon-level demo)
    p = (
        th.filter(pl.col("theta_metric") == "prob_on")
          .rename({"theta_value": "prob"})
          .select(["horizon", "alloc", "prob"])
    )
    df = ca.join(p, on="horizon", how="left")

    # 2) Expected metrics (tall): expected_metric_value = metric_value * prob; expected_score if present
    df = df.with_columns([
        (pl.col("metric_value") * pl.col("prob").fill_null(0.5)).alias("expected_metric_value")
    ])
    if "score" in df.columns:
        df = df.with_columns((pl.col("score") * pl.col("prob").fill_null(0.5)).alias("expected_score"))
    # delta per metric row
    df = df.with_columns((pl.col("expected_metric_value") - pl.col("metric_value")).alias("delta_metric_value"))

    # 3) Execution/realization time semantics (explicit):
    #    exec_time = time + lag*cadence; realization_time = exec_time + horizon*cadence
    cadence_sec = int(args.cadence_mins * 60)
    df = df.with_columns([
        (pl.col("time") + pl.duration(seconds=cadence_sec) * pl.col("lag")).alias("exec_time"),
        (pl.col("time") + pl.duration(seconds=cadence_sec) * (pl.col("lag") + pl.col("horizon"))).alias("realization_time"),
    ])

    # Optionally keep only the latest slice (production snapshot)
    if args.mode == "production":
        t_latest = df.select(pl.col("time").max()).item()
        df = df.filter(pl.col("time") == t_latest)

    # 4) Wide expected table: expected_<metric>, delta_<metric>
    from pathlib import Path
    id_cols = [
        "time","exec_time","realization_time",
        "model_id","model_version_id","model_owner_id","hyper_id",
        "target_universe","target_name","regime_id","horizon","lag",
        "alloc","prob"
    ]
    # expected values pivot
    w_exp = (
        df.pivot(values="expected_metric_value", index=id_cols, columns="metric_name", aggregate_function="first")
          .rename({c: f"expected_{c}" for c in df.select("metric_name").unique().to_series().to_list() if c in df.columns or True})
    )
    # delta values pivot
    w_del = (
        df.pivot(values="delta_metric_value", index=id_cols, columns="metric_name", aggregate_function="first")
          .rename({c: f"delta_{c}" for c in df.select("metric_name").unique().to_series().to_list() if c in df.columns or True})
    )
    # join wide tables and add expected_score if present
    wide = w_exp.join(w_del, on=id_cols, how="left")
    if "expected_score" in df.columns:
        wide = wide.join(df.select(id_cols + ["expected_score"]).unique(), on=id_cols, how="left")

    # Save narrow and wide
    save_parquet_with_meta(df, args.output, {"kind": "expected"})
    outp = Path(args.output)
    wide_path = outp.with_name(outp.stem + "_wide" + outp.suffix)
    save_parquet_with_meta(wide, str(wide_path), {"kind": "expected_wide"})

    print("\n=== Expected Surfaces (head) ===")
    cols_show = ["time","exec_time","realization_time","target_universe","target_name","regime_id","horizon","lag","metric_name","metric_value","prob","expected_metric_value","delta_metric_value"]
    if "expected_score" in df.columns:
        cols_show.append("expected_score")
    print(df.select([c for c in cols_show if c in df.columns]).head(10))

    # 5) Print key performance metric tables (latest slice per regime)
    try:
        t_latest = df.select(pl.max("time")).item()
        latest = df.filter(pl.col("time") == t_latest)
        metrics = ["t_stat","sharpe","ir","p_val"]
        regimes = latest.select("regime_id").unique().to_series().to_list()
        for reg in regimes:
            sub = latest.filter(pl.col("regime_id") == reg)
            print(f"\n=== Regime {reg}: Metric tables (latest) ===")
            for m in metrics:
                tab = (
                    sub.filter(pl.col("metric_name") == m)
                       .pivot(index="lag", columns="horizon", values="metric_value", aggregate_function="first")
                       .sort("lag")
                )
                print(f"-- {m} --")
                print(tab.head(10))
    except Exception:
        pass
    print("\n=== Expected (wide head) ===")
    print(wide.head(10))

if __name__ == "__main__":
    import sys
    cmd = os.path.basename(sys.argv[0])
    if cmd.endswith("fit-alpha"):
        fit_alpha()
    elif cmd.endswith("build-crossalpha"):
        build_crossalpha()
    elif cmd.endswith("expected"):
        expected()
    else:
        # multiplexer
        if len(sys.argv) < 2:
            print("Usage: cli.py [fit-alpha|build-crossalpha|expected] ...")
            raise SystemExit(2)
        sub = sys.argv[1]
        sys.argv = [sys.argv[0]] + sys.argv[2:]
        if sub == "fit-alpha":
            fit_alpha()
        elif sub == "build-crossalpha":
            build_crossalpha()
        elif sub == "expected":
            expected()
        else:
            raise SystemExit(f"Unknown subcommand {sub}")
