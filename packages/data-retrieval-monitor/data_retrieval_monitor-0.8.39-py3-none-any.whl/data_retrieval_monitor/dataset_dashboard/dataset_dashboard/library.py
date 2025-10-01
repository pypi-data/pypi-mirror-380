import random
from pathlib import Path
from typing import List, Tuple, Dict
from .constants import DATA_STAGES, status_order_for_tab
from .config import AppConfig
from .utils import utc_now_iso

def _mk_chunks(statuses, base_dir: Path, dn: str, bucket: str, k: int):
    chunks = []
    for j in range(k):
        s = random.choice(statuses)
        log_path = (base_dir / dn / f"{bucket}-{j}.log")
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(f"{dn} {bucket} chunk {j} status={s}\n", encoding="utf-8")
        chunks.append({"id": f"{bucket[:1].upper()}{j}", "status": s,
                       "proc": f"https://example.com/proc/{dn}/{bucket}/{j}",
                       "log": str(log_path)})
    return chunks

def make_payload_for_owner(cfg: AppConfig, owner: str, tab: str, num_items: int = 12) -> Tuple[List[dict], Dict]:
    random.seed()
    log_root = Path(cfg.log_root)
    items: List[dict] = []
    statuses = status_order_for_tab(tab)
    owner_norm = (owner or cfg.default_owner).strip().lower()

    for i in range(num_items):
        dn = f"{tab}-{owner_norm}-{i:03d}"
        if tab == "data":
            mode = "backfill" if (i % 3 == 0) else "live"
            for stg in DATA_STAGES:
                k = random.randint(2, 5)
                chs = _mk_chunks(statuses, log_root, dn, stg, k)
                items.append({
                    "owner": owner_norm, "mode": mode, "data_name": dn,
                    "stage": stg, "chunks": chs, "errors": [],
                })
        else:
            k = random.randint(2, 6)
            chs = _mk_chunks(statuses, log_root, dn, "status", k)
            items.append({
                "owner": owner_norm, "mode": "live", "data_name": dn,
                "stage": "status", "chunks": chs, "errors": [],
            })
    meta = {"env": cfg.environment_label, "last_ingest_at": utc_now_iso(), "owner_labels": {}}
    return items, meta

def seed_all_tabs(host, num_per_tab: int = 12):
    cfg = host.cfg
    owners = ["kimdg","kimyd","leejm"]
    for t in ["data","features","alphas","strategies"]:
        all_items: List[dict] = []
        meta = {}
        for o in owners:
            items, meta = make_payload_for_owner(cfg, o, t, num_per_tab)
            all_items.extend(items)
        host.store.apply_snapshot_with_meta_tab(t, all_items, meta)
