"""
Módulo: graficos
Representación gráfica de niveles de energía y órbitas.
"""

import matplotlib.pyplot as plt
from bohrmodel.energia import energia_n
from bohrmodel.radios import radio_n
import numpy as np

def plot_niveles(max_n: int, Z: int = 1):
    """
    Grafica los niveles de energía hasta un n máximo.
    """
    niveles = [energia_n(n, Z) for n in range(1, max_n + 1)]
    for i, E in enumerate(niveles, 1):
        plt.hlines(E, xmin=0, xmax=1, label=f"n={i}")
    plt.ylabel("Energía (eV)")
    plt.title(f"Niveles de energía (Z={Z})")
    plt.legend()
    plt.show()

def plot_orbitas(max_n: int, Z: int = 1):
    """
    Dibuja las órbitas circulares en 2D.
    """
    fig, ax = plt.subplots()
    for n in range(1, max_n + 1):
        r = radio_n(n, Z)
        circ = plt.Circle((0, 0), r, fill=False, label=f"n={n}")
        ax.add_patch(circ)
    ax.set_aspect("equal", "box")
    ax.set_xlim(-radio_n(max_n, Z) * 1.2, radio_n(max_n, Z) * 1.2)
    ax.set_ylim(-radio_n(max_n, Z) * 1.2, radio_n(max_n, Z) * 1.2)
    plt.title(f"Órbitas electrónicas (Z={Z})")
    plt.legend()
    plt.show()