import pandas as pd

def merge_datasets(df1: pd.DataFrame, df2: pd.DataFrame, on_field: str, how: str = "inner") -> pd.DataFrame:
    """
    Merge two datasets on a user-specified field.
    """
    if on_field not in df1.columns or on_field not in df2.columns:
        raise ValueError(f"'{on_field}' must exist in both datasets")
    
    merged_df = pd.merge(df1, df2, on=on_field, how=how)
    return merged_df
