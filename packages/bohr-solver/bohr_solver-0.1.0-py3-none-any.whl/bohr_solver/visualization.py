import matplotlib.pyplot as plt
import numpy as np
from . import calculations

def plot_bohr_atom(atom, n: int, mode: str = 'scaled'):
    """
    Plots a schematic Bohr-type atom with a nucleus and electron orbits.

    Args:
        atom: An instance of the BohrAtom class.
        n (int): The principal quantum number of the outermost electron.
        mode (str): The plotting mode. Can be 'scaled' for physically
                    accurate radii or 'schematic' for evenly spaced orbits.
    """
    if not (isinstance(n, int) and n > 0):
        raise ValueError("The quantum number n must be a positive integer.")
    if mode not in ['scaled', 'schematic']:
        raise ValueError("Mode must be either 'scaled' or 'schematic'.")

    Z = atom.Z
    fig, ax = plt.subplots(figsize=(8, 8))

    # --- Draw Nucleus ---
    proton_locations = np.linspace(0, 2 * np.pi, Z, endpoint=False)
    # Use the first Bohr radius as a reference for nucleus size
    first_radius = calculations.calculate_orbit_radius(atom, 1)
    nucleus_radius = 0.1 * first_radius
    for i in range(Z):
        x = nucleus_radius * np.cos(proton_locations[i])
        y = nucleus_radius * np.sin(proton_locations[i])
        ax.plot(x, y, 'o', color='red', markersize=12, markeredgecolor='black', markeredgewidth=1.5)
        ax.text(x, y, "+", color='white', fontsize=8, ha='center', va='center', fontweight='bold')

    # --- Determine Radii based on Mode ---
    if mode == 'scaled':
        # Physically accurate radii (r ∝ n^2)
        radii = [calculations.calculate_orbit_radius(atom, i) for i in range(1, n + 1)]
        title = f"Bohr Model (Z={Z}, n={n}) - Scaled Radii"
    else: # mode == 'schematic'
        # Illustrative, evenly spaced radii (r ∝ n)
        last_radius = calculations.calculate_orbit_radius(atom, n)
        # Create n evenly spaced points from the first radius to the last
        radii = np.linspace(first_radius, last_radius, n)
        title = f"Bohr Model (Z={Z}, n={n}) - Schematic (Not to Scale)"

    # --- Draw Orbits and Electron ---
    for r in radii:
        circle = plt.Circle((0, 0), r, color='gray', fill=False, linestyle='--')
        ax.add_artist(circle)

    electron_radius = radii[-1]
    ax.plot(electron_radius, 0, 'o', color='blue', markersize=10, markeredgecolor='black', markeredgewidth=1.5)
    ax.text(electron_radius, 0, "-", color='white', fontsize=10, ha='center', va='center', fontweight='bold')

    # --- Final Plot Configuration ---
    max_radius = radii[-1]
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-max_radius * 1.2, max_radius * 1.2)
    ax.set_ylim(-max_radius * 1.2, max_radius * 1.2)
    ax.set_xlabel("x (meters)")
    ax.set_ylabel("y (meters)")
    ax.set_title(title)
    ax.grid(True, linestyle=':')
    plt.show()

def plot_energy_transition(atom, n_initial: int, n_final: int):
    n_max = max(n_initial, n_final, 5)
    levels = [calculations.calculate_energy_level(atom, n, unit='eV') for n in range(1, n_max + 1)]
    fig, ax = plt.subplots(figsize=(5, 7))
    for n, energy_ev in enumerate(levels, start=1):
        ax.hlines(energy_ev, xmin=0, xmax=1, color='b', alpha=0.7)
        ax.text(1.05, energy_ev, f"n={n}", va='center', ha='left')
    E_initial = calculations.calculate_energy_level(atom, n_initial, unit='eV')
    E_final = calculations.calculate_energy_level(atom, n_final, unit='eV')
    transition_energy = abs(E_final - E_initial)
    color = 'red' if n_initial > n_final else 'green'
    ax.annotate("", xy=(0.5, E_final), xytext=(0.5, E_initial),
                arrowprops=dict(facecolor=color, shrink=0.05, width=2, headwidth=8))
    ax.text(0.45, (E_initial + E_final) / 2, f"ΔE = {transition_energy:.2f} eV",
            color=color, va='center', ha='right')
    ax.set_xlim(0, 1.5)
    ax.set_xticks([])
    ax.set_ylabel('Energy (eV)')
    ax.set_title(f'Electronic Transition (Z={atom.Z})')
    plt.show()
