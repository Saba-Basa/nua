import pandas as pd

def fit_quantile_bins(df: pd.DataFrame, n_bins=4):
    edges = {}
    for col in df.columns:
        _, bins = pd.qcut(df[col], q=n_bins, retbins=True, duplicates="drop")
        edges[col] = bins
    return edges

def transform_with_bins(df: pd.DataFrame, edges: dict) -> pd.DataFrame:
    out = pd.DataFrame(index=df.index)
    for col, bins in edges.items():
        out[col] = pd.cut(df[col], bins=bins, labels=False, include_lowest=True)
    return out
