from typing import List, Optional, Tuple
from dash import html, dcc
import dash_bootstrap_components as dbc
from .compute import best_status
from ..constants import DATA_STAGES, status_order_for_tab, rgb_for_tab

class TableComponent:
    """
    Intrinsic-width table; compact chunk badges with proc/log + clipboard.
    Data tab renders Archive/Stage/Enrich/Consolidate.
    Other tabs render a single 'Status' column.
    """
    def __init__(self, log_linker, clipboard_fallback_open: bool):
        self.linker = log_linker
        self.fallback_open = bool(clipboard_fallback_open)

    @staticmethod
    def _shade(tab: str, status: Optional[str], alpha=0.18):
        if not status: 
            return {"backgroundColor":"#FFFFFF"}
        r,g,b = rgb_for_tab(tab).get(status, (230,230,230))
        return {"backgroundColor": f"rgba({r},{g},{b},{alpha})"}

    def _clipboard_button(self, text: str):
        icon = html.Span("📄", title=f"Copy: {text}",
                         style={"display":"inline-block","fontSize":"12px","opacity":0.9,
                                "marginLeft":"6px","cursor":"pointer"})
        overlay = dcc.Clipboard(
            content=text, title="Copy",
            style={"position":"absolute","left":0,"top":0,"width":"1.6em","height":"1.6em",
                   "opacity":0.01,"zIndex":5,"cursor":"pointer","border":0,"background":"transparent"}
        )
        return html.Span([icon, overlay],
                         style={"position":"relative","display":"inline-block","marginRight":"10px"})

    def _chunk_badge_and_links(self, tab: str, ch: dict, idx: int, prefix: str):
        label = f"{prefix}{idx}"
        st  = (ch.get("status") or "other")
        proc = ch.get("proc")
        raw  = ch.get("log")
        href = self.linker.href_for(raw)

        badge = html.Span(
            label,
            title=str(label),
            style={"display":"inline-block","padding":"2px 6px","borderRadius":"8px",
                   "fontSize":"12px","marginRight":"6px", **self._shade(tab, st, 0.35)}
        )
        bits = [badge]

        if proc:
            bits.append(html.A("p", href=proc, target="_blank", title="proc",
                               style={"marginRight":"6px","textDecoration":"underline"}))

        if href:
            link = html.A("l", href=href, target="_blank", title="open log",
                          style={"marginRight":"0","textDecoration":"underline","fontSize":"12px"})
            bits.append(link)
            bits.append(self._clipboard_button(str(raw or href)))  # copy RAW path if present
        elif raw:
            bits.append(self._clipboard_button(str(raw)))

        return bits

    def _chunk_block(self, tab: str, chunks: List[dict], chunks_per_line: int, prefix: str):
        if not chunks:
            return html.I("—", className="text-muted")
        cpl = max(1, int(chunks_per_line or 999_999))
        lines = []
        for i in range(0, len(chunks), cpl):
            seg = chunks[i:i+cpl]
            seg_nodes = []
            for j, ch in enumerate(seg):
                seg_nodes.extend(self._chunk_badge_and_links(tab, ch, idx=i + j, prefix=prefix))
            lines.append(html.Div(seg_nodes, style={"whiteSpace":"nowrap"}))
        return html.Div(lines, style={"display":"grid","rowGap":"2px"})

    def build(self, tree: dict, labels: dict,
              owner: Optional[str], mode: Optional[str],
              groups_per_row: int, entries_sorted: List[Tuple],
              chunks_per_line: int, tab: str = "data") -> html.Div:
        gpr = max(1, min(int(groups_per_row or 1), 6))
        is_data = (tab == "data")
        prefix = self._prefix_for_tab(tab) 
        # header
        head_cells = []
        if is_data:
            for _ in range(gpr):
                head_cells.extend([html.Th("Dataset", style={"whiteSpace":"nowrap"})] +
                                  [html.Th(s.title(), style={"whiteSpace":"nowrap"}) for s in DATA_STAGES])
        else:
            for _ in range(gpr):
                head_cells.extend([html.Th("Name", style={"whiteSpace":"nowrap"}),
                                   html.Th("Status", style={"whiteSpace":"nowrap"})])
        head = html.Thead(html.Tr(head_cells))

        def _chunked(lst: List, n: int) -> List[List]:
            return [lst[i:i+n] for i in range(0, len(lst), n)]

        body_rows = []
        for row_groups in _chunked(entries_sorted, gpr):
            tds: List[html.Td] = []
            for _, _own, _md, dn, d_map in row_groups:
                if is_data:
                    stage_stat = {stg: best_status((d_map.get(stg) or {"counts":{}})["counts"], "data") for stg in DATA_STAGES}
                    title = dn
                    cells = [html.Td(title, style={"fontWeight":"600","whiteSpace":"nowrap"})]
                    for stg in DATA_STAGES:
                        leaf = d_map.get(stg, {"counts":{}, "chunks":[]})
                        cells.append(html.Td(self._chunk_block(tab, leaf.get("chunks", []), chunks_per_line, prefix=prefix),
                                             style={"verticalAlign":"top","padding":"6px 10px","whiteSpace":"nowrap",
                                                    **self._shade(tab, stage_stat.get(stg), 0.18)}))
                    tds.extend(cells)
                else:
                    # single status bucket
                    leaf = d_map.get("status", {"counts":{}, "chunks":[]})
                    bs = best_status(leaf.get("counts", {}), tab)
                    title = dn
                    cells = [
                        html.Td(title, style={"fontWeight":"600","whiteSpace":"nowrap"}),
                        html.Td(self._chunk_block(tab, leaf.get("chunks", []), chunks_per_line, prefix=prefix),
                                style={"verticalAlign":"top","padding":"6px 10px","whiteSpace":"nowrap",
                                       **self._shade(tab, bs, 0.18)}),
                    ]
                    tds.extend(cells)
            # pad empties
            if len(row_groups) < gpr:
                if is_data:
                    for _ in range(gpr - len(row_groups)):
                        tds.extend([html.Td(""), html.Td(""), html.Td(""), html.Td(""), html.Td("")])
                else:
                    for _ in range(gpr - len(row_groups)):
                        tds.extend([html.Td(""), html.Td("")])
            body_rows.append(html.Tr(tds))

        if not body_rows:
            body_rows = [html.Tr(html.Td("No data", colSpan=(5*gpr if is_data else 2*gpr), className="text-muted"))]

        return dbc.Table(
            [head, html.Tbody(body_rows)],
            bordered=True, hover=False, size="sm", className="mb-1",
            style={
                "tableLayout": "auto",
                "width": "auto",
                "display": "inline-table",
                "marginRight":"10ch"
            },
        )
    def _prefix_for_tab(self, tab: str) -> str:
        """
        Single-letter prefix driven by the tab name.
        Data must use 'c' (c0, c1, ...).
        """
        m = {"data": "c", "features": "f", "alphas": "a", "strategies": "s"}
        return m.get((tab or "").lower(), "c")