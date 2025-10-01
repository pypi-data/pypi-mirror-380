# dataset_dashboard/components/table.py
from typing import List, Optional, Tuple
from dash import html, dcc
import dash_bootstrap_components as dbc

from dataset_dashboard.components.compute import best_status
from dataset_dashboard.constants import DATA_STAGES, rgb_for_tab


class TableComponent:
    """
    - Data tab: Dataset + ONLY the visible_stages columns (defaults to all DATA_STAGES).
    - All tab: Data(name)+4 stages + Features(name,Status) + Alphas(name,Status) + Strategies(name,Status).
              Stage filter (if provided) controls which Data-stage columns are shown in the All view’s Data sub-table.
    - Other tabs (features/alphas/strategies): Name + single Status column
    """

    def __init__(self, log_linker, clipboard_fallback_open: bool):
        self.linker = log_linker
        self.fallback_open = bool(clipboard_fallback_open)

    @staticmethod
    def _shade(tab: str, status: Optional[str], alpha=0.18):
        if not status:
            return {"backgroundColor": "#FFFFFF"}
        r, g, b = rgb_for_tab(tab).get(status, (230, 230, 230))
        return {"backgroundColor": f"rgba({r},{g},{b},{alpha})"}

    def _clipboard_button(self, text: str):
        icon = html.Span(
            "📄",
            title=f"Copy: {text}",
            style={"display": "inline-block", "fontSize": "12px", "opacity": 0.9, "marginLeft": "6px", "cursor": "pointer"},
        )
        overlay = dcc.Clipboard(
            content=text,
            title="Copy",
            style={"position": "absolute", "left": 0, "top": 0, "width": "1.6em", "height": "1.6em",
                   "opacity": 0.01, "zIndex": 5, "cursor": "pointer", "border": 0, "background": "transparent"},
        )
        return html.Span([icon, overlay], style={"position": "relative", "display": "inline-block", "marginRight": "10px"})

    def _chunk_badge_and_links(self, tab: str, ch: dict, idx: int, prefix: str):
        label = f"{prefix}{idx}"
        st = (ch.get("status") or "other")
        proc = ch.get("proc")
        raw = ch.get("log")
        href = self.linker.href_for(raw)

        badge = html.Span(
            label,
            title=str(label),
            style={"display": "inline-block", "padding": "2px 6px", "borderRadius": "8px",
                   "fontSize": "12px", "marginRight": "6px", **self._shade(tab, st, 0.35)},
        )
        bits = [badge]

        if proc:
            bits.append(html.A("p", href=proc, target="_blank", title="proc",
                               style={"marginRight": "6px", "textDecoration": "underline"}))
        if href:
            bits.append(html.A("l", href=href, target="_blank", title="open log",
                               style={"marginRight": "0", "textDecoration": "underline", "fontSize": "12px"}))
            bits.append(self._clipboard_button(str(raw or href)))
        elif raw:
            bits.append(self._clipboard_button(str(raw)))
        return bits

    def _chunk_block(self, tab: str, chunks: List[dict], chunks_per_line: int, prefix: str):
        if not chunks:
            return html.I("—", className="text-muted")
        cpl = max(1, int(chunks_per_line or 6))
        lines = []
        for i in range(0, len(chunks), cpl):
            seg = chunks[i:i+cpl]
            seg_nodes = []
            for j, ch in enumerate(seg):
                seg_nodes.extend(self._chunk_badge_and_links(tab, ch, idx=i + j, prefix=prefix))
            lines.append(html.Div(seg_nodes, style={"whiteSpace": "nowrap"}))
        return html.Div(lines, style={"display": "grid", "rowGap": "2px"})

    # ---------- helpers ----------
    @staticmethod
    def _safe(map_like: Optional[dict]) -> dict:
        return map_like or {}

    def _tabs_root(self, tree: dict) -> Optional[dict]:
        if isinstance(tree, dict) and "tabs" in tree and isinstance(tree["tabs"], dict):
            return tree
        return None

    def _lookup_name_and_leaf(self, tabs_root: dict, tab_name: str, owner: str, mode: str, dataset: str):
        jobs = self._safe(self._safe(self._safe(tabs_root.get("tabs")).get(tab_name)).get("jobs"))
        # try exact owner/mode first
        name_map = self._safe(jobs.get(owner, {}).get(mode) or jobs.get(owner, {}).get("live", {}))
        if isinstance(name_map, dict) and dataset in name_map:
            leaf = self._safe(self._safe(name_map.get(dataset)).get("status"))
            return dataset, {"counts": self._safe(leaf.get("counts")), "chunks": list(self._safe(leaf.get("chunks")))}
        # fallback: search other owners/modes for same dataset key
        for o_map in jobs.values():
            for m_map in self._safe(o_map).values():
                if dataset in self._safe(m_map):
                    node = self._safe(m_map.get(dataset))
                    leaf = self._safe(node.get("status"))
                    return dataset, {"counts": self._safe(leaf.get("counts")), "chunks": list(self._safe(leaf.get("chunks")))}
        return None, {"counts": {}, "chunks": []}

    # --------------------------------------------------------------
    def build(
        self,
        tree: dict,
        labels: dict,
        owner: Optional[str],
        groups_per_row: int,
        entries_sorted: List[Tuple],
        chunks_per_line: int,
        tab: str = "data",
        visible_stages: Optional[List[str]] = None,  # controls which DATA columns are shown
    ) -> html.Div:
        gpr = max(1, min(int(groups_per_row or 2), 6))
        is_data = (tab == "data")
        is_all = (tab == "all")
        tabs_root = self._tabs_root(tree) if is_all else None

        # Which DATA stage columns to show
        if is_data:
            want = [s.strip().lower() for s in (visible_stages or DATA_STAGES)]
            vis_stages = [s for s in DATA_STAGES if s in set(want)] or list(DATA_STAGES)
        else:
            vis_stages = list(DATA_STAGES)

        # ---- header
        head_cells: List[html.Th] = []
        if is_data:
            per_group = [html.Th("Dataset", style={"whiteSpace": "nowrap"})] + \
                        [html.Th(s.title(), style={"whiteSpace": "nowrap"}) for s in vis_stages]
        elif is_all:
            per_group = [
                html.Th("Data", style={"whiteSpace": "nowrap"}),
                html.Th("Archive", style={"whiteSpace": "nowrap"}),
                html.Th("Stage", style={"whiteSpace": "nowrap"}),
                html.Th("Enrich", style={"whiteSpace": "nowrap"}),
                html.Th("Consolidate", style={"whiteSpace": "nowrap"}),
                html.Th("Features", style={"whiteSpace": "nowrap"}),
                html.Th("Status", style={"whiteSpace": "nowrap"}),
                html.Th("Alphas", style={"whiteSpace": "nowrap"}),
                html.Th("Status", style={"whiteSpace": "nowrap"}),
                html.Th("Strategies", style={"whiteSpace": "nowrap"}),
                html.Th("Status", style={"whiteSpace": "nowrap"}),
            ]
        else:
            per_group = [html.Th("Name", style={"whiteSpace": "nowrap"}),
                         html.Th("Status", style={"whiteSpace": "nowrap"})]
        for _ in range(gpr):
            head_cells.extend(per_group)
        head = html.Thead(html.Tr(head_cells))

        def _chunked(lst: List, n: int) -> List[List]:
            return [lst[i:i+n] for i in range(0, len(lst), n)]

        body_rows: List[html.Tr] = []
        for row_groups in _chunked(entries_sorted, gpr):
            tds: List[html.Td] = []
            for _, own, md, dn, d_map in row_groups:
                if is_data:
                    # only selected DATA columns
                    stage_stat = {stg: best_status(self._safe(self._safe(d_map.get(stg)).get("counts")), "data")
                                  for stg in vis_stages}
                    cells = [html.Td(dn, style={"fontWeight": "600", "whiteSpace": "nowrap"})]
                    for stg in vis_stages:
                        leaf = self._safe(d_map.get(stg))
                        cells.append(
                            html.Td(
                                self._chunk_block("data", list(self._safe(leaf.get("chunks"))), chunks_per_line, prefix="c"),
                                style={"verticalAlign": "top", "padding": "6px 10px", "whiteSpace": "nowrap",
                                       **self._shade("data", stage_stat.get(stg), 0.18)}))
                    tds.extend(cells)

                elif is_all:
                    # left: all four data stages (All view always shows all four)
                    stage_stat = {stg: best_status(self._safe(self._safe(d_map.get(stg)).get("counts")), "data")
                                  for stg in DATA_STAGES}
                    cells = [html.Td(dn, style={"fontWeight": "600", "whiteSpace": "nowrap"})]
                    for stg in DATA_STAGES:
                        leaf = self._safe(d_map.get(stg))
                        cells.append(
                            html.Td(
                                self._chunk_block("data", list(self._safe(leaf.get("chunks"))), chunks_per_line, prefix="c"),
                                style={"verticalAlign": "top", "padding": "6px 10px", "whiteSpace": "nowrap",
                                       **self._shade("data", stage_stat.get(stg), 0.18)}))
                    # right: single-status tabs
                    if tabs_root:
                        for tname, prefix in (("features", "f"), ("alphas", "a"), ("strategies", "s")):
                            nm, leaf = self._lookup_name_and_leaf(tabs_root, tname, own, md, dn)
                            bs = best_status(self._safe(leaf.get("counts")), tname)
                            cells.append(html.Td(nm or "—", style={"whiteSpace": "nowrap", "fontWeight": "600"}))
                            cells.append(
                                html.Td(
                                    self._chunk_block(tname, list(self._safe(leaf.get("chunks"))), chunks_per_line, prefix=prefix),
                                    style={"verticalAlign": "top", "padding": "6px 10px", "whiteSpace": "nowrap",
                                           **self._shade(tname, bs, 0.18)}))
                    else:
                        cells.extend([html.Td("—"), html.Td("—")] * 3)
                    tds.extend(cells)

                else:
                    # single-status tabs
                    leaf = self._safe(d_map.get("status"))
                    bs = best_status(self._safe(leaf.get("counts")), tab)
                    tds.extend([
                        html.Td(dn, style={"fontWeight": "600", "whiteSpace": "nowrap"}),
                        html.Td(
                            self._chunk_block(tab, list(self._safe(leaf.get("chunks"))), chunks_per_line, prefix=self._prefix_for_tab(tab)),
                            style={"verticalAlign": "top", "padding": "6px 10px", "whiteSpace": "nowrap",
                                   **self._shade(tab, bs, 0.18)}),
                    ])

            # do not pad non-All tabs
            if is_all and len(row_groups) < gpr:
                for _ in range(gpr - len(row_groups)):
                    tds.extend([html.Td("") for _ in range(11)])

            body_rows.append(html.Tr(tds))

        if not body_rows:
            span = (1 + (len(vis_stages) if is_data else 0)) * gpr if is_data else (11 * gpr if is_all else 2 * gpr)
            body_rows = [html.Tr(html.Td("No data", colSpan=span, className="text-muted"))]

        return dbc.Table(
            [head, html.Tbody(body_rows)],
            bordered=True, hover=False, size="sm", className="mb-1",
            style={"tableLayout": "auto", "width": "auto", "display": "inline-table", "marginRight": "10ch"},
        )

    def _prefix_for_tab(self, tab: str) -> str:
        return {"data": "c", "features": "f", "alphas": "a", "strategies": "s"}.get((tab or "").lower(), "c")