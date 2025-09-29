import threading
from typing import Callable, Optional, Tuple, Any, List, Dict

class InjectorService:
    """
    Periodically calls `make()` and applies via `apply(tab, items, meta=None)`.
    """
    def __init__(self,
                 apply_tab: Callable[[str, List[dict], Optional[Dict]], None],
                 make: Callable[[], Any],
                 tab: str,
                 period_sec: int = 300,
                 enabled: bool = False):
        self._apply = apply_tab
        self._make = make
        self._tab = (tab or "data").lower()
        self._period = self._clamp(period_sec)
        self._enabled = bool(enabled)
        self._stop = threading.Event()
        self._lock = threading.RLock()
        self._thr: Optional[threading.Thread] = None

    def start(self):
        with self._lock:
            if not self._enabled: return
            if self._thr and self._thr.is_alive(): return
            self._stop.clear()
            self._thr = threading.Thread(target=self._run, name=f"InjectorService[{self._tab}]", daemon=True)
            self._thr.start()

    def stop(self): self._stop.set()
    def set_period(self, seconds: int): 
        with self._lock: self._period = self._clamp(seconds)
    def enable(self, enabled: bool):
        with self._lock:
            self._enabled = bool(enabled)
            if self._enabled: self.start()
            else: self.stop()

    @property
    def period(self) -> int: return self._period
    @property
    def enabled(self) -> bool: return self._enabled

    def _run(self):
        while not self._stop.is_set():
            try:
                result = self._make()
                items, meta = self._resolve_payload(result)
                if items:
                    self._apply(self._tab, items, meta)
            except Exception:
                pass
            finally:
                self._stop.wait(self._period)

    @staticmethod
    def _resolve_payload(result: Any) -> Tuple[List[dict], Optional[Dict]]:
        if isinstance(result, tuple) and len(result) == 2:
            items, meta = result
            return list(items or []), dict(meta or {})
        if isinstance(result, dict):
            items = result.get("items") or result.get("snapshot") or []
            meta = result.get("meta") or {}
            return list(items), dict(meta)
        return list(result or []), None

    @staticmethod
    def _clamp(n: int) -> int:
        try: n = int(n)
        except Exception: n = 300
        if n < 5: n = 5
        if n > 300: n = 300
        return n