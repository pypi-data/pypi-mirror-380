"""
Constraint-aware MD+Relaxation runner for GA simulations (ASE backend).

This module adds *the same constraint system you use for mutations* to your
simulation pipeline. You can pass lists of the very same callables
(e.g., component_greater_than('z', 10.), label_in({'Ni','Fe'}), etc.) and choose
how to apply them during MD/relaxation: freeze selected atoms entirely (FixAtoms),
or freeze only chosen Cartesian components (FixCartesian). The implementation is
non-intrusive and keeps your existing schedules (linear_interpolation, etc.).

Key features
------------
- `_StructAdapter` bridges your constraint predicates to raw arrays.
- `_select_indices_by_constraints(...)` reuses your predicate logic.
- `_build_ase_constraints(...)` creates ASE constraints (FixAtoms/FixCartesian)
  from the selected indices and components.
- `ase_calculator(...)` and its returned `run(...)` **both** accept a list of
  already-built predicate callables (`(idx, structure) -> bool`). The set used
  at runtime is the concatenation of factory-level and run-level lists.

Python compatibility
--------------------
- Uses `typing.Union[...]` instead of the `|` syntax to support Python < 3.10.
- No dependency on `from __future__ import annotations`.
"""

from typing import Union, Sequence, Optional, Callable, Tuple, Any
import numpy as np
from .F_vib import corrected_vdos_and_F_from_velocities as _vib_pipeline
from .F_vib import _VibSampler, _save_vib_outputs_to_folder

# =============================================================================
# Shared utilities
# =============================================================================
INTERPOLATION_PREC = 256


def linear_interpolation(data, N):
    """
    Generates N linearly interpolated points over M input points.

    Parameters
    ----------
    data : int, float, list, tuple, or numpy.ndarray
        Input data specifying M control points. If scalar or of length 1,
        returns a constant array of length N.
    N : int
        Number of points to generate. Must be a positive integer and at least
        as large as the number of control points when M > 1.

    Returns
    -------
    numpy.ndarray
        Array of N linearly interpolated points.
    """
    # Validate N
    if not isinstance(N, int) or N <= 0:
        raise ValueError("N must be a positive integer.")

    # Handle scalar input
    if isinstance(data, (int, float)):
        return np.full(N, float(data))

    # Convert sequence input to numpy array
    try:
        arr = np.asarray(data, dtype=float).flatten()
    except Exception:
        raise ValueError("Data must be an int, float, list, tuple, or numpy.ndarray of numeric values.")

    M = arr.size
    if M == 0:
        raise ValueError("Input data sequence must contain at least one element.")
    if M == 1:
        return np.full(N, arr[0])

    # Ensure N >= M for piecewise interpolation
    if N < M:
        raise ValueError(f"N ({N}) must be at least the number of input points M ({M}).")

    # Define original and target sample positions
    xp = np.arange(M)
    xi = np.linspace(0, M - 1, N)

    # Perform piecewise linear interpolation
    return np.interp(xi, xp, arr)

# =============================================================================
# Constraint bridge utilities
# =============================================================================
class _APMAdapter:
    """Minimal adapter exposing the attributes your predicates expect."""

    def __init__(self, symbols, positions, cell, atomic_constraints=None):
        self.atomPositions  = np.asarray(positions, float)
        self.atomLabelsList = np.asarray(symbols, dtype=object)

        # If cell is missing/degenerate, use I3 for predicate safety
        _cell = np.asarray(cell, float) if cell is not None else None
        if _cell is None or _cell.shape != (3, 3) or not np.isfinite(_cell).all() or abs(np.linalg.det(_cell)) < 1e-9:
            _cell = np.eye(3, dtype=float)
        self.latticeVectors = _cell

        self.atomicConstraints = (
            np.asarray(atomic_constraints, bool) if atomic_constraints is not None else None
        )
        self.atomCount = len(self.atomPositions)


class _StructAdapter:
    def __init__(self, symbols, positions, cell, atomic_constraints=None):
        self.AtomPositionManager = _APMAdapter(symbols, positions, cell, atomic_constraints)


def _evaluate(idx: int, structure: _StructAdapter, constraints: Sequence[Callable], logic: str = "all") -> bool:
    if not constraints:
        return True
    if logic == "all":
        return all(not c(idx, structure) for c in constraints)
    elif logic == "any":
        return any(not c(idx, structure) for c in constraints)
    else:
        raise ValueError("logic must be 'all' or 'any'")


def _select_indices_by_constraints(
    symbols,
    positions,
    cell,
    fixed: Optional[Sequence[bool]],
    constraints: Sequence[Callable],
    logic: str = "all",
) -> np.ndarray:
    N = len(symbols)
    adapter = _StructAdapter(symbols=symbols, positions=positions, cell=cell, atomic_constraints=fixed)
    sel = [i for i in range(N) if _evaluate(i, adapter, constraints, logic=logic)]
    return np.asarray(sel, dtype=int)


def _normalize_components(components: Optional[Sequence[Union[int, str]]]) -> Optional[Sequence[int]]:
    if components is None:
        return None
    comp_map = {"x": 0, "y": 1, "z": 2}
    out = []
    for c in components:
        if isinstance(c, str):
            out.append(comp_map[c.lower()])
        else:
            out.append(int(c))
    if any(c not in (0, 1, 2) for c in out):
        raise ValueError("freeze_components must be a subset of {0,1,2,'x','y','z'}")
    return out


def _build_ase_constraints(atoms, selected: np.ndarray, action: str, freeze_components: Optional[Sequence[int]]):
    """
    Returns a list of ASE constraints implementing the requested action.
    - action == 'freeze'     : freeze the *selected* DOFs
    - action == 'move_only'  : freeze the complement (non-selected) DOFs
    If freeze_components is None -> FixAtoms; else -> FixCartesian(mask).
    """
    from ase.constraints import FixAtoms, FixCartesian

    N = len(atoms)
    selected = np.unique(selected)
    if action not in ("freeze", "move_only"):
        raise ValueError("constraint_action must be 'freeze' or 'move_only'")

    if freeze_components is None:
        if action == "freeze":
            idx = selected
        else:
            mask = np.ones(N, dtype=bool)
            mask[selected] = False
            idx = np.where(mask)[0]

        return FixAtoms(indices=list(idx))
    else:
        comps = list(freeze_components)
        mask = np.zeros((N, 3), dtype=bool)
        if action == "freeze":
            mask[np.ix_(selected, comps)] = True
        else:
            comp = np.ones(N, dtype=bool)
            comp[selected] = False
            idx = np.where(comp)[0]
            mask[np.ix_(idx, comps)] = True
        return FixCartesian(mask=mask)

# =============================================================================
# Calculator factory (ASE backend) with constraint-aware run() with optimized vibrational correction
# =============================================================================
def _to_pred_list(preds: Optional[Sequence[Callable]]) -> list:
    """Normalize predicates to a plain Python list; robust to numpy arrays/single callables."""
    if preds is None:
        return []
    if callable(preds):
        return [preds]
    try:
        return list(preds)
    except TypeError:
        return [preds]

def ase_calculator(
    calculator: object = None,
    # --- MD / relaxation controls ---
    nvt_steps: Union[int, Sequence[float], None] = None,
    fmax: Union[float, Sequence[float], None] = 0.05,
    steps_max: int = 100,
    hydrostatic_strain: bool = False,
    constant_volume: bool = True,
    device: str = 'cuda',
    default_dtype: str = 'float32',
    optimizer: str = 'FIRE',
    # --- temperature schedules ---
    T: Union[float, Sequence[float]] = 300.0,
    T_ramp: bool = False,
    # --- timestep (fs) for the MD integrator ---
    md_timestep_fs: float = 1.0,

    # --- vibrational correction controls ---
    vib_correction: bool = False,
    vib_store_interval: int = 1,     # record every k MD steps -> effective dt = k * md_timestep_fs
    vib_min_samples: int = 200,      # need at least this many stored samples to compute spectrum
    remove_com_drift: bool = False,   # remove COM velocity before storing
    mass_weighted_com: bool = True,  # COM uses masses if True; else arithmetic mean
    vacf_window: str = "hann",

    # --- constraint controls ---
    constraint_logic: str = "all",
    constraint_action: str = "freeze",
    freeze_components: Optional[Sequence[Union[int, str]]] = None,
    constraints: Optional[Sequence[Callable]] = None,
) -> Callable[..., Tuple[np.ndarray, np.ndarray, Optional[np.ndarray], float, float, Optional[dict]]]:
    """
    Returns a `run(...)` callable that performs:
        [optional] NVT MD with downsampled velocity capture
        [optional] Vibrational free energy from VACF/VDOS
        [optional] Relaxation to `fmax`
    honoring your constraint predicates.

    The returned `run(...)` signature is:
        run(symbols, positions, cell, fixed=None, sampling_temperature=0.0,
            steps_max_=steps_max, output_path='MD_out.xyz', constraints=None)

    It returns (positions, symbols, cell, E_pot, corrections).
    """
    import ase.io
    from ase import Atoms, units
    from ase.md.langevin import Langevin
    from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
    from ase.optimize import BFGS, FIRE
    from ase.filters import FrechetCellFilter
    from ase.units import fs
    import os, time

    # Precompute schedules
    nvt_steps_sched = linear_interpolation(nvt_steps, INTERPOLATION_PREC) if nvt_steps is not None else None
    T_sched = linear_interpolation(T, INTERPOLATION_PREC) if T is not None else None
    fmax_sched = linear_interpolation(fmax, INTERPOLATION_PREC) if fmax is not None else None

    freeze_components_norm = _normalize_components(freeze_components)
    factory_constraints = _to_pred_list(constraints)

    def run(
        symbols: Union[np.ndarray, Sequence[str]],
        positions: np.ndarray,
        cell: np.ndarray,
        fixed: np.ndarray = None,
        sampling_temperature: float = 0.0,
        steps_max_: int = steps_max,
        output_path: str = 'MD_out.xyz',
        constraints: Optional[Sequence[Callable]] = None,
    ) -> Tuple[np.ndarray, np.ndarray, Optional[np.ndarray], float, float, Optional[dict]]:
        """Executes MD + relaxation for one structure, honoring constraints."""
        # Validate basic inputs
        if not isinstance(symbols, (list, np.ndarray)):
            raise TypeError("`symbols` must be a list or numpy array of strings")
        positions_arr = np.asarray(positions, dtype=float)
        if positions_arr.ndim != 2 or positions_arr.shape[1] != 3:
            raise ValueError("`positions` must be an array of shape (N, 3)")
        cell_arr = np.asarray(cell, dtype=float)
        #if cell_arr.shape != (3, 3):
        #    raise ValueError("`cell` must be a 3×3 array")
        if not isinstance(sampling_temperature, (int, float)):
            raise TypeError("`sampling_temperature` must be a number")
        if not isinstance(output_path, str):
            raise TypeError("`output_path` must be a string path")

        # Ensure output dir
        out_dir = os.path.dirname(output_path) or '.'
        os.makedirs(out_dir, exist_ok=True)

        # ------------------------ Build Atoms ------------------------
        # Build Atoms object and attach calculator
        # --- arrays ---
        symbols_arr   = np.asarray(symbols, dtype=object)
        positions_arr = np.asarray(positions, dtype=float)

        # --- validate / classify cell ---
        cell_is_valid = False
        cell_arr = None
        if cell is not None:
            try:
                cell_arr = np.asarray(cell, dtype=float)
                cell_is_valid = (
                    cell_arr.shape == (3, 3)
                    and np.isfinite(cell_arr).all()
                    and abs(np.linalg.det(cell_arr)) > 1e-9
                )
            except Exception:
                cell_is_valid = False
                cell_arr = None

        # PBC only if user wants a real cell
        pbc_flag = bool(cell_is_valid)

        # --- make Atoms ---
        atoms = Atoms(symbols=symbols_arr, positions=positions_arr,
                      cell=(cell_arr if pbc_flag else None), pbc=pbc_flag)
        atoms.calc = calculator

        # Split into callable predicates and preselected indices/masks
        N_atoms = positions_arr.shape[0]

        # ------------------------ Constraints ------------------------
        # Combine factory- and run-level predicates
        combined_constraints = list(factory_constraints)
        combined_constraints.extend(_to_pred_list(constraints))

        # Adapter cell for predicate evaluation (I3 if non-periodic)
        adapter_cell = cell_arr if pbc_flag else np.eye(3, dtype=float)

        if len(combined_constraints) > 0:
            selected = _select_indices_by_constraints(
                symbols_arr, positions_arr, adapter_cell, fixed, 
                combined_constraints, logic=constraint_logic
            )
        else:
            selected = np.array([], dtype=int)

        if selected.size > 0:
            atoms.set_constraint(
                _build_ase_constraints(atoms, selected, action=constraint_action, freeze_components=freeze_components_norm)
            )

        # ================================================================= # # ================================================================= #
        # ------------------------ Stage 1: NVT MD ------------------------ # ------------------------ Stage 1: NVT MD ------------------------
        # ================================================================= # # ================================================================= #
        corrections = {}
        idx_sample = int(min(max(float(sampling_temperature), 0.0)*INTERPOLATION_PREC, INTERPOLATION_PREC-1))

        if nvt_steps_sched is not None:
            # Select schedule index from "sampling_temperature" in [0,1]
            nvt_steps_act = int(np.asarray(nvt_steps_sched, dtype=float)[idx_sample])
            T_K = float(T_sched[idx_sample]) if T_sched is not None else 300.0

            if nvt_steps_act > 0:
                # Initialize velocities and set up Langevin thermostat
                MaxwellBoltzmannDistribution(atoms, temperature_K=T_K)
                dyn = Langevin(atoms=atoms,
                               timestep=md_timestep_fs * fs,
                               temperature_K=T_K,
                               friction=0.001)

                # --- Determine frozen DOFs for accurate F_vib scaling
                N = len(atoms)
                dof_frozen = 0
                if selected.size > 0:
                    if freeze_components_norm is None:
                        if constraint_action == "freeze":
                            dof_frozen = 3 * int(selected.size)
                        else:
                            dof_frozen = 3 * (N - int(selected.size))
                    else:
                        comps = len(set(freeze_components_norm))
                        if constraint_action == "freeze":
                            dof_frozen = comps * int(selected.size)
                        else:
                            dof_frozen = comps * (N - int(selected.size))
                dof_count = max(3 * N - dof_frozen, 1)

                # --- Preallocate velocity buffer (downsampled) with step-0 safety
                store_interval = max(int(vib_store_interval), 1)
                # number of calls = 1 (step 0) + ceil(nvt_steps_act / store_interval)
                n_samples_pred = 1 + (nvt_steps_act + store_interval - 1) // store_interval
                dof = len(atoms) * 3
                # Only capture if vib correction requested and enough samples expected
                capture = bool(vib_correction) and (n_samples_pred >= int(vib_min_samples))

                # --- Attach sampler
                sampler = None
                if capture:
                    sampler = _VibSampler(
                        atoms=atoms,
                        n_samples_pred=n_samples_pred,
                        store_interval=store_interval,
                        remove_com=bool(remove_com_drift),
                        mass_weighted=bool(mass_weighted_com),
                    )
                    sampler.attach(dyn)

                # Light progress printing at coarse interval
                def _printenergy(dynobj, t0):
                    a = dynobj.atoms
                    ep = a.get_potential_energy() / max(len(a), 1)
                    ek = a.get_kinetic_energy() / max(len(a), 1)
                    Tinst = ek / (1.5 * units.kB) if len(a) > 0 else 0.0
                    print(f"{time.time()-t0:.1f}s | Epot/atom={ep:.3f} eV | T={Tinst:.0f} K | t={dynobj.get_time()/units.fs:.0f} fs",
                          flush=True)
                t0 = time.time()
                dyn.attach(_printenergy, interval=max(5000//max(int(md_timestep_fs),1), 1), dynobj=dyn, t0=t0)

                # --- Run MD ---
                dyn.run(nvt_steps_act)

                # Persist last configuration if requested (best-effort)
                try:
                    out_dir = (output_path and (os.path.dirname(output_path) or '.')) or '.'
                    os.makedirs(out_dir, exist_ok=True)
                    ase.io.write(output_path, atoms, append=True)
                except Exception:
                    pass  # non-fatal

                # --- Vibrational analysis (PSD-based; **no** VACF duplication) (post-MD) --- 
                if capture:
                    vel_flat = sampler.finalize()

                    samples_used = int(vel_flat.shape[0])
                    if samples_used >= int(vib_min_samples):
                        eff_dt_fs = md_timestep_fs * store_interval
                        masses = atoms.get_masses() if remove_com_drift else None

                        res = _vib_pipeline(
                            vel_flat=vel_flat,             # COM already removed in sampler; that's fine
                            dt_fs=eff_dt_fs,
                            T_K=T_K,
                            dof_count=dof_count,
                            masses=masses,
                            remove_COM=False,              # prevent double COM removal
                            window="hann",
                            n_segments=6,                  # Welch segments (tune as needed)
                            overlap=0.5,
                            notch_bands_THz=None,          # e.g., [(1.0, 0.1)] to notch a thermostat line
                            debye_lowf_blend=True,         # True for crystalline solids; set False for liquids/amorphous
                            debye_fit_fmax_THz=1.5,
                            debye_blend_fmax_THz=1.5,
                            stats='both',
                        )
                        corrections.update( dict(res) )
                        print(res)
                        saved_files = _save_vib_outputs_to_folder(
                            corrections=corrections,
                            output_path=output_path,
                        )

        # ===================================================================== # # ================================================================= #
        # ------------------------ Stage 2: Relaxation ------------------------ # ------------------------ Stage 2: Relaxation ------------------------
        # ===================================================================== # # ================================================================= #
        if fmax_sched is not None:
            # Use same schedule index picked above (or 0 if MD not used)
            fmax_act = float(np.asarray(fmax_sched, dtype=float)[idx_sample])
            if fmax_act > 0:
                if pbc_flag and not constant_volume:
                    ecf = FrechetCellFilter(atoms, hydrostatic_strain=hydrostatic_strain,
                                            constant_volume=constant_volume, scalar_pressure=0.0)
                else:
                    ecf = None
                if optimizer.upper() == 'BFGS':
                    opt = BFGS(atoms if ecf is None else ecf, logfile=None, maxstep=0.2)
                else:
                    opt = FIRE(atoms if ecf is None else ecf, logfile=None)
                opt.run(fmax=fmax_act, steps=steps_max_)

        # ================================================================== # # ============================================================== #
        # ------------------------ Stage 3: Outputs ------------------------ # ------------------------ Stage 3: Outputs ------------------------
        # ================================================================== # # ============================================================== #        
        cell_obj = atoms.get_cell()
        pbc_flag = bool(atoms.get_pbc().any())
        has_volume = float(cell_obj.volume) > 1e-12
        cell_out = cell_obj.array if pbc_flag and has_volume else None
        E = float(atoms.get_potential_energy())
        corrections["F"] = E + corrections.get('F_vib_eV', 0)

        return (
            np.array(atoms.get_positions()),
            np.array(atoms.get_chemical_symbols()),
            np.array(cell_out),
            E,
            corrections,
        )

    return run


