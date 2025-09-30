from . import calculations
from . import visualization

class BohrAtom:
    """
    A class to model a hydrogen-like atom based on Bohr's model.

    This class serves as the main interface for the library. It holds the
    physical state of the atom (its atomic number, Z) and provides methods
    to perform calculations and generate visualizations by calling the
    appropriate backend functions.
    """
    def __init__(self, Z: int = 1):
        """
        Initializes the BohrAtom with a given atomic number (Z) and
        defines the required physical constants.

        Args:
            Z (int): The atomic number (number of protons). Defaults to 1.
        """
        if not isinstance(Z, int) or Z < 1:
            raise ValueError("Atomic number Z must be a positive integer.")
        self.Z = Z

        # --- Physical Constants (CODATA 2018 values) ---
        self.m_e = 9.1093837015e-31       # Electron mass (kg)
        self.e = 1.602176634e-19          # Elementary charge (C)
        self.h = 6.62607015e-34           # Planck constant (J*s)
        self.epsilon_0 = 8.8541878128e-12  # Vacuum permittivity (F/m)
        self.c = 299792458                # Speed of light (m/s)
        self.a0 = 5.29177210903e-11        # Bohr radius (m)

        # --- Derived Constants ---
        # Rydberg constant for an infinitely heavy nucleus (m⁻¹)
        self.R = (self.m_e * self.e**4) / (8 * self.epsilon_0**2 * self.h**3 * self.c)

    # --- Calculation Methods ---
    def calculate_energy_level(self, n: int, unit: str = 'eV') -> float:
        """
        Calculates the energy of an electron in a given quantum level 'n'.
        Wrapper for calculations.calculate_energy_level.
        """
        return calculations.calculate_energy_level(self, n, unit)

    def calculate_orbit_radius(self, n: int) -> float:
        """
        Calculates the radius of the orbit for a given quantum level 'n'.
        Wrapper for calculations.calculate_orbit_radius.
        """
        return calculations.calculate_orbit_radius(self, n)

    def calculate_transition(self, n_initial: int, n_final: int) -> dict:
        """
        Calculates properties of a photon from an electronic transition.
        Wrapper for calculations.calculate_transition.
        """
        return calculations.calculate_transition(self, n_initial, n_final)

    # --- Visualization Methods ---
    def plot_bohr_atom(self, n: int, mode: str = 'scaled'):
        """
        Plots a schematic representation of the Bohr atom.
        Wrapper for visualization.plot_bohr_atom.

        Args:
            n (int): The principal quantum number of the outermost electron.
            mode (str): 'scaled' for physical accuracy or 'schematic' for
                        illustrative clarity.
        """
        visualization.plot_bohr_atom(self, n, mode=mode)

    def plot_energy_transition(self, n_initial: int, n_final: int):
        """
        Plots an energy level diagram for a specific transition.
        Wrapper for visualization.plot_energy_transition.
        """
        visualization.plot_energy_transition(self, n_initial, n_final)
