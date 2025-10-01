import os
import pathlib
from dataclasses import dataclass

@dataclass(frozen=True)
class AppConfig:
    app_title: str
    timezone: str
    refresh_ms: int
    store_backend: str
    store_path: str
    default_owner: str
    default_mode: str
    log_root: pathlib.Path
    max_left_width: int
    max_graph_width: int
    max_kpi_width: int
    # injector
    ingest_enabled: bool
    ingest_period_sec: int
    # clipboard behavior
    clipboard_fallback_open: bool
    # environment label
    environment_label: str

def load_config() -> AppConfig:
    period = int(os.getenv("INGEST_PERIOD_SEC", "300"))
    period = 5 if period < 5 else (300 if period > 300 else period)
    return AppConfig(
        app_title=os.getenv("APP_TITLE", "Dashboard"),
        timezone=os.getenv("APP_TIMEZONE", "Europe/London"),
        refresh_ms=int(os.getenv("REFRESH_MS", "1000")),
        store_backend=os.getenv("STORE_BACKEND", "memory"),
        store_path=os.getenv("STORE_PATH", "status_store.json"),
        default_owner=os.getenv("DEFAULT_OWNER", "qsg"),
        default_mode=os.getenv("DEFAULT_MODE", "live"),
        log_root=pathlib.Path(os.getenv("LOG_ROOT", "/tmp/drm-logs")).resolve(),
        max_left_width=int(os.getenv("MAX_LEFT_WIDTH", "520")),
        max_graph_width=int(os.getenv("MAX_GRAPH_WIDTH", "420")),
        max_kpi_width=int(os.getenv("MAX_KPI_WIDTH", "300")),
        ingest_enabled=os.getenv("INGEST_ENABLED", "1") == "1",
        ingest_period_sec=period,
        clipboard_fallback_open=os.getenv("CLIPBOARD_FALLBACK_OPEN", "0") == "1",
        environment_label=os.getenv("APP_ENV", os.getenv("ENVIRONMENT", "demo")),
    )