
from __future__ import annotations
import argparse, json, os, pathlib, random, csv, datetime as dt

def ensure_dir(p: str):
    pathlib.Path(p).mkdir(parents=True, exist_ok=True)

def gen_csv(path: str, n: int = 1000, start: str = "2024-01-01", freq_min: int = 5, seed: int | None = None):
    # simple synthetic series with horizons h1,h3,h5 and 3 features
    t0 = dt.datetime.fromisoformat(start)
    rows = []
    if seed is not None:
        random.seed(seed)
    for i in range(n):
        ts = t0 + dt.timedelta(minutes=i*freq_min)
        f1 = random.gauss(0,1)
        f2 = random.gauss(0,1)
        f3 = random.gauss(0,1)
        base = 0.2*f1 + 0.1*f2 - 0.05*f3 + random.gauss(0,0.5)
        h1 = base + random.gauss(0,0.3)
        h3 = base*1.5 + random.gauss(0,0.3)
        h5 = base*2.0 + random.gauss(0,0.3)
        rows.append([ts.isoformat(), f1, f2, f3, h1, h3, h5])
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["time","f1","f2","f3","ret_1","ret_3","ret_5"])
        w.writerows(rows)

def gen_model_cfg(path: str, *, model_id: str, owner: str, version: str, hyper: str, csv_path: str, universe: str, name: str, regime_id: str):
    cfg = {
        "identity": {"model_id": model_id, "model_owner_id": owner, "model_version_id": version, "hyper_id": hyper},
        "target": {"universe": universe, "name": name},
        "data": {
            "csv_path": csv_path, "time_col":"time",
            "feature_cols":["f1","f2","f3"],
            "horizon_cols":["ret_1","ret_3","ret_5"]
        },
        "model": {"lags":[0,1,2,3]},
        "regime_id": regime_id
    }
    pathlib.Path(path).write_text(json.dumps(cfg, indent=2))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)       # configs folder
    ap.add_argument("--data-out", required=True)  # csv folder
    ap.add_argument("--n", type=int, default=100) # number of models
    args = ap.parse_args()

    ensure_dir(args.out); ensure_dir(args.data_out)

    universes = ["US_EQ","UK_EQ"]
    names = ["AAPL","MSFT","BARC","HSBA"]
    owners = ["team_alpha","team_beta"]
    random.seed(13)

    for i in range(args.n):
        uni = random.choice(universes)
        nm = random.choice(names)
        owner = random.choice(owners)
        mid = f"m{i:03d}"
        ver = "v1"
        hyp = f"h{random.randint(1,5)}"
        csvp = os.path.join(args.data_out, f"{mid}_{nm}.csv")
        # different seed per model to diversify outputs
        gen_csv(csvp, n=1200, start="2024-01-01", freq_min=5, seed=13 + i)
        rid = f"r{random.randint(1,5)}"
        cfgp = os.path.join(args.out, f"{mid}_{nm}.json")
        gen_model_cfg(cfgp, model_id=mid, owner=owner, version=ver, hyper=hyp, csv_path=csvp, universe=uni, name=nm, regime_id=rid)

if __name__ == "__main__":
    main()
