# dataset_dashboard/inject.py
from __future__ import annotations
from datetime import datetime
from typing import List, Optional, Dict
import pytz
from dash import dcc
from dash import Input, Output, State

from .constants import TAB_IDS, DATA_STAGES, status_order_for_tab
from .components import compute  # best_status, make_sort_key, aggregate_counts, filtered_stage_counts
from .utils import to_local_str


def _subtree_for_tab(state: dict, tab: str) -> dict:
    tabs = state.get("tabs")
    if isinstance(tabs, dict) and tab in tabs:
        return tabs[tab] or {}
    return state


def register_callbacks(app, cfg, host):
    # heartbeat
    app.layout.children.append(dcc.Interval(id="interval", interval=cfg.refresh_ms, n_intervals=0))

    store = host.store
    pie = host.pies
    table = host.table

    @app.callback(
        # KPIs
        Output("kpi-container", "children"),
        # options
        Output("owner-filter", "options"),
        Output("mode-filter", "options"),
        Output("stage-filter", "options"),
        Output("status-filter", "options"),
        # pies
        Output("pie-stage", "figure"),
        Output("pie-archive", "figure"),
        Output("pie-enrich", "figure"),
        Output("pie-consolidate", "figure"),
        Output("pie-overview", "figure"),
        # table + status + interval
        Output("table-title", "children"),
        Output("table-container", "children"),
        Output("now-indicator", "children"),
        Output("interval", "interval"),
        # visibilities
        Output("advanced-controls", "style"),
        Output("pie-stage", "style"),
        Output("pie-archive", "style"),
        Output("pie-enrich", "style"),
        Output("pie-consolidate", "style"),
        Output("pie-overview", "style"),
        # inputs
        Input("interval", "n_intervals"),
        Input("main-tabs", "value"),
        Input("owner-filter", "value"), Input("mode-filter", "value"),
        Input("stage-filter", "value"), Input("status-filter", "value"),
        Input("table-groups", "value"), Input("chunks-per-line", "value"), Input("sort-by", "value"),
        State("interval", "interval"),
        prevent_initial_call=False
    )
    def refresh(_n, tab, owner_sel, mode_sel, stage_filter, status_filter,
            groups_per_row, chunks_per_line, sort_by, cur_interval):
        tab = (tab or "data").lower()
        state = store.state()
        tree = _subtree_for_tab(state, tab)

        # options
        owner_opts, mode_opts = store.list_filters_for_tab(tab)
        # non-data tabs have no stage dropdown
        stage_opts = (
            [{"label": s.title(), "value": s} for s in DATA_STAGES] if tab == "data" else []
        )
        status_vocab = status_order_for_tab(tab)
        status_opts = [{"label": s, "value": s} for s in status_vocab]

        # KPIs
        k_counts = compute.aggregate_counts(state, tab)
        kpi_children = host.kpis.render(tab, status_vocab, k_counts, per_row=3)

        # pies
        empty_fig = {"data": [], "layout": {"margin": {"l": 0, "r": 0, "t": 0, "b": 0}}}
        if tab == "data":
            figs = {
                "stage":       pie.figure("data", "Stage",
                                        compute.filtered_stage_counts(state, owner_sel, mode_sel, "stage", "data"),
                                        labels_order=status_vocab),
                "archive":     pie.figure("data", "Archive",
                                        compute.filtered_stage_counts(state, owner_sel, mode_sel, "archive", "data"),
                                        labels_order=status_vocab),
                "enrich":      pie.figure("data", "Enrich",
                                        compute.filtered_stage_counts(state, owner_sel, mode_sel, "enrich", "data"),
                                        labels_order=status_vocab),
                "consolidate": pie.figure("data", "Consolidate",
                                        compute.filtered_stage_counts(state, owner_sel, mode_sel, "consolidate", "data"),
                                        labels_order=status_vocab),
            }
            fig_overview = empty_fig
            adv_style = {"display": "block"}
            p_stage_sty = p_archive_sty = p_enrich_sty = p_conso_sty = {"display": "block"}
            p_overview_sty = {"display": "none"}
        else:
            overall = compute.aggregate_counts(state, tab)
            fig_overview = pie.figure(tab, "Overview", overall, labels_order=status_vocab)
            figs = {"stage": empty_fig, "archive": empty_fig, "enrich": empty_fig, "consolidate": empty_fig}
            adv_style = {"display": "none"}
            p_stage_sty = p_archive_sty = p_enrich_sty = p_conso_sty = {"display": "none"}
            p_overview_sty = {"display": "block"}

        # table
        owner_sel = owner_sel or "All"
        mode_sel = mode_sel or "All"
        sort_by = sort_by or "name_asc"
        want_owner = None if str(owner_sel).lower() in ("", "all") else str(owner_sel).lower()
        want_mode = None if str(mode_sel).lower() in ("", "all") else str(mode_sel).lower()

        # stage buckets for filtering/sorting
        buckets = DATA_STAGES if tab == "data" else ["status"]
        sel_stages = (stage_filter or DATA_STAGES) if tab == "data" else ["status"]
        sel_status = status_filter or []

        entries = []
        jobs = tree.get("jobs", {})
        for own, o_map in jobs.items():
            if want_owner and own != want_owner:
                continue
            for md, m_map in o_map.items():
                if want_mode and md != want_mode:
                    continue
                for dn, d_map in m_map.items():
                    # ---- FIXED FILTER: match if ANY of the selected statuses has count > 0
                    if sel_status:
                        found = False
                        for stg in buckets:
                            leaf = (d_map.get(stg) or {"counts": {}})
                            counts = leaf.get("counts") or {}
                            # counts might miss absent statuses, so default to 0
                            for s in sel_status:
                                if int(counts.get(s, 0) or 0) > 0:
                                    found = True
                                    break
                            if found:
                                break
                        if not found:
                            continue
                    # sort key unchanged
                    sk = compute.make_sort_key(tab, d_map, dn, own, md, sel_stages, sort_by)
                    entries.append((sk, own, md, dn, d_map))
        entries.sort(key=lambda x: x[0])

        labels = tree.get("meta", {}).get("owner_labels", {})
        table_comp = host.table.build(
            tree, labels, owner_sel, mode_sel, int(groups_per_row or 1),
            entries, int(chunks_per_line or 999_999), tab=tab
        )

        # titles/lines
        table_title = {"data": "Datasets", "features": "Features", "alphas": "Alphas", "strategies": "Strategies"}.get(tab, "Items")
        meta = tree.get("meta", {}) or {}
        env_label = meta.get("env") or cfg.environment_label or "-"
        last_ing = to_local_str(meta.get("last_ingest_at"), cfg.timezone)
        tz = pytz.timezone(cfg.timezone)
        refreshed = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")
        status_line = f"Environment: {env_label} | Last Ingested: {last_ing} | Refreshed: {refreshed}"
        interval_ms = int(cur_interval or cfg.refresh_ms)

        return (
            kpi_children,
            owner_opts, mode_opts, stage_opts, status_opts,
            figs["stage"], figs["archive"], figs["enrich"], figs["consolidate"], fig_overview,
            table_title, table_comp, status_line, interval_ms,
            adv_style, p_stage_sty, p_archive_sty, p_enrich_sty, p_conso_sty, p_overview_sty,
        )

def register_ingest_routes(server, host):
    """
    Accepts:
      1) {"tab": "data|features|alphas|strategies", "snapshot":[...], "meta": {...}}
      2) {"tabs": {"data": {"snapshot":[...], "meta": {...}}, "features": {...}, ...}}
      3) [ ... ]  (legacy list → defaults to data)
    We canonicalize chunk.status per tab: unknown statuses -> "other".
    """
    from flask import request, jsonify

    def _canon_status(tab: str, raw: Optional[str]) -> str:
        t = (tab or "data").lower()
        vocab = set(status_order_for_tab(t))
        if raw is None:
            return "other"
        s = str(raw).strip()
        if t == "data":
            s = s.lower()
        return s if s in vocab else "other"

    def _canon_items(tab: str, items: List[dict]) -> List[dict]:
        t = (tab or "data").lower()
        out: List[dict] = []
        for it in items or []:
            chs = []
            for ch in (it.get("chunks") or []):
                ch = dict(ch or {})
                ch["status"] = _canon_status(t, ch.get("status"))
                chs.append(ch)
            it2 = dict(it)
            it2["chunks"] = chs
            out.append(it2)
        return out

    def _apply(tab: str, items: List[dict], meta: Optional[dict]):
        host.store.apply_snapshot_with_meta_tab(tab, items, meta or {})

    @server.route("/ingest_snapshot", methods=["POST"])
    def ingest_snapshot():
        try:
            body = request.get_json(force=True, silent=False)

            # Legacy: raw list → data tab
            if isinstance(body, list):
                items = _canon_items("data", body)
                _apply("data", items, {})
                return jsonify({"ok": True})

            if not isinstance(body, dict):
                return jsonify({"ok": False, "error": "Unsupported payload"}), 400

            # Multi-tab bundle
            tabs_pack = body.get("tabs")
            if isinstance(tabs_pack, dict):
                for t, pack in tabs_pack.items():
                    if not isinstance(pack, dict):
                        continue
                    tab = str(t).lower()
                    items = pack.get("snapshot") or pack.get("items") or []
                    meta = pack.get("meta") or {}
                    items = _canon_items(tab, list(items or []))
                    _apply(tab, items, dict(meta or {}))
                return jsonify({"ok": True})

            # Single-tab payload
            tab = str(body.get("tab") or "data").lower()
            items = body.get("snapshot") or body.get("items") or []
            meta = body.get("meta") or {}
            if not isinstance(items, list):
                return jsonify({"ok": False, "error": "Send {snapshot:[...]} or a JSON array"}), 400
            items = _canon_items(tab, list(items or []))
            _apply(tab, items, dict(meta or {}))
            return jsonify({"ok": True})

        except Exception as e:
            return jsonify({"ok": False, "error": str(e)}), 400

    @server.route("/__debug__/store_summary", methods=["GET"])
    def store_summary():
        from flask import jsonify
        st = host.store.state()
        tabs = st.get("tabs", {})
        out: Dict[str, Dict] = {"tabs": {}}
        for t, tree in tabs.items():
            jobs = tree.get("jobs", {}) or {}
            n = 0
            for o_map in jobs.values():
                for m_map in o_map.values():
                    n += len(m_map)
            meta = tree.get("meta", {}) or {}
            owners = sorted(jobs.keys())
            modes = set()
            for o_map in jobs.values():
                modes.update(o_map.keys())
            out["tabs"][t] = {
                "datasets_total": n,
                "meta": {
                    "env": meta.get("env"),
                    "last_ingest_at": meta.get("last_ingest_at"),
                    "owner_labels": meta.get("owner_labels", {}),
                },
                "modes": sorted(modes),
                "owners": owners,
                "updated_at": tree.get("updated_at"),
            }
        return jsonify(out)