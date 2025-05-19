import pandas as pd

def convert_to_jst(df, columns):
    """
    Convert specified columns in a DataFrame to JST
    Args:
        df : targeted DataFrame
        columns : list of columns to convert
    Returns: 
        DataFrame with specified columns converted to JST

    Usage:
        cols = ['Started', 'Finished', 'Updated']
        train_df = convert_to_jst(train_df, cols)
    """
    for col in columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            if df[col].dt.tz is None:
                # Naive datetime: assume it's already in JST, do nothing or add warning
                print(f"Column '{col}' is naive. Skipping tz conversion to avoid incorrect shift.")
            else:
                # Aware datetime: convert to JST
                df[col] = df[col].dt.tz_convert('Asia/Tokyo')
        else:
            # If not already datetime, try parsing it
            try:
                df[col] = pd.to_datetime(df[col], utc=True).dt.tz_convert('Asia/Tokyo')
            except Exception as e:
                print(f"Could not convert column '{col}': {e}")
    return df
