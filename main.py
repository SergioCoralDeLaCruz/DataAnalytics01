import pandas as pd
import tratamientoDx as trat
import exploracionDx as explo

def main():
    data = {'A': [1, 2, None, 4], 'B': [5, None, -7, 8], 'C': [9, 10, 11, 12]}
    df = pd.DataFrame(data)
    
    print(df)
    
    df_clean = trat.remove_columns_with_nulls(df)
    df_clean2 = trat.remove_rows_with_nulls(df_clean)
    
    print("\nDataFrame limpio:")
    print(df_clean)
    
    print("\nVisualizar correlacion:")
    explo.plot_correlacion(df_clean)
    
if __name__ == "__main__":
    main()
