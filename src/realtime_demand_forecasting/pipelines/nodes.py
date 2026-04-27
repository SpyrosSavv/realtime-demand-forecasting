import pandas as pd
from typing import Dict, Any, Tuple, Union
from pathlib import Path

def rename_columns(df: pd.DataFrame, renaming_dict: Dict[str, str]) -> pd.DataFrame:
    """Rename columns based on column mapping"""
    return df.rename(columns=renaming_dict)