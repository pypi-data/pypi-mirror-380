import os, json, tempfile, threading, pathlib
from typing import Dict, List, Optional
from ..constants import TAB_IDS, DATA_STAGES, status_order_for_tab
from ..utils import utc_now_iso

class StoreService:
    """
    Multi-tab store:
    {
      "tabs": {
        "data": {...single_store_shape...},
        "features": {...},
        ...
      }
    }
    Each tab store: {"jobs":{owner->{mode->{dataset->{stage|status:{chunks,counts}}}}}, "meta":{}, "updated_at":...}
    """
    def __init__(self, backend: str, store_path: str, default_owner: str, default_mode: str):
        self.backend = backend
        self.store_path = store_path
        self.default_owner = default_owner
        self.default_mode = default_mode
        self._lock = threading.RLock()
        self._mem: Optional[dict] = None
        self._cache: Optional[dict] = None
        self._mtime: Optional[float] = None
        self._ensure_file()

    def _init_tab(self, tab: str) -> dict:
        return {
            "jobs": {},
            "meta": {"owner_labels": {}, "env": "demo", "last_ingest_at": None},
            "updated_at": utc_now_iso()
        }

    def _init(self) -> dict:
        return {"tabs": {t: self._init_tab(t) for t in TAB_IDS}}

    def _ensure_file(self):
        if self.backend == "memory":
            if self._mem is None: self._mem = self._init()
            return
        p = pathlib.Path(self.store_path)
        if not p.exists():
            p.write_text(json.dumps(self._init(), indent=2))

    def _load(self) -> dict:
        self._ensure_file()
        if self.backend == "memory":
            return self._mem
        mtime = os.path.getmtime(self.store_path)
        if self._cache is not None and self._mtime == mtime:
            return self._cache
        with open(self.store_path, "rb") as f:
            data = json.loads(f.read().decode("utf-8"))
        self._cache, self._mtime = data, mtime
        return data

    def _save(self, store: dict):
        if self.backend == "memory":
            with self._lock: self._mem = store
            return
        dir_ = os.path.dirname(os.path.abspath(self.store_path)) or "."
        fd, tmp = tempfile.mkstemp(prefix="store.", suffix=".tmp", dir=dir_)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as w:
                json.dump(store, w, indent=2)
            os.replace(tmp, self.store_path)
            self._cache = store
            self._mtime = os.path.getmtime(self.store_path)
        finally:
            try:
                if os.path.exists(tmp): os.remove(tmp)
            except Exception:
                pass

    # ---------- helpers per tab ----------
    def _ensure_leaf(self, tab_store, owner: str, mode: str, data_name: str, bucket: str) -> dict:
        jobs = tab_store.setdefault("jobs", {})
        o = jobs.setdefault(owner, {})
        m = o.setdefault(mode, {})
        d = m.setdefault(data_name, {})
        # bucket: Data uses one of DATA_STAGES; others use "status"
        return d.setdefault(bucket, {"chunks": [], "counts": {s:0 for s in status_order_for_tab("data")}, "errors": []})

    def _recount(self, tab: str, leaf: dict):
        order = status_order_for_tab(tab)
        counts = {s:0 for s in order}
        for ch in leaf.get("chunks", []):
            st = (ch.get("status") or "other")
            if st not in counts: st = "other"
            counts[st] += 1
        leaf["counts"] = counts

    # ---------- public ----------
    def state(self) -> dict:
        return self._load()

    def apply_snapshot_with_meta_tab(self, tab: str, items: List[dict], meta: Optional[dict] = None):
        tab = (tab or "data").lower()
        store = self._load()
        tabs = store.setdefault("tabs", {})
        tab_store = tabs.setdefault(tab, self._init_tab(tab))

        # meta
        meta = meta or {}
        store_meta = tab_store.setdefault("meta", {})
        if "env" in meta:
            store_meta["env"] = meta.get("env") or store_meta.get("env") or "demo"
        store_meta["last_ingest_at"] = meta.get("last_ingest_at") or meta.get("ingested_at") or utc_now_iso()

        # reset jobs for tab then fill
        tab_store["jobs"] = {}
        order_data = status_order_for_tab("data")
        order_tab  = status_order_for_tab(tab)

        for it in items or []:
            owner = (it.get("owner") or self.default_owner).strip().lower()
            mode  = (it.get("mode")  or self.default_mode).strip().lower()
            dn    = it.get("data_name") or "unknown"
            if tab == "data":
                bucket = (it.get("stage") or "stage").lower()
                if bucket not in DATA_STAGES: bucket = "stage"
                leaf = self._ensure_leaf(tab_store, owner, mode, dn, bucket)
                # counts must follow DATA status order
                leaf["chunks"] = list(it.get("chunks", []))
                leaf["errors"] = list(it.get("errors", []))[-50:] if isinstance(it.get("errors"), list) else []
                # convert unknown to "other"
                for ch in leaf["chunks"]:
                    s = ch.get("status") or "other"
                    if s not in order_data: ch["status"] = "other"
                self._recount("data", leaf)
            else:
                bucket = "status"
                leaf = self._ensure_leaf(tab_store, owner, mode, dn, bucket)
                leaf["chunks"] = list(it.get("chunks", []))
                leaf["errors"] = list(it.get("errors", []))[-50:] if isinstance(it.get("errors"), list) else []
                for ch in leaf["chunks"]:
                    s = ch.get("status") or "other"
                    if s not in order_tab: ch["status"] = "other"
                # recount using tab vocab
                order = status_order_for_tab(tab)
                counts = {s:0 for s in order}
                for ch in leaf["chunks"]:
                    counts[ch["status"]] += 1
                leaf["counts"] = counts

        tab_store["updated_at"] = utc_now_iso()
        self._save(store)

    # compatibility (legacy single-tab ingestion → route to data)
    def apply_snapshot_with_meta(self, items: List[dict], meta: Optional[dict] = None):
        self.apply_snapshot_with_meta_tab("data", items, meta or {})

    # options for dropdowns
    def list_filters_for_tab(self, tab: str):
        st = self._load()
        tree = st.get("tabs", {}).get(tab, {}) or {}
        jobs = tree.get("jobs", {})
        owners = sorted(jobs.keys())
        owner_opts = [{"label": "All", "value": "All"}] + [{"label": o.upper(), "value": o} for o in owners]
        modes = set()
        for o_map in jobs.values(): modes.update(o_map.keys())
        mode_opts = [{"label": "All", "value": "All"}] + [{"label": m.title(), "value": m} for m in sorted(modes)]
        return owner_opts, mode_opts