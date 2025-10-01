import pandas as pd
def validate_dataframe(df: pd.DataFrame, require_columns=None):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if require_columns:
        missing = [c for c in require_columns if c not in df.columns]
        if missing:
            raise ValueError(f"DataFrame is missing required columns: {missing}")
    return True
