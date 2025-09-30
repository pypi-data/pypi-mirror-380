# Contenido para src/Bohrmodel/__init__.py

# Definición de la versión para el paquete.
__version__ = "0.1.0"

# Importa la clase principal (BohrAtom) desde atom.py.
# Esto permite que los usuarios hagan: from Bohrmodel import BohrAtom
from .atom import BohrAtom 

# Importa las funciones individuales desde los submódulos.
# Esto permite que los usuarios hagan: from Bohrmodel import radio_n
from .radios import radio_n
from .energia import energia_n
from .transiciones import transicion
from .graficos import plot_niveles, plot_orbitas 

# Define los nombres que se importarán cuando un usuario use 'from Bohrmodel import *'.
__all__ = [
    "__version__",
    "BohrAtom",
    "radio_n",
    "energia_n",
    "transicion",
    "plot_niveles", 
    "plot_orbitas"
]