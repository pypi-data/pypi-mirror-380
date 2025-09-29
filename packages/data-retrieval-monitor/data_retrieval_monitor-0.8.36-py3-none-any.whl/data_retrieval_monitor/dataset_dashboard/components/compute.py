from typing import Dict, List, Optional, Tuple
from ..constants import DATA_STAGES, status_order_for_tab, status_scores_for_tab

def best_status(counts: Dict[str,int], tab: str) -> Optional[str]:
    for s in status_order_for_tab(tab):
        if int(counts.get(s, 0) or 0) > 0:
            return s
    return None

def aggregate_counts(store: dict, tab: str) -> Dict[str,int]:
    tree = store.get("tabs", {}).get(tab, {}) or store  # accept flat or nested
    jobs = tree.get("jobs", {}) or {}
    tot = {s:0 for s in status_order_for_tab(tab)}
    for o_map in jobs.values():
        for m_map in o_map.values():
            for d_map in m_map.values():
                for leaf in d_map.values():
                    for s, v in (leaf.get("counts") or {}).items():
                        if s in tot: tot[s] += int(v or 0)
    return tot

def filtered_stage_counts(store: dict, owner: Optional[str], mode: Optional[str], stage: str, tab: str) -> Dict[str,int]:
    assert tab == "data", "filtered_stage_counts is only for Data tab stages"
    tree = store.get("tabs", {}).get("data", {}) or store
    jobs = tree.get("jobs", {}) or {}

    owner_sel = (owner or "").lower(); want_owner = None if owner_sel in ("","all") else owner_sel
    mode_sel  = (mode  or "").lower(); want_mode  = None if mode_sel  in ("","all") else mode_sel

    tot = {s:0 for s in status_order_for_tab("data")}
    for own, o_map in jobs.items():
        if want_owner and own != want_owner: continue
        for md, m_map in o_map.items():
            if want_mode and md != want_mode: continue
            for d_map in m_map.values():
                leaf = d_map.get(stage)
                if not leaf: continue
                for s, v in (leaf.get("counts") or {}).items():
                    if s in tot:
                        tot[s] += int(v or 0)
    return tot

def _avg_scores_for(tab: str, d_map: dict, sel_stages: List[str]) -> Tuple[float, float]:
    scores = status_scores_for_tab(tab)
    chunk_scores: List[float] = []
    status_set: set = set()
    buckets = sel_stages if tab == "data" else ["status"]
    for stg in buckets:
        leaf = d_map.get(stg)
        if not leaf: continue
        for ch in leaf.get("chunks", []):
            st = (ch.get("status") or "other")
            if st not in scores: st = "other"
            chunk_scores.append(scores.get(st, 0.0))
            status_set.add(st)
    avg_chunk = (sum(chunk_scores)/len(chunk_scores)) if chunk_scores else 0.0
    avg_status = (sum(scores.get(s,0.0) for s in status_set)/len(status_set)) if status_set else 0.0
    return avg_chunk, avg_status

def make_sort_key(tab: str, d_map: dict, dataset_name: str, owner: str, mode: str,
                  sel_stages: List[str], kind: str) -> Tuple:
    avg_chunk, avg_status = _avg_scores_for(tab, d_map, sel_stages)
    if kind == "chunk_asc":     sk = ( avg_chunk, dataset_name.lower(), owner.lower(), mode.lower())
    elif kind == "chunk_desc":  sk = (-avg_chunk, dataset_name.lower(), owner.lower(), mode.lower())
    elif kind == "status_asc":  sk = ( avg_status, dataset_name.lower(), owner.lower(), mode.lower())
    elif kind == "status_desc": sk = (-avg_status, dataset_name.lower(), owner.lower(), mode.lower())
    else:                       sk = ( dataset_name.lower(), owner.lower(), mode.lower())
    return sk