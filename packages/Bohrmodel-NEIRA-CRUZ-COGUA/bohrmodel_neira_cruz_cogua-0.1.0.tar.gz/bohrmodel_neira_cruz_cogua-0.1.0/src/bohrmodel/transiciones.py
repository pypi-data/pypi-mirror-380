from bohrmodel.energia import energia_n

# Constantes físicas (valores más exactos)
h = 6.62607015e-34  # J·s
eV_to_J = 1.602176634e-19  # conversión
c = 299792458  # m/s

def transicion(n_inicial: int, n_final: int, Z: int = 1) -> dict:
    """
    Calcula parámetros de una transición (emisión) entre dos niveles:
    n_inicial > n_final
    """
    if n_inicial <= n_final:
        raise ValueError("La transición debe ir de un nivel mayor a uno menor (emisión).")

    E1 = energia_n(n_inicial, Z)  # eV (nivel inicial, menos negativo)
    E2 = energia_n(n_final, Z)    # eV (nivel final, más negativo)
    deltaE_eV = E1 - E2           # energía liberada (positiva) en eV
    deltaE_J = deltaE_eV * eV_to_J

    frecuencia = deltaE_J / h
    longitud_onda = c / frecuencia if frecuencia != 0 else float("inf")

    return {
        "deltaE_eV": deltaE_eV,
        "deltaE_J": deltaE_J,
        "frecuencia": frecuencia,
        "longitud_onda": longitud_onda
    }
