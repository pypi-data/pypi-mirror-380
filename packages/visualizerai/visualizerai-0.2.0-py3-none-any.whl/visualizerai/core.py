import pandas as pd
import matplotlib.pyplot as plt
from .utils import validate_dataframe

def plot_time_series(df: pd.DataFrame, column: str, index_col=None, title=None, save_path=None):
    validate_dataframe(df, require_columns=[column] + ([index_col] if index_col else []))
    plot_df = df.copy()
    if index_col:
        plot_df = plot_df.set_index(index_col)
        try:
            plot_df.index = pd.to_datetime(plot_df.index)
        except Exception:
            pass
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(plot_df.index, plot_df[column], marker='o')
    ax.set_title(title or f"{column} over time")
    ax.set_xlabel(index_col or "index")
    ax.set_ylabel(column)
    ax.grid(True)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
    return fig

def summary_report(df: pd.DataFrame) -> dict:
    validate_dataframe(df)
    return {
        "shape": df.shape,
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isna().sum().to_dict(),
        "describe": df.describe(include='all', datetime_is_numeric=True).to_dict()
    }
