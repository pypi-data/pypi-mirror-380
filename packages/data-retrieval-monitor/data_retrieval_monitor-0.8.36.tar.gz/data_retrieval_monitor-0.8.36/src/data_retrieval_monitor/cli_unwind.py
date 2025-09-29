
from __future__ import annotations
import argparse, polars as pl, json
from blocks.unwind import ResidualUnwinder

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    pm = sub.add_parser("preview-mimic")
    pm.add_argument("--exposures", required=True)
    pm.add_argument("--output", required=True)
    pm.add_argument("--allow", action="store_true", help="grant reveal_mimic permission")

    na = sub.add_parser("neutralize")
    na.add_argument("--exposures", required=True)
    na.add_argument("--desired", required=True)
    na.add_argument("--output", required=True)
    na.add_argument("--budget", type=float, default=None)

    tf = sub.add_parser("target-factor")
    tf.add_argument("--exposures", required=True)
    tf.add_argument("--desired", required=True)
    tf.add_argument("--target", required=True, help="JSON file with {factor_id: exposure}")
    tf.add_argument("--output", required=True)
    tf.add_argument("--budget", type=float, default=None)

    args = ap.parse_args()
    if args.cmd == "preview-mimic":
        df = pl.read_parquet(args.exposures) if args.exposures.endswith(".parquet") else pl.read_csv(args.exposures)
        rw = ResidualUnwinder(permissions={"reveal_mimic": args.allow})
        out = rw.preview_mimic_portfolios(exposures=df)
        out.write_parquet(args.output)
        print(out.head(10))

    elif args.cmd == "neutralize":
        ex = pl.read_parquet(args.exposures) if args.exposures.endswith(".parquet") else pl.read_csv(args.exposures)
        de = pl.read_parquet(args.desired) if args.desired.endswith(".parquet") else pl.read_csv(args.desired)
        rw = ResidualUnwinder()
        out = rw.neutralize_to_factors(exposures=ex, desired_weights=de, budget=args.budget)
        out.write_parquet(args.output)
        print(out.head(10))

    elif args.cmd == "target-factor":
        ex = pl.read_parquet(args.exposures) if args.exposures.endswith(".parquet") else pl.read_csv(args.exposures)
        de = pl.read_parquet(args.desired) if args.desired.endswith(".parquet") else pl.read_csv(args.desired)
        tgt = json.loads(open(args.target).read())
        rw = ResidualUnwinder()
        out = rw.target_factor_exposure(exposures=ex, desired_weights=de, target=tgt, budget=args.budget)
        out.write_parquet(args.output)
        print(out.head(10))

if __name__ == "__main__":
    main()
