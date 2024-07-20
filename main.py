import pandas as pd
from exploracionDx import tratamientoDx

def main():
    data = {'A': [1, 2, None, 4], 'B': [5, None, -7, 8], 'C': [9, 10, 11, 12]}
    df = pd.DataFrame(data)
    
    print(df)
    
    df_clean = tratamientoDx(df)
    
    print("\nDataFrame limpio:")
    print(df_clean)

if __name__ == "__main__":
    main()
