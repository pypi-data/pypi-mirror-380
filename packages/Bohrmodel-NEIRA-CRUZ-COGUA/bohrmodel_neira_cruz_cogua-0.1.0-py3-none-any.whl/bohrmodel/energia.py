"""
Módulo: energia
Cálculo de niveles de energía en el modelo de Bohr.
"""

def energia_n(n: int, Z: int = 1) -> float:
    """
    Calcula la energía de un electrón en el nivel n de un átomo hidrogenoide.

    Parámetros
    ----------
    n : int
        Número cuántico principal (n >= 1).
    Z : int
        Número atómico (por defecto 1 para hidrógeno).

    Retorna
    -------
    float
        Energía en electronvoltios (eV).
    """
    if n < 1:
        raise ValueError("El número cuántico principal n debe ser >= 1")
    energia = -13.6 * (Z ** 2) / (n ** 2)  # eV
    return energia
