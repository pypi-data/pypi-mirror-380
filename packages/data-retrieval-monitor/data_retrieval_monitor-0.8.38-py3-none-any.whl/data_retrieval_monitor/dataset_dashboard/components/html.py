from dash import html, dcc
from ..utils import px

class PageLayout:
    """Assembles the left controls/KPIs/pies and right table container + interval, incl. Tab bar."""
    def __init__(self, cfg, controls_component, kpi_strip, pie_component):
        self.cfg = cfg
        self.controls = controls_component
        self.kpis = kpi_strip
        self.pies = pie_component

    def build(self):
        controls = self.controls.render(self.cfg)

        def pie_holder(_id, title, max_graph_width: int):
            return dcc.Graph(id=_id, figure={"layout":{"title":{"text": title}}},
                             style={"height":"320px", "maxWidth": px(max_graph_width), "margin":"0"})

        pies_block = html.Div(
            [
                pie_holder("pie-stage","Stage", self.cfg.max_graph_width),
                pie_holder("pie-archive","Archive", self.cfg.max_graph_width),
                pie_holder("pie-enrich","Enrich", self.cfg.max_graph_width),
                pie_holder("pie-consolidate","Consolidate", self.cfg.max_graph_width),
                pie_holder("pie-overview","Overview", self.cfg.max_graph_width),
            ],
            className="mb-2",
            style={"display":"flex","gap":"12px","flexWrap":"wrap","paddingBottom":"8px"}
        )

        spacer_after_kpis = html.Div(style={"height": "12px"})

        left = html.Div([controls, pies_block],
                        style={"width": px(self.cfg.max_left_width), "minWidth": px(self.cfg.max_left_width),
                               "maxWidth": px(self.cfg.max_left_width), "flex":"0 0 auto"})

        right = html.Div([
            html.Div([
                html.H4(id="table-title", className="fw-semibold", style={"margin":"0","whiteSpace":"nowrap"}),
                html.Div(id="table-container", style={"flex":"1 1 auto","minWidth":"0"})
            ], style={"display":"flex","alignItems":"flex-start","gap":"8px","width":"100%"}),
        ], style={"flex":"1 1 auto","minWidth":"0"})

        page = html.Div(
            [left, right],
            style={
                "display": "flex",
                "flexWrap": "nowrap",
                "alignItems": "flex-start",
                "gap": "16px",
                "width": "100%",
                "margin": "0 auto",
                "paddingLeft": "10ch",
                "paddingRight": "10ch",
                 "marginTop": "24px"
            },
        )
        return page