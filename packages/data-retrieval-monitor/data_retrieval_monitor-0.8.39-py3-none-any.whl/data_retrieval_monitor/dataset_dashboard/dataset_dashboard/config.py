from dataclasses import dataclass

@dataclass
class AppConfig:
    app_title: str = "Dataset Dashboard"
    environment_label: str = "demo"
    default_owner: str = "kimdg"
    log_root: str = "/tmp/drm-logs"
    store_backend: str = "memory"
    store_path: str = ""
    clipboard_fallback_open: bool = False
    max_left_width = 720
    max_graph_width = 680
    max_kpi_width = 220
    refresh_ms: int = 1500
    timezone: str = "UTC"

def load_config() -> "AppConfig":
    return AppConfig()
