import random
from pathlib import Path
from typing import List, Tuple, Dict
from .constants import DATA_STAGES, TAB_IDS, status_order_for_tab
from .config import AppConfig
from .utils import utc_now_iso

def _mk_chunks(statuses: List[str], base_dir: Path, dn: str, bucket: str, k: int):
    chunks = []
    for j in range(k):
        s = random.choice(statuses)
        log_path = (base_dir / dn / f"{bucket}-{j}.log")
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(f"{dn} {bucket} chunk {j} status={s}\n", encoding="utf-8")
        chunks.append({
            "id": f"{bucket[:1].upper()}{j}",
            "status": s,
            "proc": f"https://example.com/proc/{dn}/{bucket}/{j}",
            "log": str(log_path),  # absolute path
        })
    return chunks

def make_dummy_payload(cfg: AppConfig, tab: str, num_items: int = 12) -> Tuple[List[dict], Dict]:
    """
    Return (items, meta) for a specific tab.
    Data tab fills 4 stages per dataset; other tabs fill a single 'status' bucket.
    """
    random.seed()
    log_root = Path(cfg.log_root)
    items: List[dict] = []
    statuses = status_order_for_tab(tab)

    for i in range(num_items):
        dn = f"{tab}-{i:03d}"
        mode = "live"
        if tab == "data" and (i % 3 == 0): mode = "backfill"
        if tab == "data":
            for stg in DATA_STAGES:
                k = random.randint(2, 5)
                chs = _mk_chunks(statuses, log_root, dn, stg, k)
                items.append({
                    "owner": cfg.default_owner.lower(),
                    "mode": mode.lower(),
                    "data_name": dn,
                    "stage": stg,
                    "chunks": chs,
                    "errors": [],
                })
        else:
            # single bucket "status"
            k = random.randint(2, 6)
            chs = _mk_chunks(statuses, log_root, dn, "status", k)
            items.append({
                "owner": cfg.default_owner.lower(),
                "mode": "live",
                "data_name": dn,
                "stage": "status",         # ignored by store for non-data; kept for clarity
                "chunks": chs,
                "errors": [],
            })
    meta = {"env": cfg.environment_label, "ingested_at": utc_now_iso()}
    return items, meta

def seed_all_tabs(host, num_per_tab: int = 12):
    cfg = host.cfg
    for t in TAB_IDS:
        items, meta = make_dummy_payload(cfg, t, num_per_tab)
        host.store.apply_snapshot_with_meta_tab(t, items, meta)