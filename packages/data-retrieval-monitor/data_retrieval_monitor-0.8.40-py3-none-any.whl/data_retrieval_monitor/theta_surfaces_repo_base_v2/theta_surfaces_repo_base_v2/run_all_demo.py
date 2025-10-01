
from __future__ import annotations
import subprocess, sys, os, json, polars as pl, numpy as np, pathlib
import csv, datetime as dt, random as _rnd
def run(cmd, cwd=None):
    print('>>', ' '.join(cmd), '(cwd=' + (str(cwd) if cwd else os.getcwd()) + ')', flush=True)
    subprocess.check_call(cmd, cwd=cwd)

def here():
    return pathlib.Path(__file__).resolve().parent

def main():
    repo = here()
    tools = repo/'tools'/'gen_models.py'
    configs = repo/'configs'/'models'
    data_out = repo/'data_gen'
    alpha_out = data_out/'alpha'
    demo_out = repo/'demo_out'
    configs.mkdir(parents=True, exist_ok=True)
    data_out.mkdir(parents=True, exist_ok=True)
    alpha_out.mkdir(parents=True, exist_ok=True)
    demo_out.mkdir(parents=True, exist_ok=True)

    # 0) Generate 100 model configs & CSVs (if tools/gen_models.py missing, inline fallback)
    if tools.exists():
        run([sys.executable, str(tools), '--out', str(configs), '--data-out', str(data_out), '--n', '100'], cwd=str(repo))
    else:
        print('** WARNING: tools/gen_models.py missing, using inline fallback generator **')
        
        def gen_csv(path: str, n: int = 1000, start: str = "2024-01-01", freq_min: int = 5):
            t0 = dt.datetime.fromisoformat(start)
            rows = []
            for i in range(n):
                ts = t0 + dt.timedelta(minutes=i*freq_min)
                f1 = _rnd.gauss(0,1); f2 = _rnd.gauss(0,1); f3 = _rnd.gauss(0,1)
                base = 0.2*f1 + 0.1*f2 - 0.05*f3 + _rnd.gauss(0,0.5)
                h1 = base + _rnd.gauss(0,0.3)
                h3 = base*1.5 + _rnd.gauss(0,0.3)
                h5 = base*2.0 + _rnd.gauss(0,0.3)
                rows.append([ts.isoformat(), f1, f2, f3, h1, h3, h5])
            with open(path, 'w', newline='') as f:
                w = csv.writer(f); w.writerow(['time','f1','f2','f3','ret_1','ret_3','ret_5']); w.writerows(rows)
        def gen_model_cfg(path: str, *, model_id: str, owner: str, version: str, hyper: str, csv_path: str, universe: str, name: str, regime_id: str):
            cfg = {
                "identity": {"model_id": model_id, "model_owner_id": owner, "model_version_id": version, "hyper_id": hyper},
                "target": {"universe": universe, "name": name},
                "data": {"csv_path": csv_path, "time_col": "time", "feature_cols":["f1","f2","f3"], "horizon_cols":["ret_1","ret_3","ret_5"]},
                "model": {"lags":[0,1,2,3]},
                "regime_id": regime_id
            }
            pathlib.Path(path).write_text(json.dumps(cfg, indent=2))
        universes = ["US_EQ","UK_EQ"]; names = ["AAPL","MSFT","BARC","HSBA"]; owners = ["team_alpha","team_beta"]
        _rnd.seed(13)
        for i in range(100):
            uni = _rnd.choice(universes); nm = _rnd.choice(names); owner = _rnd.choice(owners)
            mid = f"m{i:03d}"; ver = "v1"; hyp = f"h{_rnd.randint(1,5)}"
            csvp = data_out/f"{mid}_{nm}.csv"; gen_csv(str(csvp), n=1200, start="2024-01-01", freq_min=5)
            rid = f"r{_rnd.randint(1,5)}"; cfgp = configs/f"{mid}_{nm}.json"
            gen_model_cfg(str(cfgp), model_id=mid, owner=owner, version=ver, hyper=hyp, csv_path=str(csvp), universe=uni, name=nm, regime_id=rid)

    # 1) Fit a sample of Alpha models and build Cross-Alpha end-to-end (path-safe, no external tests)
    cfg_files = sorted(list(configs.glob('*.json')))
    if not cfg_files:
        raise SystemExit(f"No model configs found under {configs}")
    # Fit first N models to keep the demo quick
    N = min(20, len(cfg_files))
    for p in cfg_files[:N]:
        outp = alpha_out / (p.stem + '.parquet')
        run([sys.executable, str(repo/'cli.py'), 'fit-alpha', '--config', str(p), '--output', str(outp)], cwd=str(repo))

    # Build Cross-Alpha from individual alpha parquet files
    ca_all = demo_out/'cross_alpha_many.parquet'
    run([sys.executable, str(repo/'cli.py'), 'build-crossalpha', '--input-folder', str(alpha_out), '--output', str(ca_all)], cwd=str(repo))

    # Filter/sort Cross-Alpha to select top regimes per model
    ca_filt = demo_out/'cross_alpha_many_filtered.parquet'
    run([sys.executable, str(repo/'cli_ext.py'), 'filter-crossalpha', '--input', str(ca_all), '--output', str(ca_filt), '--threshold', '0.0', '--config', str(repo/'configs'/'weights.json')], cwd=str(repo))

    # Derive Theta control surfaces from Cross-Alpha
    theta_ctrl = demo_out/'theta_ctrl_from_ca_many.parquet'
    run([sys.executable, str(repo/'cli_ext.py'), 'theta-from-crossalpha', '--input', str(ca_filt), '--theta-config', str(repo/'configs'/'theta_multi.json'), '--output', str(theta_ctrl)], cwd=str(repo))

    # Build Expected surfaces
    expected = demo_out/'expected_many.parquet'
    run([sys.executable, str(repo/'cli.py'), 'expected', '--cross-alpha', str(ca_filt), '--theta-surfaces', str(theta_ctrl), '--output', str(expected)], cwd=str(repo))

    # 2) Time-varying exposures for unwinding (aligned to expected times)
    assets = ['AAPL','MSFT','BARC','HSBA']; factors = ['MKT','SIZE','VALUE']
    exp_times = pl.read_parquet(str(expected)).select('time').unique().sort('time')['time'].to_list()
    rows = []
    rng = _rnd.Random(42)
    for t in exp_times:
        for a in assets:
            for f in factors:
                base = {'MKT': 0.2, 'SIZE': -0.1, 'VALUE': 0.05}.get(f, 0.0)
                jitter = rng.uniform(-0.05, 0.05)
                rows.append((t, a, f, base + jitter))
    ex = pl.DataFrame({'time':[r[0] for r in rows], 'asset_id':[r[1] for r in rows], 'factor_id':[r[2] for r in rows], 'exposure':[r[3] for r in rows]})
    (repo/'demo').mkdir(parents=True, exist_ok=True)
    ex.write_parquet(str(repo/'demo'/'exposures.parquet'))

    # 3) Trade using expected surfaces
    run([sys.executable, str(repo/'cli_trade.py'),
         '--expected', str(expected),
         '--exposures', str(repo/'demo'/'exposures.parquet'),
         '--output', str(demo_out/'allocs_demo.parquet'),
         '--global-gross', '2.0',
         '--residual-universes', 'US_EQ', 'UK_EQ'], cwd=str(repo))

    al = pl.read_parquet(str(demo_out/'allocs_demo.parquet'))
    print('Allocations (head):'); print(al.head(20))

if __name__ == '__main__':
    main()
