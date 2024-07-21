"""Método main"""

from scipy import stats 
import numpy as np
import pandas as pd
import variance
import normality

# importamos el dataset desde el exel
dataset = pd.read_excel(r"dataset_empleados.xlsx")

# Obtenemos los datos muestrales (la columna que querramos, en este caso salarios)
muestra = np.array(dataset['Salario'])
muestra_fem = dataset.loc[dataset['Genero'] == 'Femenino', 'Salario']
muestra_masc = dataset.loc[dataset['Genero'] == 'Masculino', 'Salario']
muestra_noB = dataset.loc[dataset['Genero'] == 'No Binario', 'Salario']

#Supuesto N° 1 la distribucion de los residuos es normal
print("")
print(f"Valor-p de la prueba de Shapiro-Wilk: {normality.shapiro_wilk(dataset)}")


#Supuesto N° 2: las muestras K son independientes.
#Se asume que las observaciones fueron tomadas aleatoriamente y que los grupos (niveles del factor) son independientes entre sí.


#Supuesto N° 3: las poblaciones tienen todas igual varianza (homocedasticidad)
print("")
print(f"Valor-p de la prueba de Levene: {variance.levene_test(muestra_fem, muestra_masc, muestra_noB)}")
variance.density_plot(dataset)
variance.box_plot(dataset)

# Se calcula ANOVA
print("")
stats.f_oneway(muestra_fem, muestra_masc, muestra_noB)
print(f"Valor-p de ANOVA: {stats.f_oneway(muestra_fem, muestra_masc, muestra_noB)[1]}")
