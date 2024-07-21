"""Módulo para calcular y graficar varianzas"""

from matplotlib import pyplot as plt
from scipy import stats
import numpy as np
import seaborn as sns


def levene_test(gr1, gr2, gr3):
    """Test de Levene"""
    resultados = stats.levene(gr1, gr2, gr3, center='mean')
    # Devolvemos el p-valor
    return resultados[1]


def density_plot(muestra):
    """Gráfico de densidades con ajuste normal"""

    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7, 3.5))
    
    for category in muestra['Genero'].unique():
        subset = muestra[muestra['Genero'] == category]
        
        kde_plot = sns.kdeplot(
            x       = 'Salario',
            data    = subset,
            label   = f'{category} - Densidad',
            fill    = False,
            common_norm=False,
            ax      = ax
        )
        
        # Ajuste de la distribución normal
        mu, std = stats.norm.fit(subset['Salario'])
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = stats.norm.pdf(x, mu, std)
        line_color = kde_plot.get_lines()[-1].get_c()
        plt.plot(x, p, label=f'{category} - Ajuste Normal', linestyle='dotted',linewidth=2, color=line_color)

    ax.set_title('Distribución de salario por género con Ajuste Normal')
    ax.set_xlabel('Salario')
    ax.set_ylabel('Densidad')
    ax.legend()

    plt.show()

def box_plot(muestra):
    """Gráfico de caja"""
    fig,ax = plt.subplots(nrows=1, ncols=1, figsize=(7, 3.5))
    sns.boxplot(
        x       = 'Salario',
        y       = 'Genero',
        data    = muestra,
        hue     = 'Genero',
        palette = 'tab10',
        legend  = False,
        ax      = ax
    )
    ax.set_title('Distribución de salario por género')
    ax.set_xlabel('Salario')
    ax.set_ylabel('Género')

    plt.show()
    