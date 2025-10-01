from dash import html, dcc
from .config import AppConfig
from .services.store import StoreService
from .services.logs import LogLinker, register_log_routes
from .components import BannerComponent, ControlsComponent, KpiStrip, PieChartComponent, TableComponent
from .components.html import PageLayout
from .constants import TAB_IDS

class DashboardHost:
    def __init__(self, app, cfg: AppConfig):
        self.app = app
        self.cfg = cfg

        # services
        self.store = StoreService(cfg.store_backend, cfg.store_path, cfg.default_owner, cfg.default_mode)
        self.log_linker = LogLinker(cfg.log_root)

        # components
        self.banner = BannerComponent()
        self.controls = ControlsComponent()
        self.kpis = KpiStrip(cfg.max_kpi_width)
        self.pies = PieChartComponent()
        self.table = TableComponent(self.log_linker, clipboard_fallback_open=cfg.clipboard_fallback_open)

        register_log_routes(app.server, self.log_linker)

        tabs = dcc.Tabs(
            id="main-tabs",
            value="data",
            children=[
                dcc.Tab(label="Data", value="data"),
                dcc.Tab(label="Features", value="features"),
                dcc.Tab(label="Alphas", value="alphas"),
                dcc.Tab(label="Strategies", value="strategies"),
            ],
            className="mb-2",
        )

        page_layout = PageLayout(cfg, self.controls, self.kpis, self.pies)

        self.layout = html.Div([
            self.banner.render(cfg.app_title),
            tabs,
            page_layout.build(),
        ])

    # no periodic injectors here (you can add later); ingestion is via REST routes