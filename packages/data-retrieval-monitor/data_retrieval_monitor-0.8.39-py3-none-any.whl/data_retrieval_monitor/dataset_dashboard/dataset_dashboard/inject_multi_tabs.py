#!/usr/bin/env python3
# multi_payload_injector.py
from __future__ import annotations

import os, json, random
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Tuple, Optional, Any
import requests
from enum import Enum

# ---------------------------
# Config from environment
# ---------------------------
DASH_URL = os.getenv("DASH_URL", "http://127.0.0.1:8090/ingest_snapshot")
LOG_ROOT = Path(os.getenv("LOG_ROOT", "/tmp/drm-logs")).resolve()
APP_ENV  = os.getenv("APP_ENV", "demo")
NUM_PER_TAB_DEFAULT = int(os.getenv("NUM_PER_TAB", "9"))
_SEED = os.getenv("SEED")
random.seed(_SEED)

_OWNER_NAMES = [x.strip() for x in os.getenv("OWNERS","KIMDG,KIMYD,LEEJM").split(",") if x.strip()]

def _build_owner_enum(names: List[str]) -> Enum:
    cleaned = []
    for n in names:
        sym = n.upper().replace("-","_").replace(" ","_")
        if not sym.isidentifier():
            raise ValueError(f"Owner name '{n}' not valid")
        cleaned.append((sym, n))
    return Enum("Owner", {sym: val for sym, val in cleaned})

Owner = _build_owner_enum(_OWNER_NAMES)

def get_owner(owner: str | Owner) -> Owner:
    if isinstance(owner, Owner): return owner
    key = str(owner).upper().replace("-","_").replace(" ","_")
    try: return getattr(Owner, key)
    except AttributeError:
        raise ValueError(f"Unknown owner '{owner}'. Valid: {', '.join(m.name for m in Owner)}")

# ---------------------------
# Tabs + statuses (unchanged)
# ---------------------------
TAB_IDS = ["data", "features", "alphas", "strategies"]
DATA_STAGES = ["archive","stage","enrich","consolidate"]

DATA_STATUS_ORDER     = ["failed","overdue","manual","retrying","running","waiting","succeeded","queued","allocated","other"]
FEATURES_STATUS_ORDER = ["F-Stat-001","F-Stat-002","F-Stat-003","other"]
ALPHAS_STATUS_ORDER   = ["A-Stat-001","A-Stat-002","A-Stat-003","other"]
STRATS_STATUS_ORDER   = ["S-Stat-001","S-Stat-002","S-Stat-003","other"]

def status_order_for_tab(tab: str) -> List[str]:
    t = (tab or "data").lower()
    if t == "features":   return FEATURES_STATUS_ORDER
    if t == "alphas":     return ALPHAS_STATUS_ORDER
    if t == "strategies": return STRATS_STATUS_ORDER
    return DATA_STATUS_ORDER

# ---------------------------
# Helpers
# ---------------------------
def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def _mk_log(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def _pick(seq: List[str]) -> str:
    return random.choice(seq)

def _chunk(status: str, abs_log: Path, proc_url: str, idx: int) -> Dict[str, Any]:
    return {"id": f"c{idx}", "status": status, "proc": proc_url, "log": str(abs_log)}

def _meta() -> Dict[str, Any]:
    return {"env": APP_ENV, "ingested_at": iso_now()}

def _ensure_dir(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True); return p

def _save_json(obj: Any, path: Path) -> Path:
    _ensure_dir(path.parent)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")
    return path

# ---------------------------
# Payload builders
# ---------------------------
def make_data_payload_for_owner(owner: Owner, num_entities: int = 3, start_index: int = 0, log_root: Path = LOG_ROOT) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    owner_val = get_owner(owner).value
    for i in range(num_entities):
        dn = f"dataset-{start_index + i:03d}"
        mode = "live" if (i % 3) else "backfill"
        for stg in DATA_STAGES:
            k = random.randint(2,5)
            chunks = []
            for j in range(k):
                status = _pick(DATA_STATUS_ORDER)
                abs_log = (log_root / "data" / owner_val / dn / f"{stg}-{j}.log")
                _mk_log(abs_log, f"[{iso_now()}] owner={owner_val} {dn} {stg} c{j} {status}\n")
                proc = f"https://example.com/proc/{dn}/{stg}/{j}"
                chunks.append(_chunk(status, abs_log, proc, j))
            items.append({"owner": owner_val, "mode":"live", "data_name": dn, "stage": stg, "chunks": chunks, "errors": []})
    return items

def make_features_payload_for_owner(owner: Owner, num_entities: int = 3, start_index: int = 0, log_root: Path = LOG_ROOT) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []; owner_val = get_owner(owner).value
    for i in range(num_entities):
        name = f"feature-{start_index + i:03d}"
        k = random.randint(2,5); chunks=[]
        for j in range(k):
            status = _pick(FEATURES_STATUS_ORDER)
            abs_log = (log_root / "features" / owner_val / name / f"status-{j}.log")
            _mk_log(abs_log, f"[{iso_now()}] owner={owner_val} {name} c{j} {status}\n")
            proc = f"https://example.com/features/proc/{name}/{j}"
            chunks.append(_chunk(status, abs_log, proc, j))
        items.append({"owner": owner_val, "mode":"live", "data_name": name, "stage": "status", "chunks": chunks, "errors": []})
    return items

def make_alphas_payload_for_owner(owner: Owner, num_entities: int = 3, start_index: int = 0, log_root: Path = LOG_ROOT) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []; owner_val = get_owner(owner).value
    for i in range(num_entities):
        name = f"alpha-{start_index + i:03d}"
        k = random.randint(2,5); chunks=[]
        for j in range(k):
            status = _pick(ALPHAS_STATUS_ORDER)
            abs_log = (log_root / "alphas" / owner_val / name / f"status-{j}.log")
            _mk_log(abs_log, f"[{iso_now()}] owner={owner_val} {name} c{j} {status}\n")
            proc = f"https://example.com/alphas/proc/{name}/{j}"
            chunks.append(_chunk(status, abs_log, proc, j))
        items.append({"owner": owner_val, "mode":"live", "data_name": name, "stage": "status", "chunks": chunks, "errors": []})
    return items

def make_strategies_payload_for_owner(owner: Owner, num_entities: int = 3, start_index: int = 0, log_root: Path = LOG_ROOT) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []; owner_val = get_owner(owner).value
    for i in range(num_entities):
        name = f"strategy-{start_index + i:03d}"
        k = random.randint(2,5); chunks=[]
        for j in range(k):
            status = _pick(STRATS_STATUS_ORDER)
            abs_log = (log_root / "strategies" / owner_val / name / f"status-{j}.log")
            _mk_log(abs_log, f"[{iso_now()}] owner={owner_val} {name} c{j} {status}\n")
            proc = f"https://example.com/strategies/proc/{name}/{j}"
            chunks.append(_chunk(status, abs_log, proc, j))
        items.append({"owner": owner_val, "mode":"live", "data_name": name, "stage": "status", "chunks": chunks, "errors": []})
    return items

def make_payload_for_owner(owner: Owner, tabs: Optional[List[str]] = None, num_per_tab: int = NUM_PER_TAB_DEFAULT, start_index_per_tab: Optional[Dict[str,int]] = None, log_root: Path = LOG_ROOT) -> Dict[str, Any]:
    tabs = [t.lower() for t in (tabs or TAB_IDS)]
    start_index_per_tab = start_index_per_tab or {}
    out = {"tabs": {}}
    for tab in tabs:
        si = int(start_index_per_tab.get(tab, 0))
        if tab == "data":
            snap = make_data_payload_for_owner(owner, num_entities=num_per_tab, start_index=si, log_root=log_root)
        elif tab == "features":
            snap = make_features_payload_for_owner(owner, num_entities=num_per_tab, start_index=si, log_root=log_root)
        elif tab == "alphas":
            snap = make_alphas_payload_for_owner(owner, num_entities=num_per_tab, start_index=si, log_root=log_root)
        elif tab == "strategies":
            snap = make_strategies_payload_for_owner(owner, num_entities=num_per_tab, start_index=si, log_root=log_root)
        else:
            continue
        out["tabs"][tab] = {"tab": tab, "snapshot": snap, "meta": _meta()}
    return out

def make_multi_owner_payload(owners: List[Owner], tabs: Optional[List[str]] = None, num_per_tab: int = NUM_PER_TAB_DEFAULT, start_index_per_tab: Optional[Dict[str,int]] = None, log_root: Path = LOG_ROOT) -> Dict[str, Any]:
    tabs = [t.lower() for t in (tabs or TAB_IDS)]
    start_index_per_tab = start_index_per_tab or {}
    merged = {"tabs": {t: {"tab": t, "snapshot": [], "meta": _meta()} for t in tabs}}
    for idx, owner in enumerate(owners):
        bundle = make_payload_for_owner(owner, tabs=tabs, num_per_tab=num_per_tab,
                                        start_index_per_tab={t: int(start_index_per_tab.get(t,0)) + idx*num_per_tab for t in tabs},
                                        log_root=log_root)
        for t in tabs:
            if t in bundle["tabs"]:
                merged["tabs"][t]["snapshot"].extend(bundle["tabs"][t]["snapshot"])
    return merged

# ---------------------------
# Save helpers (NEW)
# ---------------------------
def save_data_payload_for_owner(owner: Owner, out_dir: str | Path, **kwargs) -> Path:
    snap = make_data_payload_for_owner(owner, **kwargs)
    p = Path(out_dir) / "owners" / get_owner(owner).value / "data_snapshot.json"
    return _save_json(snap, p)

def save_features_payload_for_owner(owner: Owner, out_dir: str | Path, **kwargs) -> Path:
    snap = make_features_payload_for_owner(owner, **kwargs)
    p = Path(out_dir) / "owners" / get_owner(owner).value / "features_snapshot.json"
    return _save_json(snap, p)

def save_alphas_payload_for_owner(owner: Owner, out_dir: str | Path, **kwargs) -> Path:
    snap = make_alphas_payload_for_owner(owner, **kwargs)
    p = Path(out_dir) / "owners" / get_owner(owner).value / "alphas_snapshot.json"
    return _save_json(snap, p)

def save_strategies_payload_for_owner(owner: Owner, out_dir: str | Path, **kwargs) -> Path:
    snap = make_strategies_payload_for_owner(owner, **kwargs)
    p = Path(out_dir) / "owners" / get_owner(owner).value / "strategies_snapshot.json"
    return _save_json(snap, p)

def save_payload_for_owner_bundle(owner: Owner, out_dir: str | Path, tabs: Optional[List[str]] = None, **kwargs) -> Dict[str, Path]:
    bundle = make_payload_for_owner(owner, tabs=tabs, **kwargs)
    base = Path(out_dir) / "owners" / get_owner(owner).value
    paths = {"bundle": _save_json(bundle, base / "owner_bundle.json")}
    # also split per tab
    for tab, payload in bundle["tabs"].items():
        paths[tab] = _save_json(payload, base / f"{tab}_bundle.json")
    return paths

def save_multi_owner_payload_bundle(owners: List[Owner], out_dir: str | Path, tabs: Optional[List[str]] = None, **kwargs) -> Dict[str, Path]:
    bundle = make_multi_owner_payload(owners, tabs=tabs, **kwargs)
    base = Path(out_dir) / "multi"
    paths = {"bundle": _save_json(bundle, base / "multi_owner_bundle.json")}
    for tab, payload in bundle["tabs"].items():
        paths[tab] = _save_json(payload, base / f"{tab}_bundle.json")
    return paths

# ---------------------------
# Inject (optionally save)
# ---------------------------
def ingest_owner_payload(owner_bundle: Dict[str, Any], dash_url: str = DASH_URL, save_dir: str | Path | None = None) -> None:
    if save_dir:
        base = Path(save_dir) / "ingested" / "owners"
        owner_guess = None
        # try to pull from first snapshot item if available
        for tab in owner_bundle.get("tabs", {}).values():
            snap = tab.get("snapshot") or []
            if snap:
                owner_guess = (snap[0].get("owner") or "unknown").upper()
                break
        if not owner_guess: owner_guess = "unknown"
        _save_json(owner_bundle, _ensure_dir(base / owner_guess) / "owner_bundle_ingested.json")

    for tab, payload in owner_bundle.get("tabs", {}).items():
        resp = requests.post(dash_url, json=payload, timeout=20)
        ok = False
        try: ok = resp.ok and (resp.json().get("ok", True) is True)
        except Exception: pass
        print(f"[POST] owner-bundle tab={tab:<11} → {resp.status_code} {resp.reason}  ok={ok}")

def ingest_multi_owner_payload(bundle: Dict[str, Any], dash_url: str = DASH_URL, save_dir: str | Path | None = None) -> None:
    if save_dir:
        _save_json(bundle, _ensure_dir(Path(save_dir) / "ingested") / "multi_owner_bundle_ingested.json")
    for tab, payload in bundle.get("tabs", {}).items():
        resp = requests.post(dash_url, json=payload, timeout=20)
        ok = False
        try: ok = resp.ok and (resp.json().get("ok", True) is True)
        except Exception: pass
        print(f"[POST] multi-bundle tab={tab:<11} → {resp.status_code} {resp.reason}  ok={ok}")

# ---------------------------
# Demo
# ---------------------------
def demo_once(out_dir: str | Path = "samples") -> None:
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    owners = [get_owner(n) for n in _OWNER_NAMES]
    # per owner save & ingest
    for ow in owners:
        save_payload_for_owner_bundle(ow, out_dir=out_dir, tabs=TAB_IDS, num_per_tab=NUM_PER_TAB_DEFAULT, log_root=LOG_ROOT)
    # merged per tab
    multi = make_multi_owner_payload(owners=owners, tabs=TAB_IDS, num_per_tab=NUM_PER_TAB_DEFAULT, log_root=LOG_ROOT)
    save_multi_owner_payload_bundle(owners, out_dir=out_dir, tabs=TAB_IDS, num_per_tab=NUM_PER_TAB_DEFAULT, log_root=LOG_ROOT)
    ingest_multi_owner_payload(multi, dash_url=DASH_URL, save_dir=out_dir)

if __name__ == "__main__":
    print(f"DASH_URL={DASH_URL}")
    print(f"LOG_ROOT={LOG_ROOT}")
    print(f"OWNERS={_OWNER_NAMES}")
    demo_once(out_dir="samples")