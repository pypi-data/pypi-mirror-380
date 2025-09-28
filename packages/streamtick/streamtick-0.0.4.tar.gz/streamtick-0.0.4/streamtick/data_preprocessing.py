import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    preprocesses the raw stock data for time-series analysis.
    handles MultiIndex (Ticker, Date), extracts 'Close' prices,
    and applies transformations for ARIMA.
    """
    if df is None or df.empty:
        print("Input DataFrame is empty or None. Preprocessing aborted.")
        return None

    # step 1: flatten MultiIndex columns (Ticker, Field) into "Field_Ticker"
    df.columns = [
        f"{col[0]}_{col[1]}" if isinstance(col, tuple) else col
        for col in df.columns
    ]

    # step 2: select only "Close_*" columns
    close_cols = [col for col in df.columns if col.startswith("Close_")]
    processed_df = df[close_cols].copy()

    # fill missing values
    processed_df.ffill(inplace=True)
    processed_df.bfill(inplace=True)

    # step 3: add SMA_30 and differencing per ticker
    for col in close_cols:
        ticker = col.split("_")[1]
        processed_df[f"SMA_30_{ticker}"] = processed_df[col].rolling(window=30).mean()
        processed_df[f"Close_Diff_{ticker}"] = processed_df[col].diff(periods=1)

    # drop NaNs created by rolling/diff
    processed_df.dropna(inplace=True)

    if processed_df.isnull().values.any():
        print("Warning: Missing values still exist after preprocessing.")

    return processed_df
