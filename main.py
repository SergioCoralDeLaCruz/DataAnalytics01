import pandas as pd
import tratamientoDx
import exploracionDx 

def main():
    data = {'A': [1, 2, None, 4], 'B': [5, None, -7, 8], 'C': [9, 10, 11, 12]}
    df = pd.DataFrame(data)
    
    print(df)
    
    df_clean = tratamientoDx.remove_columns_with_nulls(df)
    df_clean2 = tratamientoDx.remove_rows_with_nulls(df_clean)
    
    print("\nDataFrame limpio:")
    print(df_clean)
    
    print("\nVisualizar correlacion:")
    exploracionDx.plot_correlacion(df_clean)

    print("\nVisualizar pairplot:")
    exploracionDx.plot_pairplot(df_clean)
    
if __name__ == "__main__":
    main()
