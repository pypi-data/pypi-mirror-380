
from __future__ import annotations
import polars as pl
from dataclasses import dataclass
import numpy as np

@dataclass
class AlphaBlock:
    model_id: str
    model_version_id: str
    model_owner_id: str
    hyper_id: str
    target_universe: str
    target_name: str
    regime_id: str
    metrics: list[str]

    @staticmethod
    def fit_from_csv(*, config: dict) -> pl.DataFrame:
        # Minimal demo: read CSV, compute fake metrics by correlating features with returns
        import polars as pl, numpy as np
        p = config["data"]["csv_path"]
        time_col = config["data"]["time_col"]
        feat = config["data"]["feature_cols"]
        horizons = config["data"]["horizon_cols"]
        df = pl.read_csv(p).with_columns(pl.col(time_col).str.strptime(pl.Datetime, strict=False).alias(time_col))

        rows = []
        for h in horizons:
            for lag in config["model"]["lags"]:
                # naive "signal"
                s = df.select([pl.col(f) for f in feat]).to_numpy().sum(axis=1)
                r = df[h].shift(-lag).fill_null(0).to_numpy()
                if len(s)==0 or len(r)==0:
                    tstat, pval, sr, ir = 0.0, 1.0, 0.0, 0.0
                else:
                    cov = float(np.cov(s, r)[0,1]) if len(s)>1 else 0.0
                    var = float(np.var(s)) if np.var(s)!=0 else 1e-9
                    beta = cov / var
                    tstat = float(beta / (np.std(r)+1e-9))
                    pval = float(np.exp(-abs(tstat)))
                    sr = float(beta / (np.std(r)+1e-9))
                    ir = float(sr * np.sqrt(252))
                rows.append({
                    "time": df[time_col].max(),
                    "model_id": config["identity"]["model_id"],
                    "model_version_id": config["identity"]["model_version_id"],
                    "model_owner_id": config["identity"]["model_owner_id"],
                    "hyper_id": config["identity"]["hyper_id"],
                    "target_universe": config["target"]["universe"],
                    "target_name": config["target"]["name"],
                    "regime_id": config["regime_id"],
                    "horizon": int(''.join(filter(str.isdigit, h)) or 1),
                    "lag": lag,
                    "metric_name": "t_stat",
                    "metric_value": tstat,
                })
                for name,val in [("p_val",pval),("sharpe",sr),("ir",ir)]:
                    r2 = rows[-1].copy()
                    r2["metric_name"]=name; r2["metric_value"]=val
                    rows.append(r2)
        return pl.DataFrame(rows)

    @staticmethod
    def fit_from_regimes_lab(*,
                             features: pl.DataFrame,
                             labels_long: pl.DataFrame,
                             return_cols: dict[str, int],
                             lags: list[int],
                             target_universe: str = "UNKNOWN",
                             model_version_id: str = "v1",
                             model_owner_id: str = "regimes_lab",
                             hyper_id: str = "h0",
                             window: int = 120,
                             annualization: float = 252.0,
                             time_col: str = "time",
                             asset_col: str = "asset_id",
                             regime_models: list[str] | None = None) -> pl.DataFrame:
        """Build tall alpha metrics from regimes_lab labels and features.

        Wraps model_zoo.regimes_lab_bridge.build_alpha_from_regimes_lab.
        """
        from analytics.theta_surfaces_repo_base_v2.model_zoo.regimes_lab_bridge import (
            RegimeAlphaBuildCfg, build_alpha_from_regimes_lab
        )
        cfg = RegimeAlphaBuildCfg(
            time_col=time_col,
            asset_col=asset_col,
            return_cols=return_cols,
            lags=lags,
            window=window,
            annualization=annualization,
            target_universe=target_universe,
            model_version_id=model_version_id,
            model_owner_id=model_owner_id,
            hyper_id=hyper_id,
            regime_models=regime_models,
        )
        return build_alpha_from_regimes_lab(features=features, labels_long=labels_long, cfg=cfg)
