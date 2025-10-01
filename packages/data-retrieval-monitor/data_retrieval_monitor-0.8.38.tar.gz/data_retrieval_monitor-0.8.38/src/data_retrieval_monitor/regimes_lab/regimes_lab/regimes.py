# === add near imports ===
import hashlib, json, os
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score

try:
    import ruptures as rpt
    _RUPTURES_OK = True
except Exception:
    _RUPTURES_OK = False

try:
    from hmmlearn.hmm import GaussianHMM  # optional
    _HMM_OK = True
except Exception:
    GaussianHMM = None
    _HMM_OK = False

# optional deep models (only used if available)
try:
    from regimes_lab.models.saint import SaintRegimes  # your real impl
    _SAINT_OK = True
except Exception:
    _SAINT_OK = False

try:
    from regimes_lab.models.vqvae import VQVAERegimes  # your real impl
    _VQVAE_OK = True
except Exception:
    _VQVAE_OK = False

# configs
from .configs import N_CLUSTERS, CPD, TRAIN_FRAC, VAL_FRAC

# ---------------- cache paths ----------------
REGIME_CACHE_DIR = Path("./regimes_lab/output/regimes")
MODEL_DIR        = REGIME_CACHE_DIR / "models"
REGIME_CACHE_DIR.mkdir(parents=True, exist_ok=True)
MODEL_DIR.mkdir(parents=True, exist_ok=True)

# ---------------- helpers for configuration ----------------

_DEFAULT_MODEL_LIST = [
    # base clusters
    "kmeans2","kmeans3","kmeans4",
    "gmm2","gmm3","gmm4",
    "pca2_kmeans2","pca2_kmeans3","pca3_kmeans2","pca3_kmeans3",
    "sign_posneg",
    "hmm_gauss",
    # interpretable / aligned (depend on base)
    "tree_from_kmeans3",
    "cpd_aligned",
    # heavy (optional)
    "saint","vqvae",
]

def _models_from_env(defaults: list[str]) -> list[str]:
    s = os.getenv("REGIMES_LAB_MODELS")
    if not s:
        return defaults
    return [m.strip() for m in s.split(",") if m.strip()]

def _fingerprint_IND_and_cfg(IND: pd.DataFrame, cfg: dict) -> str:
    h = hashlib.sha256()
    h.update(str(list(map(str, IND.index))).encode("utf-8"))
    h.update(str(list(map(str, IND.columns))).encode("utf-8"))
    h.update(str(IND.shape).encode("utf-8"))
    h.update(json.dumps(cfg, sort_keys=True).encode("utf-8"))
    return h.hexdigest()[:16]

def _labels_cache_paths(split_tag: str) -> tuple[Path, Path]:
    return (REGIME_CACHE_DIR / f"labels_{split_tag}.parquet",
            REGIME_CACHE_DIR / f"labels_{split_tag}.meta.json")

def _try_load_labels(split_tag: str, fp: str) -> tuple[pd.DataFrame | None, dict | None]:
    lab_p, meta_p = _labels_cache_paths(split_tag)
    if not (lab_p.exists() and meta_p.exists()):
        return None, None
    try:
        meta = json.loads(meta_p.read_text())
        if meta.get("fingerprint") != fp:
            return None, None
        df = pd.read_parquet(lab_p)
        if isinstance(df, pd.DataFrame) and df.shape[0] > 0:
            return df, meta
    except Exception:
        return None, None
    return None, None

def _save_labels(split_tag: str, fp: str, L: pd.DataFrame, extra: dict | None = None):
    lab_p, meta_p = _labels_cache_paths(split_tag)
    L.to_parquet(lab_p, index=True)
    meta = {"fingerprint": fp, "nrows": int(L.shape[0]), "ncols": int(L.shape[1]), "cols": list(L.columns)}
    if extra: meta.update(extra)
    meta_p.write_text(json.dumps(meta, indent=2))

# ---------------- utilities ----------------

def _std(X: np.ndarray) -> np.ndarray:
    mu = X.mean(0)
    sd = X.std(0); sd[sd == 0] = 1.0
    return (X - mu) / sd

def _remap_to_0k(s: pd.Series) -> pd.Series:
    v = pd.Series(s).astype(int)
    uniq = sorted(pd.unique(v))
    map_ = {u: i for i, u in enumerate(uniq)}
    out = v.map(map_).astype(int)
    # ensure >=2 classes
    if out.nunique() < 2 and len(out) >= 2:
        half = len(out)//2
        arr = out.values.copy()
        arr[half:] = (arr[half:] + 1) % 2
        out = pd.Series(arr, index=v.index, name=v.name).astype(int)
    out.name = s.name
    return out

# ---------------- base models ----------------

def _kmeans_k(IND: pd.DataFrame, k: int, name: str) -> pd.Series:
    X = _std(IND.values.astype(float))
    labs = KMeans(n_clusters=k, n_init=20, random_state=0).fit_predict(X)
    return pd.Series(labs, index=IND.index, name=name)

def _gmm_k(IND: pd.DataFrame, k: int, name: str) -> pd.Series:
    X = _std(IND.values.astype(float))
    gmm = GaussianMixture(n_components=k, covariance_type="full", random_state=0)
    labs = gmm.fit_predict(X)
    return pd.Series(labs, index=IND.index, name=name)

def _pca_kmeans_qk(IND: pd.DataFrame, q: int, k: int, name: str) -> pd.Series:
    X = _std(IND.values.astype(float))
    q = max(1, min(q, X.shape[1]-1 if X.shape[1] > 1 else 1, X.shape[0]-1))
    Xp = PCA(n_components=q, random_state=0).fit_transform(X)
    labs = KMeans(n_clusters=k, n_init=20, random_state=0).fit_predict(Xp)
    return pd.Series(labs, index=IND.index, name=name)

def _sign_posneg(IND: pd.DataFrame) -> pd.Series:
    s = (IND.values > 0).astype(int)
    codes = (s * (2 ** np.arange(s.shape[1]))).sum(axis=1)
    uniq = np.unique(codes)
    if len(uniq) <= 8:
        mapping = {v: i for i, v in enumerate(sorted(uniq))}
        labs = pd.Series(codes).map(mapping).values
    else:
        labs = KMeans(n_clusters=8, n_init=10, random_state=0).fit_predict(codes.reshape(-1,1))
    return pd.Series(labs, index=IND.index, name="sign_posneg")

def _hmm_gauss(IND: pd.DataFrame, n_components: int = 3) -> pd.Series:
    X = _std(IND.values.astype(float))
    if not _HMM_OK or X.shape[0] < 20:
        labs = KMeans(n_clusters=n_components, n_init=20, random_state=0).fit_predict(X)
        return pd.Series(labs, index=IND.index, name="hmm_gauss")
    km = KMeans(n_clusters=n_components, n_init=10, random_state=0).fit(X)
    z = km.labels_; means = km.cluster_centers_
    A = np.ones((n_components, n_components))
    for i in range(len(z)-1): A[z[i], z[i+1]] += 1
    A /= A.sum(1, keepdims=True)
    pi = (np.bincount(z, minlength=n_components) + 1).astype(float); pi /= pi.sum()
    hmm = GaussianHMM(n_components=n_components, covariance_type="full",
                      n_iter=800, tol=1e-4, random_state=0, params="stmc", init_params="")
    hmm.startprob_ = pi; hmm.transmat_ = A; hmm.means_ = means
    cov = np.cov(X.T) + 1e-3*np.eye(X.shape[1])
    hmm.covars_ = np.stack([cov]*n_components)
    hmm.fit(X)
    labs = hmm.predict(X)
    return pd.Series(labs, index=IND.index, name="hmm_gauss")

# ---------------- interpretable add-ons ----------------

def _tree_from_base(IND: pd.DataFrame, base: pd.Series, name: str) -> pd.Series:
    X = IND.values.astype(float)
    y = base.values.astype(int)
    tree = DecisionTreeClassifier(max_depth=4, min_samples_leaf=25, random_state=0)
    tree.fit(X, y)
    pred = tree.predict(X)
    if len(np.unique(pred)) < 2:
        pred = y
    return pd.Series(pred, index=IND.index, name=name)

def _sym_kl(mu1, cov1, mu2, cov2, eps=1e-9):
    inv2 = np.linalg.pinv(cov2 + eps*np.eye(len(mu2)))
    inv1 = np.linalg.pinv(cov1 + eps*np.eye(len(mu1)))
    d = len(mu1)
    t12 = np.trace(inv2 @ cov1)
    t21 = np.trace(inv1 @ cov2)
    dm = (mu2 - mu1).reshape(-1,1)
    q12 = (dm.T @ inv2 @ dm)[0,0]
    q21 = (dm.T @ inv1 @ dm)[0,0]
    k12 = 0.5*(t12 + q12 - d + np.log(np.linalg.det(cov2+eps*np.eye(d))/np.linalg.det(cov1+eps*np.eye(d))))
    k21 = 0.5*(t21 + q21 - d + np.log(np.linalg.det(cov1+eps*np.eye(d))/np.linalg.det(cov2+eps*np.eye(d))))
    return float(k12 + k21)

def _cpd_aligned(IND: pd.DataFrame, base: pd.Series, threshold: float, name: str) -> pd.Series:
    X = _std(IND.values.astype(float))
    T = X.shape[0]
    if not _RUPTURES_OK or T < 50:
        return pd.Series(base.values, index=IND.index, name=name)
    n_tr = int(TRAIN_FRAC * T); n_va = int(VAL_FRAC * T); te0 = n_tr + n_va
    X_tr = X[:n_tr]
    base_tr = base.values[:n_tr].astype(int)
    ids = np.unique(base_tr)
    ref_stats = {}
    for r in ids:
        Xr = X_tr[base_tr == r]
        if len(Xr) < 5: continue
        ref_stats[r] = (Xr.mean(0), np.cov(Xr.T) + 1e-6*np.eye(Xr.shape[1]))
    n_bkps = max(1, min(int(CPD.get("BINSEG_N_BKPS", 6)), T // 50))
    algo = rpt.Binseg(model=CPD.get("MODEL", "l2")).fit(X)
    bkps = algo.predict(n_bkps=n_bkps)
    seg = np.zeros(T, dtype=int)
    start = 0
    for end in bkps:
        Xt = X[start:end]
        Xt_tr = Xt[min(start, n_tr):max(min(end, n_tr), start)] if start < n_tr else None
        Xm = Xt_tr if (Xt_tr is not None and len(Xt_tr) >= 5) else Xt
        mu = Xm.mean(0); cov = np.cov(Xm.T) + 1e-6*np.eye(Xm.shape[1])
        best, best_d = None, np.inf
        for r, (m, S) in ref_stats.items():
            d = _sym_kl(mu, cov, m, S)
            if d < best_d:
                best_d, best = d, r
        if best is None:
            best = int(base.iloc[(start+end)//2])
        if best_d > float(threshold):
            best = int(ids.max() + 1)
        seg[start:end] = best
        start = end
    out = pd.Series(seg.astype(int), index=IND.index, name=name)
    return _remap_to_0k(out)

# ---------------- heavy models save/load ----------------

def _model_path(model_name: str, fp: str) -> Path:
    return MODEL_DIR / f"{model_name}_{fp}.pt"

def _save_saint(model: "SaintRegimes", fp: str):
    try:
        import torch
        p = _model_path("saint", fp)
        torch.save({"enc": model.enc.state_dict(),
                    "head": model.head.state_dict(),
                    "cfg": dict(
                        n_features=model.n_features, d_model=model.d_model,
                        depth=model.depth, nhead=model.nhead, dropout=model.dropout,
                        seed=model.seed, n_clusters=model.n_clusters)}, p)
    except Exception:
        pass

def _load_saint(n_features: int, fp: str) -> "SaintRegimes | None":
    if not _SAINT_OK: return None
    try:
        import torch
        p = _model_path("saint", fp)
        if not p.exists(): return None
        ck = torch.load(p, map_location="cpu")
        m = SaintRegimes(n_features=n_features, d_model=ck["cfg"]["d_model"],
                         depth=ck["cfg"]["depth"], nhead=ck["cfg"]["nhead"],
                         dropout=ck["cfg"]["dropout"], seed=ck["cfg"]["seed"],
                         n_clusters=ck["cfg"]["n_clusters"])
        m.enc.load_state_dict(ck["enc"]); m.head.load_state_dict(ck["head"])
        return m
    except Exception:
        return None

def _save_vqvae(model: "VQVAERegimes", fp: str):
    try:
        import torch
        p = _model_path("vqvae", fp)
        torch.save({
            "enc": model.enc.state_dict(),
            "dec": model.dec.state_dict(),
            "vq":  model.vq.state_dict(),
            "cfg": dict(k=model.k, embed_dim=model.embed_dim, seed=model.seed,
                        dropout=model.dropout, input_norm=model.input_norm)
        }, p)
    except Exception:
        pass

def _load_vqvae(d_in: int, fp: str) -> "VQVAERegimes | None":
    if not _VQVAE_OK: return None
    try:
        import torch
        p = _model_path("vqvae", fp)
        if not p.exists(): return None
        ck = torch.load(p, map_location="cpu")
        m = VQVAERegimes(k=ck["cfg"]["k"], embed_dim=ck["cfg"]["embed_dim"],
                         dropout=ck["cfg"]["dropout"], input_norm=ck["cfg"]["input_norm"],
                         seed=ck["cfg"]["seed"])
        # bootstrap shapes if needed
        m.fit(np.random.randn(8, d_in).astype(np.float32))
        m.enc.load_state_dict(ck["enc"]); m.dec.load_state_dict(ck["dec"]); m.vq.load_state_dict(ck["vq"])
        return m
    except Exception:
        return None

# ---------------- model dispatcher ----------------

def _build_model(name: str, IND: pd.DataFrame, base: pd.Series | None, fp: str) -> pd.Series | None:
    try:
        if name == "sign_posneg":
            return _remap_to_0k(_sign_posneg(IND))
        if name == "hmm_gauss":
            # you may swap 3 -> N_CLUSTERS if desired
            return _remap_to_0k(_hmm_gauss(IND, n_components=3))
        if name.startswith("kmeans"):
            k = int(name.replace("kmeans",""))
            return _remap_to_0k(_kmeans_k(IND, k, name=name))
        if name.startswith("gmm"):
            k = int(name.replace("gmm",""))
            return _remap_to_0k(_gmm_k(IND, k, name=name))
        if name.startswith("pca"):
            pq, pk = name.split("_")
            q = int(pq.replace("pca","")); k = int(pk.replace("kmeans",""))
            return _remap_to_0k(_pca_kmeans_qk(IND, q, k, name=name))
        if name in {"tree_from_kmeans3","tree_from_base"}:
            if base is None: return None
            nm = name
            if name == "tree_from_kmeans3" and not ((base.name or "").startswith("kmeans3")):
                nm = "tree_from_base"
            return _remap_to_0k(_tree_from_base(IND, base, nm))
        if name == "cpd_aligned":
            if base is None or not _RUPTURES_OK: return None
            thr = float(CPD.get("ALIGN_KL_THRESH", 50.0))
            return _remap_to_0k(_cpd_aligned(IND, base, threshold=thr, name="cpd_aligned"))
        if name == "saint":
            if not _SAINT_OK: return None
            X_np = IND.values.astype(np.float32)
            model = _load_saint(n_features=X_np.shape[1], fp=fp)
            if model is None:
                try:
                    model = SaintRegimes(n_features=X_np.shape[1], n_clusters=N_CLUSTERS, seed=0)
                    model.fit(X_np)
                    _save_saint(model, fp)
                except Exception:
                    return None
            labs = model.predict(X_np)
            return _remap_to_0k(pd.Series(labs, index=IND.index, name="saint"))
        if name == "vqvae":
            if not _VQVAE_OK: return None
            X_np = IND.values.astype(np.float32)
            model = _load_vqvae(d_in=X_np.shape[1], fp=fp)
            if model is None:
                try:
                    model = VQVAERegimes(k=N_CLUSTERS, seed=0)
                    model.fit(X_np)
                    _save_vqvae(model, fp)
                except Exception:
                    return None
            labs = model.predict(X_np)
            return _remap_to_0k(pd.Series(labs, index=IND.index, name="vqvae"))
    except Exception:
        return None
    return None

# ---------------- the main builder (drop-in) ----------------

def load_or_build_labels(IND: pd.DataFrame, split_tag: str = "full",
                         cache_ok: bool = True,
                         train_if_missing: bool = True,
                         models: list[str] | None = None) -> pd.DataFrame:
    """
    Build a wide DataFrame of regime labels. The set/ordering of models is configurable:

      - default list (if no override):
        kmeans2/3/4, gmm2/3/4, pca2_kmeans2/3, pca3_kmeans2/3, sign_posneg,
        hmm_gauss, tree_from_kmeans3, cpd_aligned, saint, vqvae.

      - override via:
          * `models=[...]` argument, or
          * env var REGIMES_LAB_MODELS="kmeans3,gmm4,saint"

    Cache behavior:
      * Cache key fingerprints data + cfg (not the model list). Meta stores built columns.
      * If the cache exists and contains a **superset** of requested models, we subset and return.
      * Otherwise we rebuild and save the full requested set.
    """
    IND = IND.copy()
    if not isinstance(IND.index, pd.DatetimeIndex):
        IND.index = pd.to_datetime(IND.index)
    IND = IND.sort_index()

    cfg = {
        "N_CLUSTERS": int(N_CLUSTERS),
        "CPD": dict(CPD) if isinstance(CPD, dict) else {},
        "versions": {"core": 3},  # bump if you change algorithms materially
    }
    fp = _fingerprint_IND_and_cfg(IND, cfg)

    # determine wanted list
    wanted = _models_from_env(_DEFAULT_MODEL_LIST)
    if models is not None:
        wanted = [m for m in models]  # copy

    # try cache
    if cache_ok:
        cached, meta = _try_load_labels(split_tag, fp)
        if cached is not None and meta is not None:
            built_cols = list(meta.get("cols", []))
            # if user requests a subset of cached columns -> just return subset
            if all(m in built_cols for m in wanted):
                out = cached[wanted].copy()
                return out
            # else: fall through to rebuild

    if not train_if_missing and not cache_ok:
        raise RuntimeError("Labels cache missing/stale and training disabled. Run training first.")

    cols: list[pd.Series] = []

    # --- First pass: build base candidates (for selecting 'base') ---
    base_candidates = [n for n in wanted if n.startswith("kmeans")]
    built_base: list[pd.Series] = []
    for n in base_candidates:
        s = _build_model(n, IND, base=None, fp=fp)
        if s is not None:
            built_base.append(s)
            cols.append(s)

    # choose base (prefer kmeans3 if present)
    base = None
    for c in built_base:
        if (c.name or "").startswith("kmeans3"):
            base = c; break
    if base is None and built_base:
        base = built_base[0]

    # --- Second pass: build remaining models in the requested order ---
    for n in [m for m in wanted if m not in base_candidates]:
        s = _build_model(n, IND, base=base, fp=fp)
        if s is not None:
            cols.append(s)

    # absolute fallback
    if not cols:
        labs = np.zeros(len(IND), dtype=int); labs[len(IND)//2:] = 1
        L = pd.DataFrame({"fallback": labs}, index=IND.index)
    else:
        # keep only requested names (and only those successfully built)
        L = pd.concat(cols, axis=1)
        keep = [c for c in wanted if c in L.columns]
        if keep:
            L = L[keep]
        else:
            # should not happen, but keep safety
            L = L

    _save_labels(split_tag, fp, L, extra={"models_requested": wanted, "models_built": list(L.columns)})
    # Optional: print which ones built for quick sanity
    try:
        print(f"[regimes_lab] built models ({len(L.columns)}): {list(L.columns)}")
    except Exception:
        pass
    return L