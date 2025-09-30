

# BohrSolver

**BohrSolver** is a Python library to model hydrogen-like atoms using the Bohr model. It allows you to calculate energy levels, orbit radii, electronic transitions, and generate visualizations for both individual energy levels and electronic transitions.

The library is designed to be intuitive, providing a class-based interface (`BohrAtom`) that wraps all calculations and plotting functionalities.

---

## Features

* Compute energy levels of electrons in hydrogen-like atoms.
* Calculate the radius of electron orbits for given quantum numbers.
* Calculate photon properties (energy, wavelength, frequency) during electronic transitions.
* Generate schematic or physically scaled plots of Bohr atoms.
* Visualize electronic transitions with annotated energy differences.

---

## Installation

You can install the library locally by cloning the repository and installing dependencies:

```bash
git clone <your-repo-url>
cd BohrSolver
pip install -e .
```

Dependencies:

* Python >= 3.8
* `numpy`
* `matplotlib`

---

## Usage

```python
from bohr_solver import BohrAtom

# Create a Bohr atom instance for Hydrogen (Z=1)
atom = BohrAtom(Z=1)

# Calculate energy levels
energy_n1 = atom.calculate_energy_level(1)   # default in eV
energy_n2 = atom.calculate_energy_level(2, unit='J')

# Calculate orbit radius
r_n1 = atom.calculate_orbit_radius(1)
r_n2 = atom.calculate_orbit_radius(2)

# Calculate transition properties
transition = atom.calculate_transition(n_initial=2, n_final=1)
print(transition)
# Output: {'wavelength_nm': ..., 'frequency_Hz': ..., 'energy_eV': ..., 'type': 'Emission'}

# Plot Bohr atom with scaled orbits
atom.plot_bohr_atom(n=3, mode='scaled')

# Plot electronic transition
atom.plot_energy_transition(n_initial=2, n_final=1)
```

---

## Classes & Methods

### `BohrAtom(Z: int = 1)`

Main class representing a hydrogen-like atom.

#### Calculation Methods

* `calculate_energy_level(n: int, unit: str = 'eV') -> float`
* `calculate_orbit_radius(n: int) -> float`
* `calculate_transition(n_initial: int, n_final: int) -> dict`

#### Visualization Methods

* `plot_bohr_atom(n: int, mode: str = 'scaled')`
* `plot_energy_transition(n_initial: int, n_final: int)`

---

## Examples

### 1. Energy Levels

```python
atom = BohrAtom(Z=2)  # Helium ion
for n in range(1, 4):
    print(f"n={n}: {atom.calculate_energy_level(n)} eV")
```

### 2. Orbit Radii

```python
radii = [atom.calculate_orbit_radius(n) for n in range(1, 4)]
print(radii)
```

### 3. Electronic Transition

```python
transition = atom.calculate_transition(3, 1)
print(f"Transition energy: {transition['energy_eV']} eV")
```

### 4. Visualization

```python
atom.plot_bohr_atom(n=3, mode='schematic')
atom.plot_energy_transition(3, 1)
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

