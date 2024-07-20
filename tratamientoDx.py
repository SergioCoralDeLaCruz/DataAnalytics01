import pandas as pd

def tratamientoDx(df):
    df_clean = df.dropna()
    
    return df_clean