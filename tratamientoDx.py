import pandas as pd

def remove_columns_with_nulls(df):
    return df.dropna(axis=1)

def remove_rows_with_nulls(df):
    return df.dropna(axis=0)