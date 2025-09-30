def calculate_energy_level(atom, n: int, unit: str = 'eV') -> float:
    """
    Calculates the energy of an electron in a given quantum level 'n'
    using the Rydberg formula.

    Args:
        atom: An instance of the BohrAtom class.
        n (int): The principal quantum number (n > 0).
        unit (str): The desired unit for the output energy ('eV' or 'J').

    Returns:
        float: The energy of the level in the specified unit.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Principal quantum number n must be a positive integer.")

    # Rigorous formula using the Rydberg constant defined in the atom object
    # E_n = -R * h * c * (Z^2 / n^2)
    energy_joules = -atom.R * atom.h * atom.c * (atom.Z**2 / n**2)

    if unit.lower() == 'ev':
        return energy_joules / atom.e
    elif unit.lower() == 'j':
        return energy_joules
    else:
        raise ValueError("Invalid unit. Please choose 'eV' or 'J'.")


def calculate_orbit_radius(atom, n: int) -> float:
    """
    Calculates the radius of the orbit for a given quantum level 'n'.

    Args:
        atom: An instance of the BohrAtom class.
        n (int): The principal quantum number (n > 0).

    Returns:
        float: The radius of the orbit in meters.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Principal quantum number n must be a positive integer.")

    # Formula: r_n = (n^2 / Z) * a0
    return (n**2 / atom.Z) * atom.a0


def calculate_transition(atom, n_initial: int, n_final: int) -> dict:
    """
    Calculates the properties of a photon emitted or absorbed during an
    electronic transition using the Rydberg formula for wavelength.

    Args:
        atom: An instance of the BohrAtom class.
        n_initial (int): The initial principal quantum number (must be > 0).
        n_final (int): The final principal quantum number (must be > 0).

    Returns:
        dict: A dictionary containing the photon's properties (wavelength,
              frequency, energy, and transition type), or None if no
              transition occurs.
    """
    if not (isinstance(n_initial, int) and n_initial > 0 and
            isinstance(n_final, int) and n_final > 0):
        raise ValueError("Quantum numbers n_initial and n_final must be positive integers.")

    if n_initial == n_final:
        return None

    # Rydberg formula for the inverse wavelength: 1/λ = R * Z^2 * |1/n_f^2 - 1/n_i^2|
    term = abs((1 / n_final**2) - (1 / n_initial**2))
    inv_wavelength = atom.R * (atom.Z**2) * term

    if inv_wavelength == 0: # Should not happen with valid n
        return None

    wavelength_m = 1 / inv_wavelength
    frequency_hz = atom.c / wavelength_m
    energy_j = atom.h * frequency_hz

    return {
        "wavelength_nm": wavelength_m * 1e9,
        "frequency_Hz": frequency_hz,
        "energy_eV": energy_j / atom.e,
        "type": "Emission" if n_initial > n_final else "Absorption"
    }
