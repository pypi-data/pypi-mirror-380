
from __future__ import annotations
import polars as pl
import numpy as np

class ResidualUnwinder:
    """Utilities to unwind residualized returns into tradable stock weights.

    Inputs:
      - exposures: Polars DataFrame with columns: asset_id, factor_id, exposure
      - desired_weights: Polars DataFrame with columns: asset_id, w0  (raw desired weights; can be sparse)

    Functions:
      - preview_mimic_portfolios(...): (permission-gated) factor-mimicking portfolios per factor
      - neutralize_to_factors(...): adjust asset weights to be closest to w0 but with zero factor exposure
      - target_factor_exposure(...): as above, but enforce B^T w = target (vector), e.g., re-introduce factor tilts
    """
    def __init__(self, *, permissions: dict | None = None):
        self.permissions = permissions or {}

    @staticmethod
    def _to_mats(exposures: pl.DataFrame, desired_weights: pl.DataFrame | None = None):
        """Build (assets, factors, B, w0) from exposures and desired weights.
        Exposures may include an optional 'time' column; only the columns
        'asset_id', 'factor_id', 'exposure' are used.
        """
        if not {"asset_id","factor_id","exposure"}.issubset(set(exposures.columns)):
            raise ValueError("exposures must have columns: asset_id, factor_id, exposure")
        expo = exposures.select(["asset_id","factor_id","exposure"]).to_dicts()
        assets = exposures.select("asset_id").unique().to_series().to_list()
        factors = exposures.select("factor_id").unique().to_series().to_list()
        aidx = {a:i for i,a in enumerate(assets)}
        fidx = {f:i for i,f in enumerate(factors)}
        B = np.zeros((len(assets), len(factors)))
        for row in expo:
            a = row["asset_id"]; f = row["factor_id"]; x = row["exposure"]
            B[aidx[a], fidx[f]] = float(x)
        w0 = None
        if desired_weights is not None:
            if not {"asset_id","w0"}.issubset(set(desired_weights.columns)):
                raise ValueError("desired_weights must have columns: asset_id, w0")
            w0 = np.zeros((len(assets), 1))
            for a, w in desired_weights.select(["asset_id","w0"]).iter_rows():
                if a in aidx:
                    w0[aidx[a], 0] = float(w)
        return assets, factors, B, w0

    def preview_mimic_portfolios(self, *, exposures: pl.DataFrame) -> pl.DataFrame:
        """Return factor-mimicking portfolios (weights over assets for each factor).
        Solves min || B w_f - e_f || with identity target e_f for factor f, giving w_f = B (B^T B)^{-1} e_f.
        Requires permissions['reveal_mimic']=True.
        """
        if not self.permissions.get("reveal_mimic", False):
            raise PermissionError("Not allowed to reveal factor-mimicking portfolios")
        assets, factors, B, _ = self._to_mats(exposures, None)
        BtB = B.T @ B + 1e-9*np.eye(B.shape[1])
        inv = np.linalg.inv(BtB)
        W = B @ inv  # columns correspond to canonical basis in factor space
        # Build long-form table
        rows = []
        for j, f in enumerate(factors):
            for i, a in enumerate(assets):
                rows.append((f, a, float(W[i, j])))
        return pl.DataFrame({"factor_id":[r[0] for r in rows], "asset_id":[r[1] for r in rows], "weight":[r[2] for r in rows]})

    @staticmethod
    def _project_to_null(B: np.ndarray, w0: np.ndarray, Aeq: np.ndarray | None = None, beq: np.ndarray | None = None):
        """Project w0 to the null space of B^T (i.e., enforce B^T w = 0) with optional equality constraints Aeq w = beq.
        Solve: min ||w - w0||^2  s.t.  B^T w = 0  and Aeq w = beq.
        KKT: [I  B  Aeq^T][w]   = [w0]
             [B^T 0   0  ][λ]     [0 ]
             [Aeq 0   0  ][μ]     [beq]
        """
        n = B.shape[0]
        k = B.shape[1]
        I = np.eye(n)
        Bt = B.T
        m = Aeq.shape[0] if Aeq is not None else 0
        Aeq_mat = Aeq if Aeq is not None else np.zeros((0, n))
        # Assemble KKT blocks with consistent widths (n + k + m)
        top = np.hstack([I, B, Aeq_mat.T])
        mid = np.hstack([Bt, np.zeros((k, k)), np.zeros((k, m))])
        bot = np.hstack([Aeq_mat, np.zeros((m, k)), np.zeros((m, m))])
        K = np.vstack([top, mid, bot])
        rhs = np.vstack([w0, np.zeros((k, 1)), beq if beq is not None else np.zeros((m, 1))])
        sol = np.linalg.lstsq(K, rhs, rcond=None)[0]
        w = sol[:n]
        return w

    def neutralize_to_factors(self, *, exposures: pl.DataFrame, desired_weights: pl.DataFrame, budget: float | None = None) -> pl.DataFrame:
        """Return adjusted weights w* closest to w0 but with zero factor exposure (B^T w* = 0).
        If budget is provided, also enforce sum(w*) = budget.
        """
        assets, factors, B, w0 = self._to_mats(exposures, desired_weights)
        Aeq = None; beq = None
        if budget is not None:
            Aeq = np.ones((1, B.shape[0]))
            beq = np.array([[budget]])
        w = self._project_to_null(B, w0, Aeq=Aeq, beq=beq)
        return pl.DataFrame({"asset_id": assets, "w_adj": [float(x) for x in w.flatten()]})

    def target_factor_exposure(self, *, exposures: pl.DataFrame, desired_weights: pl.DataFrame, target: dict[str,float], budget: float | None = None) -> pl.DataFrame:
        """As above, but enforce B^T w = t (vector of target factor exposures).
        'target' is a dict of {factor_id: exposure}.
        """
        assets, factors, B, w0 = self._to_mats(exposures, desired_weights)
        t = np.zeros((B.shape[1], 1))
        for j,f in enumerate(factors):
            t[j,0] = float(target.get(f, 0.0))
        # Use same KKT trick but shift w0 by a feasible particular solution. Solve min||w - w0|| s.t. Bt w = t.
        # Convert by augmenting RHS in KKT system: B^T w = t.
        n = B.shape[0]; k = B.shape[1]
        I = np.eye(n); Bt = B.T
        Aeq_rows = 1 if budget is not None else 0
        Aeq = np.ones((1,n)) if budget is not None else np.zeros((0,n))
        beq = np.array([[budget]]) if budget is not None else np.zeros((0,1))
        # Assemble KKT
        top = np.hstack([I, B, Aeq.T])
        mid = np.hstack([Bt, np.zeros((k,k)), np.zeros((k,Aeq_rows))])
        bot = np.hstack([Aeq, np.zeros((Aeq_rows,k)), np.zeros((Aeq_rows,Aeq_rows))])
        K = np.vstack([top, mid, bot])
        rhs = np.vstack([w0, t, beq])
        sol = np.linalg.lstsq(K, rhs, rcond=None)[0]
        w = sol[:n]
        return pl.DataFrame({"asset_id": assets, "w_adj": [float(x) for x in w.flatten()]})
