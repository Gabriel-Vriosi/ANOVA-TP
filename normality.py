"""Módulo donde se prueba la normalidad de la poblacion de la que 
proviene la muestra a partir de los residuos del modelo ANOVA"""

from scipy.stats import shapiro, probplot
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols 

def calc_residuos(dataframe):    
    """Calculo de residuos"""
    # Ajustar el modelo ANOVA
    model = ols('Salario ~ Genero', data=dataframe).fit()

    # Obtener los residuos
    residuos = model.resid

    return residuos

def shapiro_wilk(dataframe):
    """Test de Shapiro-Wilk a partir de los residuos"""
    #calculo los residuos
    residuos = calc_residuos(dataframe)

    statistic, p_value = shapiro(residuos)

    # Gráfico de probabilidad normal (Q-Q plot)
    plt.figure(figsize=(8, 4))

    # Q-Q plot para comparar con la distribución normal teórica
    probplot(residuos, dist="norm", plot=plt)
    plt.title("Q-Q Plot de los residuos")
    plt.xlabel("Cuantiles teóricos")
    plt.ylabel("Cuantiles de la muestra")

    # Muestra el gráfico
    plt.show()

    # Se devuelve el p-valor
    return p_value
