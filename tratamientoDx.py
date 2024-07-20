import pandas as pd

def drop_nulls(df):
    df_clean = df.dropna()
    
    return df_clean