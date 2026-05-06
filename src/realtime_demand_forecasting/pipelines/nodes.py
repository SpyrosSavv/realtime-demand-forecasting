from narwhals import dataframe
import pandas as pd
from typing import Dict, Any, Tuple, Union
from pathlib import Path

def rename_columns(df: pd.DataFrame, renaming_dict: Dict[str, str]) -> pd.DataFrame:
    """Rename columns based on column mapping"""
    return df.rename(columns=renaming_dict)

def get_features(df: pd.DataFrame, lag_params: Dict[str, Any]) -> Tuple[pd.DataFrame, pd.Timestamp]:
    """Create lag features for timeseries data.

        Generates lagged versions of specified columns, useful for capturing
        temporal patterns in timeseries forecasting. Missing values at the
        beginning of each lagged column are backfilled.

        Args:
            df: Input DataFrame containing the original features.
            lag_params: Dictionary mapping feature names to lists of lag values.
                Example: {"temperature": [1, 2, 3]} creates columns
                "temperature_lag_1", "temperature_lag_2", "temperature_lag_3".

        Returns:
            DataFrame with original columns plus new lag feature columns.
    """

    for feature, lags in lag_params.items():
        for lag in lags:
            df[f"{feature}_lag_{lag}"] = df[feature].shift(lag).bfill()
    timestamps = pd.to_datetime(df['datetime'])
    df.drop(columns=['datetime'], inplace=True)
    return df, timestamps

def make_target(df: pd.DataFrame, target_params: Dict[str, Any]) -> pd.DataFrame:
    """Create target column by shifting."""
    df[target_params["new_target_name"]] = (
        df[target_params["target_column"]].shift(-target_params["shift_period"]).ffill()
    )
    return df

def split_data(
    df: pd.DataFrame, 
    params: Dict[str, Any]
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split data into train/test sets."""
    # Get target column name
    target_name = params["target_params"]["new_target_name"]
    # Get features columns names
    features = [col for col in df.columns if col != target_name]
    # Split data into train/test sets
    x, y = df[features], df[target_name]
    train_size = int(params["train_fraction"] * len(df))
    x_train, x_test = x[:train_size], x[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    return x_train, x_test, y_train, y_test