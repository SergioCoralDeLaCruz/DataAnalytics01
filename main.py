import pandas as pd
<<<<<<< HEAD
import tratamientoDx as trat
=======
from tratamientoDx import drop_nulls
from exploracionDx import plot_correlacion
>>>>>>> 815b367b88094887fd15ae324316e73f97aca0e3

def main():
    data = {'A': [1, 2, None, 4], 'B': [5, None, -7, 8], 'C': [9, 10, 11, 12]}
    df = pd.DataFrame(data)
    
    print(df)
    
    df_clean = trat.remove_columns_with_nulls(df)
    df_clean2 = trat.remove_rows_with_nulls(df_clean)
    
    print("\nDataFrame limpio:")
    print(df_clean)
    
    print("\nVisualizar correlacion:")
    plot_correlacion(df_clean)
    
if __name__ == "__main__":
    main()
