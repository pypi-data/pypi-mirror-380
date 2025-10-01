# dataset_dashboard/inject.py
from __future__ import annotations

from datetime import datetime
from typing import List, Optional, Dict

import pytz
from dash import Input, Output, State, html

import dataset_dashboard.components.compute as compute
from dataset_dashboard.constants import DATA_STAGES, status_order_for_tab
from dataset_dashboard.utils import to_local_str


def _subtree_for_tab(state: dict, tab: str) -> dict:
    tabs = state.get("tabs", {}) or {}
    return tabs.get(tab) or {}


def register_callbacks(app, cfg, host):
    store = host.store
    pie = host.pies

    @app.callback(
        # KPIs
        Output("kpi-container", "children"),

        # Filter option lists
        Output("owner-filter", "options"),
        Output("stage-filter", "options"),
        Output("status-filter", "options"),

        # Pies
        Output("pie-stage", "figure"),
        Output("pie-archive", "figure"),
        Output("pie-enrich", "figure"),
        Output("pie-consolidate", "figure"),
        Output("pie-overview", "figure"),

        # Table + footer + refresh
        Output("table-title", "children"),
        Output("table-container", "children"),
        Output("now-indicator", "children"),
        Output("interval", "interval"),

        # Visibilities
        Output("advanced-controls", "style"),
        Output("pie-stage", "style"),
        Output("pie-archive", "style"),
        Output("pie-enrich", "style"),
        Output("pie-consolidate", "style"),
        Output("pie-overview", "style"),

        # Inputs
        Input("interval", "n_intervals"),
        Input("main-tabs", "value"),
        Input("owner-filter", "value"),
        Input("stage-filter", "value"),   # controls DATA columns on Data tab and All tab’s Data sub-table
        Input("status-filter", "value"),  # present on every tab (incl. All, using union vocab)
        Input("table-groups", "value"),
        Input("chunks-per-line", "value"),
        Input("sort-by", "value"),
        State("interval", "interval"),
        prevent_initial_call=False,
    )
    def refresh(_n, tab, owner_sel, stage_filter,
                status_filter, groups_per_row, chunks_per_line, sort_by, cur_interval):

        tab = (tab or "data").lower()
        state = store.state()
        # Precompute per-tab aggregate counts once

        tab_for_subtree = "data" if tab == "all" else tab
        tree = _subtree_for_tab(state, tab_for_subtree)

        # --- Filter option lists ---
        owner_opts = store.list_filters_for_tab(tab_for_subtree)

        # Stage filter: show on Data and All (affects columns)
        if tab in ("data", "all"):
            stage_opts = [{"label": s.title(), "value": s} for s in DATA_STAGES]
        else:
            stage_opts = []

        # Status vocab and options:
        if tab == "all":
            # union of all tab vocabularies
            union_vocab = list({
                *status_order_for_tab("data"),
                *status_order_for_tab("features"),
                *status_order_for_tab("alphas"),
                *status_order_for_tab("strategies"),
            })
            union_vocab.sort()
            status_vocab = union_vocab
        else:
            status_vocab = status_order_for_tab(tab_for_subtree)
        status_opts = [{"label": s, "value": s} for s in status_vocab]

        # --- KPIs & pies ---
        empty_fig = {"data": [], "layout": {"margin": {"l": 0, "r": 0, "t": 0, "b": 0}}}

        if tab == "data":
            # KPIs for Data
            k_counts = compute.aggregate_counts(state, "data")
            kpi_children = host.kpis.render("data", status_vocab, k_counts, per_row=3)

            # ✅ Overview figure for Data tab (actually show it)
            fig_overview = pie.figure(
                "data", "Overview",
                compute.aggregate_counts(state, "data"),
                labels_order=status_vocab,
            )

            # Stage pies (ids are fixed; visual order is controlled in components/html.py)
            figs = {
                "stage": pie.figure(
                    "data", "Stage",
                    compute.filtered_stage_counts(state, owner_sel, "stage", "data"),
                    labels_order=status_vocab,
                ),
                "archive": pie.figure(
                    "data", "Archive",
                    compute.filtered_stage_counts(state, owner_sel, "archive", "data"),
                    labels_order=status_vocab,
                ),
                "enrich": pie.figure(
                    "data", "Enrich",
                    compute.filtered_stage_counts(state, owner_sel, "enrich", "data"),
                    labels_order=status_vocab,
                ),
                "consolidate": pie.figure(
                    "data", "Consolidate",
                    compute.filtered_stage_counts(state, owner_sel, "consolidate", "data"),
                    labels_order=status_vocab,
                ),
            }

            # Show all five pies on the Data tab (Overview included)
            adv_style = {"display": "block"}
            p_stage_sty = p_archive_sty = p_enrich_sty = p_conso_sty = {"display": "block"}
            p_overview_sty = {"display": "block"}

        elif tab == "all":
            # Show "Data" FIRST on the page. The HTML renders pies in the order:
            # pie-archive, pie-stage, pie-enrich, pie-consolidate.
            # So we assign Data -> pie-archive, Features -> pie-stage, etc.
            figs = {
                "archive": pie.figure("data", "Data",
                                    compute.aggregate_counts(state, "data"),
                                    labels_order=status_order_for_tab("data")),
                "stage": pie.figure("features", "Features",
                                    compute.aggregate_counts(state, "features"),
                                    labels_order=status_order_for_tab("features")),
                "enrich": pie.figure("alphas", "Alphas",
                                    compute.aggregate_counts(state, "alphas"),
                                    labels_order=status_order_for_tab("alphas")),
                "consolidate": pie.figure("strategies", "Strategies",
                                        compute.aggregate_counts(state, "strategies"),
                                        labels_order=status_order_for_tab("strategies")),
            }
            fig_overview = empty_fig
            adv_style = {"display": "block"}  # keep Stage filter visible here if desired
            p_stage_sty = p_archive_sty = p_enrich_sty = p_conso_sty = {"display": "block"}
            p_overview_sty = {"display": "none"}

            # KPIs (unchanged): union vocab, summed counts across tabs
            totals: Dict[str, int] = {}
            for t in ("data", "features", "alphas", "strategies"):
                cc = compute.aggregate_counts(state, t) or {}
                for k, v in cc.items():
                    totals[k] = totals.get(k, 0) + int(v or 0)
            kpi_children = host.kpis.render("all", status_vocab, totals, per_row=3)

        else:
            overall = compute.aggregate_counts(state, tab)
            kpi_children = host.kpis.render(tab, status_vocab, overall, per_row=3)
            fig_overview = pie.figure(tab, "Overview", overall, labels_order=status_vocab)
            figs = {"stage": empty_fig, "archive": empty_fig, "enrich": empty_fig, "consolidate": empty_fig}
            adv_style = {"display": "none"}
            p_stage_sty = p_archive_sty = p_enrich_sty = p_conso_sty = {"display": "none"}
            p_overview_sty = {"display": "block"}

        # --- Build table rows (status filter filters rows on EVERY tab) ---
        owner_sel = owner_sel or "All"
        sort_by = sort_by or "name_asc"
        want_owner = None if str(owner_sel).lower() in ("", "all") else str(owner_sel).lower()
        sel_status = list(status_filter or [])

        def _filter_entries(sub_tree: dict, sub_tab: str) -> List[tuple]:
            buckets = DATA_STAGES if sub_tab == "data" else ["status"]
            sel_stages_for_sort = DATA_STAGES if sub_tab == "data" else ["status"]
            entries = []
            jobs = (sub_tree.get("jobs") or {})
            for own, o_map in jobs.items():
                if want_owner and own != want_owner:
                    continue
                for md, m_map in (o_map or {}).items():
                    for dn, d_map in (m_map or {}).items():
                        if sel_status:
                            keep = False
                            for stg in buckets:
                                counts = ((d_map.get(stg) or {}).get("counts")) or {}
                                if any(int(counts.get(s, 0) or 0) > 0 for s in sel_status):
                                    keep = True
                                    break
                            if not keep:
                                continue
                        sk = compute.make_sort_key(sub_tab, d_map, dn, own, sel_stages_for_sort, sort_by)
                        entries.append((sk, own, md, dn, d_map))
            entries.sort(key=lambda x: x[0])
            return entries

        labels = tree.get("meta", {}).get("owner_labels", {})
        groups_per_row = int((groups_per_row or 2))
        chunks_per_line = int((chunks_per_line or 6))

        if tab != "all":
            entries = _filter_entries(tree, tab)
            visible_stages = list(stage_filter or DATA_STAGES) if tab == "data" else None
            table_comp = host.table.build(
                tree, labels, owner_sel,
                groups_per_row, entries, chunks_per_line,
                tab=tab,
                visible_stages=visible_stages,  # Data tab: control columns; others ignore
            )
            table_title = {"data": "Datasets",
                           "features": "Features",
                           "alphas": "Alphas",
                           "strategies": "Strategies"}.get(tab, "Items")
        else:
            table_title = "All"
            table_comps = []
            for sub_tab in ["data", "features", "alphas", "strategies"]:
                sub_tree = _subtree_for_tab(state, sub_tab)
                entries = _filter_entries(sub_tree, sub_tab)
                sub_labels = sub_tree.get("meta", {}).get("owner_labels", {})
                sub_comp = host.table.build(
                    sub_tree, sub_labels, owner_sel,
                    groups_per_row, entries, chunks_per_line,
                    tab=sub_tab,
                    # All tab: let the stage filter control Data sub-table columns too:
                    visible_stages=list(stage_filter or DATA_STAGES) if sub_tab == "data" else None,
                )
                sub_title = "Datasets" if sub_tab == "data" else sub_tab.title()
                table_comps.append(html.Div([html.H4(sub_title), sub_comp],
                                            style={"marginRight": "30px", "flex": "0 0 auto"}))
            table_comp = html.Div(table_comps,
                                  style={"display": "flex", "flexDirection": "row", "flexWrap": "nowrap", "width": "max-content"})

        # --- footer + refresh ---
        meta = tree.get("meta", {}) or {}
        env_label = meta.get("env") or cfg.environment_label or "-"
        last_ing = to_local_str(meta.get("last_ingest_at"), cfg.timezone)
        tz = pytz.timezone(cfg.timezone)
        refreshed = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")
        status_line = f"Environment: {env_label} | Last Ingested: {last_ing} | Refreshed: {refreshed}"
        interval_ms = int(cur_interval or cfg.refresh_ms)

        return (
            kpi_children,
            owner_opts, stage_opts, status_opts,
            figs["stage"], figs["archive"], figs["enrich"], figs["consolidate"], fig_overview,
            table_title, table_comp, status_line, interval_ms,
            adv_style, p_stage_sty, p_archive_sty, p_enrich_sty, p_conso_sty, p_overview_sty,
        )


def register_ingest_routes(server, host):
    from flask import request, jsonify

    def _canon_status(tab: str, raw: Optional[str]) -> str:
        from dataset_dashboard.constants import status_order_for_tab
        vocab = set(status_order_for_tab(tab))
        s = (raw or "other")
        s = s.lower() if tab == "data" else s
        return s if s in vocab else "other"

    def _canon_items(tab: str, items: List[dict]) -> List[dict]:
        out: List[dict] = []
        for it in items or []:
            chs = []
            for ch in (it.get("chunks") or []):
                ch = dict(ch or {})
                ch["status"] = _canon_status(tab, ch.get("status"))
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
            if isinstance(body, list):
                items = _canon_items("data", body)
                _apply("data", items, {})
                return jsonify({"ok": True})
            if not isinstance(body, dict):
                return jsonify({"ok": False, "error": "Unsupported payload"}), 400
            tabs_pack = body.get("tabs")
            if isinstance(tabs_pack, dict):
                for t, pack in tabs_pack.items():
                    if not isinstance(pack, dict):
                        continue
                    tab = str(t).lower()
                    if tab == "all":
                        continue
                    items = pack.get("snapshot") or pack.get("items") or []
                    meta = pack.get("meta") or {}
                    items = _canon_items(tab, list(items or []))
                    _apply(tab, items, dict(meta or {}))
                return jsonify({"ok": True})
            tab = str(body.get("tab") or "data").lower()
            if tab == "all":
                return jsonify({"ok": False, "error": "tab 'all' is synthetic"}), 400
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