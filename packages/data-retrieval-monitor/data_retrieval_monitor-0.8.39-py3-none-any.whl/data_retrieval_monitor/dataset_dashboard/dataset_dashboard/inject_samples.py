#!/usr/bin/env python3
"""
inject_samples.py — external injector for dataset_dashboard

- Generates realistic payloads for tabs: data, features, alphas, strategies
- Writes dummy log files under /tmp/drm-logs (or --log-root)
- Always saves the generated payload to JSON (default: ./sample_payload.json)
- Posts to http://HOST:PORT/ingest_snapshot unless --print-only is set
- Can run once or continuously (--period seconds)
"""

from __future__ import annotations
import argparse
import json
import os
import random
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

import requests


# ---------------------------
# Tab definitions (mirror your constants.py)
# ---------------------------

TAB_IDS = ["data", "features", "alphas", "strategies"]

DATA_STAGES = ["archive", "stage", "enrich", "consolidate"]

DATA_STATUS_ORDER = [
    "failed", "overdue", "manual", "retrying", "running",
    "waiting", "succeeded", "queued", "allocated", "other"
]
FEATURES_STATUS_ORDER = ["F-Stat-001", "F-Stat-002", "F-Stat-003", "other"]
ALPHAS_STATUS_ORDER    = ["A-Stat-001", "A-Stat-002", "A-Stat-003", "other"]
STRATS_STATUS_ORDER    = ["S-Stat-001", "S-Stat-002", "S-Stat-003", "other"]

def status_order_for_tab(tab: str) -> List[str]:
    t = (tab or "data").lower()
    if t == "features": return FEATURES_STATUS_ORDER
    if t == "alphas":   return ALPHAS_STATUS_ORDER
    if t == "strategies": return STRATS_STATUS_ORDER
    return DATA_STATUS_ORDER


# ---------------------------
# Helpers
# ---------------------------

def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def pick(seq: List[str]) -> str:
    return random.choice(seq)

def ensure_log_file(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(text, encoding="utf-8")

def make_chunk(idx: int, status: str, proc_url: str, log_path: Path, prefix: str = "c") -> Dict:
    return {
        "id": f"{prefix}{idx}",   # <- c0/f0/a0/s0
        "status": status,
        "proc": proc_url,
        "log": str(log_path),
    }

def save_payload(path: Path, payload: Dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"Saved payload -> {path}")


# ---------------------------
# Payload makers per tab
# ---------------------------

def make_items_for_data(
    owners: List[str],
    num_datasets: int,
    chunks_per_stage: Tuple[int, int],
    log_root: Path,
) -> List[Dict]:
    """
    Classic 'data' tab: datasets × 4 pipeline stages, chunks per stage,
    statuses from DATA_STATUS_ORDER.
    """
    items: List[Dict] = []
    for i in range(num_datasets):
        owner = owners[i % len(owners)].lower()
        data_name = f"dataset-{i:03d}"
        mode = "live" if (i % 3) else "backfill"

        for stage in DATA_STAGES:
            k = random.randint(chunks_per_stage[0], chunks_per_stage[1])
            chunks: List[Dict] = []
            for j in range(k):
                st = pick(DATA_STATUS_ORDER)
                proc = f"https://example.com/proc/{data_name}/{stage}/{j}"
                logp = log_root / data_name / f"{stage}-{j}.log"
                ensure_log_file(logp, f"{data_name} {stage} chunk {j}\n")
                chunks.append(make_chunk(j, st, proc, logp, prefix="c"))
            items.append({
                "owner": owner,
                "mode": mode,
                "data_name": data_name,
                "stage": stage,
                "chunks": chunks,
                "errors": [],
            })
    return items


def make_items_flat_single_status_column(
    tab: str,
    owners: List[str],
    label_prefix: str,       # e.g. "feature", "alpha", "strategy"
    num_rows: int,
    chunks_per_row: Tuple[int, int],
    log_root: Path,
) -> List[Dict]:
    """
    For features/alphas/strategies: single column 'status' (no pipeline stages).
    Each 'row' has N chunks with tab-specific statuses.
    """
    items: List[Dict] = []
    stat_order = status_order_for_tab(tab)
    for i in range(num_rows):
        owner = owners[i % len(owners)].lower()
        mode = "live"
        data_name = f"{label_prefix}-{i:03d}"
        stage = "status"
        k = random.randint(chunks_per_row[0], chunks_per_row[1])
        chunks: List[Dict] = []
        for j in range(k):
            st = pick(stat_order)
            proc = f"https://example.com/{tab}/{data_name}/{j}"
            logp = log_root / tab / data_name / f"{stage}-{j}.log"
            ensure_log_file(logp, f"{tab} {data_name} chunk {j} status={st}\n")
            prefix = {"features": "f", "alphas": "a", "strategies": "s"}.get(tab, "c")
            chunks.append(make_chunk(j, st, proc, logp, prefix=prefix))
        items.append({
            "owner": owner,
            "mode": mode,
            "data_name": data_name,
            "stage": stage,
            "chunks": chunks,
            "errors": [],
        })
    return items


def make_snapshot_for_tab(
    tab: str,
    owners: List[str],
    num_rows: int,
    chunk_range: Tuple[int, int],
    log_root: Path,
) -> Tuple[List[Dict], Dict]:
    t = tab.lower()
    if t == "data":
        items = make_items_for_data(
            owners=owners,
            num_datasets=num_rows,
            chunks_per_stage=chunk_range,
            log_root=log_root,
        )
    elif t == "features":
        items = make_items_flat_single_status_column(
            tab="features", owners=owners, label_prefix="feature",
            num_rows=num_rows, chunks_per_row=chunk_range, log_root=log_root
        )
    elif t == "alphas":
        items = make_items_flat_single_status_column(
            tab="alphas", owners=owners, label_prefix="alpha",
            num_rows=num_rows, chunks_per_row=chunk_range, log_root=log_root
        )
    else:  # strategies
        items = make_items_flat_single_status_column(
            tab="strategies", owners=owners, label_prefix="strategy",
            num_rows=num_rows, chunks_per_row=chunk_range, log_root=log_root
        )
    meta = {"env": "demo", "ingested_at": iso_now(), "tab": t}
    return items, meta


# ---------------------------
# POST/print driver
# ---------------------------

def post_snapshot(base_url: str, items: List[Dict], meta: Dict, print_only: bool):
    url = f"{base_url.rstrip('/')}/ingest_snapshot"
    payload = {"snapshot": items, "meta": meta}
    if print_only:
        print("\n--- PRINT-ONLY (not posting) ---")
        print(json.dumps(payload, indent=2))
        return
    try:
        r = requests.post(url, json=payload, timeout=15)
        print(f"POST {url} -> {r.status_code}")
        print(r.text)
    except Exception as e:
        print(f"POST error: {e}")


# ---------------------------
# CLI
# ---------------------------

def parse_args():
    ap = argparse.ArgumentParser(description="External injector for dataset_dashboard")
    ap.add_argument("--host", default=os.getenv("DASH_HOST", "127.0.0.1"))
    ap.add_argument("--port", type=int, default=int(os.getenv("DASH_PORT", "8090")))
    ap.add_argument("--tab", choices=TAB_IDS, default="data", help="Which tab to target")
    ap.add_argument("--owners", default="qsg", help="Comma-separated owners (e.g. qsg,teamx,teamy)")
    ap.add_argument("--rows", type=int, default=6, help="Number of dataset/feature/alpha/strategy rows")
    ap.add_argument("--chunk-min", type=int, default=2, help="Min chunks per leaf")
    ap.add_argument("--chunk-max", type=int, default=5, help="Max chunks per leaf")
    ap.add_argument("--log-root", default="/tmp/drm-logs", help="Directory to write logs")
    ap.add_argument("--print-only", action="store_true", help="Do not POST; just print the payload")
    ap.add_argument("--period", type=int, default=0, help="If >0, re-inject every N seconds until Ctrl-C")
    ap.add_argument("--out", default="sample_payload.json", help="Path to save generated payload JSON")
    return ap.parse_args()

def main():
    args = parse_args()
    base_url = f"http://{args.host}:{args.port}"
    owners = [o.strip() for o in args.owners.split(",") if o.strip()]
    log_root = Path(args.log_root).resolve()
    out_path = Path(args.out).resolve()
    log_root.mkdir(parents=True, exist_ok=True)

    random.seed()

    def one_inject():
        items, meta = make_snapshot_for_tab(
            tab=args.tab,
            owners=owners,
            num_rows=args.rows,
            chunk_range=(args.chunk_min, args.chunk_max),
            log_root=log_root,
        )
        payload = {"snapshot": items, "meta": meta}

        # 1) Save to JSON first
        save_payload(out_path, payload)

        # 2) Print or POST (according to --print-only)
        post_snapshot(base_url, items, meta, args.print_only)

    if args.period and args.period > 0:
        print(f"Looping every {args.period}s. Ctrl-C to stop.")
        try:
            while True:
                one_inject()
                time.sleep(args.period)
        except KeyboardInterrupt:
            print("\nStopped.")
    else:
        one_inject()


if __name__ == "__main__":
    main()