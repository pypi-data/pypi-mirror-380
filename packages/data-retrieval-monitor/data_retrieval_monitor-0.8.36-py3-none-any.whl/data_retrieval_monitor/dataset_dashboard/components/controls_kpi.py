from dash import html, dcc
import dash_bootstrap_components as dbc
from ..utils import px
from ..constants import DATA_STAGES, status_order_for_tab

class ControlsComponent:
    def render(self, cfg):
        # Owner + Status always visible; Mode/Stage wrapped in #advanced-controls (hidden on non-data tabs)
        return dbc.Card(
            dbc.CardBody([
                html.Div("Owner", className="text-muted small"),
                dcc.Dropdown(id="owner-filter", options=[], value="All", clearable=False, className="mb-2", style={"minWidth":"180px"}),

                html.Div(id="advanced-controls", children=[
                    html.Div("Mode", className="text-muted small"),
                    dcc.Dropdown(id="mode-filter", options=[], value="All", clearable=False, className="mb-2", style={"minWidth":"180px"}),

                    html.Div("Stage filter (ANY of)", className="text-muted small"),
                    dcc.Dropdown(id="stage-filter",
                                 options=[{"label": s.title(), "value": s} for s in DATA_STAGES],
                                 value=DATA_STAGES, multi=True, className="mb-2"),
                ]),

                html.Div("Status filter (ANY of)", className="text-muted small"),
                dcc.Dropdown(id="status-filter",
                             options=[],  # filled dynamically by tab
                             value=[], multi=True, placeholder="(none)"),

                html.Div("Table groups per row", className="text-muted small mt-2"),
                dcc.Dropdown(id="table-groups", options=[{"label": str(n), "value": n} for n in (1,2,3,4,5,6)],
                             value=2, clearable=False, style={"width":"120px"}),

                html.Div("Chunks per line", className="text-muted small mt-2"),
                dcc.Dropdown(id="chunks-per-line", options=[{"label": str(n), "value": n} for n in (1,2,3,4,5,6,8,10,16)],
                             value=6, clearable=False, style={"width":"120px"}),

                html.Div("Sort by", className="text-muted small mt-2"),
                dcc.Dropdown(
                    id="sort-by",
                    options=[
                        {"label": "Data Name (A–Z)", "value": "name_asc"},
                        {"label": "Chunk Avg Score (worst→best)", "value": "chunk_asc"},
                        {"label": "Chunk Avg Score (best→worst)", "value": "chunk_desc"},
                        {"label": "Status Avg Score (worst→best)", "value": "status_asc"},
                        {"label": "Status Avg Score (best→worst)", "value": "status_desc"},
                    ],
                    value="name_asc",
                    clearable=False,
                    style={"minWidth":"220px"},
                ),

                # KPI zone (below sort as requested)
                html.Div(id="kpi-container", className="mt-3"),
            ]),
            style={"margin":"0"}
        )

class KpiStrip:
    def __init__(self, max_kpi_width: int):
        self.max_kpi_width = max_kpi_width

    def render(self, tab: str, order: list, counts: dict, per_row: int = 3):
        # grid with per_row columns; each card same width
        cards = []
        for s in order:
            val = int(counts.get(s, 0) or 0)
            cards.append(
                dbc.Card(
                    dbc.CardBody([html.Div(s, className="text-muted small"),
                                  html.H4(str(val), className="mb-0")]),
                    style={"margin":"0"}
                )
            )
        # grid layout
        return html.Div(
            cards,
            style={
                "display":"grid",
                "gridTemplateColumns": f"repeat({max(1, per_row)}, minmax(0, {px(self.max_kpi_width)}))",
                "gap":"10px",
            }
        )