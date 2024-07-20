import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlacion(df):
    # Obtener las columnas numéricas
    columnas_numericas = df.select_dtypes(include='number').columns

    # Calcular la matriz de correlación de Pearson
    matriz_correlacion = df[columnas_numericas].corr(method='pearson')

    # Graficar la matriz de correlación
    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
    plt.title('Matriz de Correlación de Pearson')
    plt.show()

def plot_pairplot(df, hue=None):
   
    sns.pairplot(df, hue=hue)
    plt.show()