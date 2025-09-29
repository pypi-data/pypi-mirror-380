from __future__ import annotations

from dash import Dash
import dash_bootstrap_components as dbc
import argparse, sys

from .config import load_config
from .dashboard import DashboardHost
from .inject import register_callbacks, register_ingest_routes
from .library import seed_all_tabs


def create_app(seed_count: int = 10, do_seed: bool = True):
    """
    Build the Dash app + host, wire routes/callbacks, and optionally seed demo data.
    Returns (app, flask_server, cfg).
    """
    cfg = load_config()
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.FLATLY],
        title=cfg.app_title,
        # avoids "allow_duplicate requires prevent_initial_call..." on startup
        prevent_initial_callbacks="initial_duplicate",
    )

    host = DashboardHost(app, cfg)
    app.layout = host.layout

    # REST routes + callbacks
    register_ingest_routes(app.server, host)
    register_callbacks(app, cfg, host)

    # Seed demo data so you always see something unless disabled
    if do_seed and (seed_count or 0) > 0:
        seed_all_tabs(host, num_per_tab=int(seed_count))

    return app, app.server, cfg


def _parse_cli(argv):
    p = argparse.ArgumentParser()
    p.add_argument("--host", default=None, help="Interface to bind (default 127.0.0.1)")
    p.add_argument("--port", default=None, type=int, help="Port to bind (default 8090)")
    p.add_argument("--debug", action="store_true", help="Run Flask/Dash in debug mode")
    p.add_argument("--seed", type=int, default=10,
                   help="Seed N demo items per tab at startup (0 disables)")
    p.add_argument("--no-seed", action="store_true",
                   help="Disable seeding regardless of --seed value")
    return p.parse_args(argv)


if __name__ == "__main__":
    args = _parse_cli(sys.argv[1:])
    app, server, cfg = create_app(
        seed_count=(0 if args.no_seed else (args.seed or 0)),
        do_seed=(not args.no_seed),
    )
    host_addr = args.host or "127.0.0.1"
    port = int(args.port or 8090)
    app.run(host=host_addr, port=port, debug=bool(args.debug))