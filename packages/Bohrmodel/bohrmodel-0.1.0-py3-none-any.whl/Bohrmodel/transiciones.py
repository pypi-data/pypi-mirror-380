"""
Módulo: transiciones
Cálculo de transiciones electrónicas en el modelo de Bohr.
"""

from bohrmodel.energia import energia_n

# Constantes físicas
h = 6.626e-34  # J·s
eV_to_J = 1.602e-19  # conversión
c = 3.0e8  # m/s

def transicion(n_inicial: int, n_final: int, Z: int = 1) -> dict:
    """
    Calcula los parámetros de una transición entre dos niveles.

    Parámetros
    ----------
    n_inicial : int
        Nivel inicial (n > n_final para emisión).
    n_final : int
        Nivel final (n >= 1).
    Z : int
        Número atómico.

    Retorna
    -------
    dict
        {"deltaE_eV", "deltaE_J", "frecuencia", "longitud_onda"}
    """
    if n_inicial <= n_final:
        raise ValueError("La transición debe ir de un nivel mayor a uno menor.")

    E1 = energia_n(n_inicial, Z)
    E2 = energia_n(n_final, Z)
    deltaE_eV = E2 - E1
    deltaE_J = deltaE_eV * eV_to_J

    frecuencia = deltaE_J / h
    longitud_onda = c / frecuencia

    return {
        "deltaE_eV": deltaE_eV,
        "deltaE_J": deltaE_J,
        "frecuencia": frecuencia,
        "longitud_onda": longitud_onda
    }