from dash import Dash, dcc
import dash_bootstrap_components as dbc
import argparse, sys

from .config import load_config
from .dashboard import DashboardHost
from .inject import register_callbacks, register_ingest_routes
from .library import seed_all_tabs

def create_app():
    cfg = load_config()
    app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY], title=cfg.app_title)
    host = DashboardHost(app, cfg)
    app.layout = host.layout

    # Routes + callbacks
    register_ingest_routes(app.server, host)
    register_callbacks(app, cfg, host)

    # Seed demo data so you always see something
    seed_all_tabs(host, num_per_tab=10)

    return app, app.server, cfg

def _parse_cli(argv):
    p = argparse.ArgumentParser()
    p.add_argument("--host", default=None)
    p.add_argument("--port", default=None, type=int)
    return p.parse_args(argv)

if __name__ == "__main__":
    args = _parse_cli(sys.argv[1:])
    app, server, cfg = create_app()
    host = args.host or "127.0.0.1"
    port = int(args.port or 8090)
    app.run(host=host, port=port, debug=False)