from __future__ import annotations
import polars as pl

def table_by_metric(df: pl.DataFrame, *, metric: str, value_col: str = "metric_value") -> pl.DataFrame:
    """Lag × horizon table for a given metric from tall alpha DataFrame."""
    sub = df.filter(pl.col("metric_name") == metric)
    return sub.pivot(index="lag", columns="horizon", values=value_col, aggregate_function="mean").sort("lag")

def plot_surface_3d(df: pl.DataFrame, *, metric: str, value_col: str = "metric_value", title: str | None = None, save_path: str | None = None):
    """Render a 3D surface for metric over (horizon, lag)."""
    tab = table_by_metric(df, metric=metric, value_col=value_col)
    try:
        import numpy as np
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
    except Exception as e:
        print(f"plot_surface_3d: matplotlib unavailable: {e}")
        return None
    cols = tab.columns
    Hs = [c for c in cols if c != 'lag']
    Ls = tab.select('lag').to_series().to_list()
    Z = tab.select(Hs).to_numpy()
    import numpy as np
    Hm, Lm = np.meshgrid(np.asarray(Hs, dtype=float), np.asarray(Ls, dtype=float))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(Hm, Lm, Z)
    ax.set_xlabel('Horizon'); ax.set_ylabel('Lag'); ax.set_zlabel(metric)
    ax.set_title(title or f"{metric} surface")
    if save_path:
        fig.savefig(save_path, bbox_inches='tight')
    return fig

