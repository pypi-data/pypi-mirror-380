from dash import Dash
import dash_bootstrap_components as dbc
import argparse, sys

from .config import load_config
from .dashboard import DashboardHost
from .inject import register_callbacks, register_ingest_routes
from .library import seed_all_tabs

def create_app(do_seed: bool = True, seed_count: int = 10):
    cfg = load_config()

    app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY], title=cfg.app_title)
    host = DashboardHost(app, cfg)
    app.layout = host.layout

    register_ingest_routes(app.server, host)
    register_callbacks(app, cfg, host)

    if do_seed and (seed_count or 0) > 0:
        seed_all_tabs(host, num_per_tab=int(seed_count))

    return app, app.server, cfg

def _parse_cli(argv):
    p = argparse.ArgumentParser()
    p.add_argument("--host", default=None)
    p.add_argument("--port", default=None, type=int)
    p.add_argument("--no-seed", action="store_true")
    p.add_argument("--seed-count", default=10, type=int)
    return p.parse_args(argv)

if __name__ == "__main__":
    args = _parse_cli(sys.argv[1:])
    app, server, cfg = create_app(do_seed=not args.no_seed, seed_count=args.seed_count)
    print("Callback keys (filtered):")
    for k in sorted(app.callback_map):
        if "kpi-container" in k or "pie-" in k:
            print("  ", k)
    host = args.host or "127.0.0.1"
    port = int(args.port or 8090)
    app.run(host=host, port=port, debug=False)
