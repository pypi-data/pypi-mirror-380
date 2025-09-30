# src/bohrmodel/atom.py

from bohrmodel.energia import energia_n
from bohrmodel.radios import radio_n
from bohrmodel.transiciones import transicion
from bohrmodel.graficos import plot_niveles, plot_orbitas


class BohrAtom:
    """Clase principal del modelo de Bohr."""
    def __init__(self, Z: int = 1):
        self.Z = Z

    def energy_level_ev(self, n: int) -> float:
        return energia_n(n, self.Z)

    def orbit_radius(self, n: int) -> float:
        return radio_n(n, self.Z)

    def transition(self, n1: int, n2: int):
        return transicion(n1, n2, self.Z)

    def plot_energy_levels(self, max_n: int = 5):
        return plot_niveles(max_n, self.Z)

    def plot_orbits(self, max_n: int = 3):
        return plot_orbitas(max_n, self.Z)


if __name__ == "__main__":
    print("=== MODELO DE BOHR PARA ÁTOMOS HIDROGENOIDES ===")
    Z = int(input("Ingrese el número atómico Z (1=Hidrógeno): ") or 1)
    atom = BohrAtom(Z=Z)

    while True:
        print("\nSeleccione una opción:")
        print("1. Calcular energía de un nivel (en eV)")
        print("2. Calcular radio de una órbita")
        print("3. Calcular transición electrónica (energía, frecuencia, longitud de onda)")
        print("4. Graficar niveles de energía")
        print("5. Graficar órbitas electrónicas")
        print("0. Salir")

        choice = input("Opción: ")

        if choice == "1":
            n = int(input("Ingrese nivel n: "))
            print(f"Energía en n={n}: {atom.energy_level_ev(n):.4f} eV")

        elif choice == "2":
            n = int(input("Ingrese nivel n: "))
            print(f"Radio en n={n}: {atom.orbit_radius(n):.4e} m")

        elif choice == "3":
            n1 = int(input("Nivel inicial n1: "))
            n2 = int(input("Nivel final n2: "))
            datos = atom.transition(n1, n2)
            print(f"ΔE = {datos['deltaE_eV']:.6f} eV")
            print(f"Energía: {datos['deltaE_J']:.4e} J")
            print(f"Frecuencia: {datos['frecuencia']:.4e} Hz")
            print(f"Longitud de onda: {datos['longitud_onda']:.4e} m")

        elif choice == "4":
            max_n = int(input("Número máximo de niveles a graficar: ") or 5)
            atom.plot_energy_levels(max_n)

        elif choice == "5":
            max_n = int(input("Número máximo de órbitas a graficar: ") or 3)
            atom.plot_orbits(max_n)

        elif choice == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")
