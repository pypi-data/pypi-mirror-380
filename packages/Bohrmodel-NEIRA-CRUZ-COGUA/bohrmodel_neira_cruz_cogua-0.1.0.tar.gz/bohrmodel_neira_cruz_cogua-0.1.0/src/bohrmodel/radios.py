

"""
Módulo: radios
Cálculo de radios de órbita en el modelo de Bohr.
"""

# Radio de Bohr en metros
a0 = 5.29e-11  

def radio_n(n: int, Z: int = 1) -> float:
    """
    Calcula el radio de la órbita en el nivel n.

    Parámetros
    ----------
    n : int
        Número cuántico principal (n >= 1).
    Z : int
        Número atómico (por defecto 1 para hidrógeno).

    Retorna
    -------
    float
        Radio en metros (m).
    """
    if n < 1:
        raise ValueError("El número cuántico principal n debe ser >= 1")
    r = (n ** 2) * a0 / Z
    return r
  