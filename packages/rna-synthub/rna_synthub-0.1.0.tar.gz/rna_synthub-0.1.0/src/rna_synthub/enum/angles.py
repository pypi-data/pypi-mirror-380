import numpy as np
ANGLES = {
    "alpha": {"atoms": ["O3'", "P", "O5'", "C5'"], "index": [-1, 0, 0, 0]},
    "beta": {"atoms": ["P", "O5'", "C5'", "C4'"], "index": [0, 0, 0, 0]},
    "gamma": {"atoms": ["O5'", "C5'", "C4'", "C3'"], "index": [0, 0, 0, 0]},
    "delta": {"atoms": ["C5'", "C4'", "C3'", "O3'"], "index": [0, 0, 0, 0]},
    "epsilon": {"atoms": ["C4'", "C3'", "O3'", "P"], "index": [0, 0, 0, 1]},
    "zeta": {"atoms": ["C3'", "O3'", "P", "O5'"], "index": [0, 0, 1, 1]},
    "chi": {"atoms": ["O4'", "C1'", "N1", "C2"], "index": [0, 0, 0, 0]},
    "eta": {"atoms": ["C4'", "P", "C4'", "P"], "index": [-1, 0, 0, 1]},
    "theta": {"atoms": ["P", "C4'", "P", "C4'"], "index": [0, 0, 1, 1]},
    "eta'": {"atoms": ["C1'", "P", "C1'", "P"], "index": [-1, 0, 0, 1]},
    "theta'": {"atoms": ["P", "C1'", "P", "C1'"], "index": [0, 0, 1, 1]},
    "torsion_OP1": {"atoms": ["C3'", "O3'", "P", "OP1"], "index": [-1, -1, 0, 0]},
    "torsion_OP2": {"atoms": ["C3'", "O3'", "P", "OP2"], "index": [-1, -1, 0, 0]},
    "v0": {"atoms": ["C4'", "O4'", "C1'", "C2'"], "index": [0, 0, 0, 0]},
    "v1": {"atoms": ["O4'", "C1'", "C2'", "C3'"], "index": [0, 0, 0, 0]},
    "v2": {"atoms": ["C1'", "C2'", "C3'", "C4'"], "index": [0, 0, 0, 0]},
    "v3": {"atoms": ["C2'", "C3'", "C4'", "O4'"], "index": [0, 0, 0, 0]},
    "v4": {"atoms": ["C3'", "C4'", "O4'", "C1'"], "index": [0, 0, 0, 0]},
}

TORSION_DEFS = {
    "alpha": {"atoms": ["O3'", "P", "O5'", "C5'"], "index": [-1, 0, 0, 0]},
    "beta": {"atoms": ["P", "O5'", "C5'", "C4'"], "index": [0, 0, 0, 0]},
    "gamma": {"atoms": ["O5'", "C5'", "C4'", "C3'"], "index": [0, 0, 0, 0]},
    "delta": {"atoms": ["C5'", "C4'", "C3'", "O3'"], "index": [0, 0, 0, 0]},
    "epsilon": {"atoms": ["C4'", "C3'", "O3'", "P"], "index": [0, 0, 0, 1]},
    "zeta": {"atoms": ["C3'", "O3'", "P", "O5'"], "index": [0, 0, 1, 1]},
    # "chi": {"atoms": ["O4'", "C1'", "N1", "C2"], "index": [0, 0, 0, 0]},
}

BOND_ANGLES = {
    "bond_epsilon": {"atoms": ["C3'", "O3'", "P"], "index": [-1, -1, 0]},
    "bond_torsion_OP1": {"atoms": ["O3'", "P", "OP1"], "index": [-1, 0, 0]},
    "bond_torsion_OP2": {"atoms": ["O3'", "P", "OP2"], "index": [-1, 0, 0]},
    "bond_zeta": {"atoms": ["O3'", "P", "O5'"], "index": [-1, 0, 0]},
    "bond_chi": {"atoms": ["O4'", "C1'", "N1", "C2"], "index": [0, 0, 0]},
    "bond_alpha": {"atoms": ["P", "O5'", "C5'"], "index": [0, 0, 0]},
    "bond_beta": {"atoms": ["O5'", "C5'", "C4'"], "index": [0, 0, 0]},
    "bond_gamma": {"atoms": ["C5'", "C4'", "C3'"], "index": [0, 0, 0]},
    "bond_delta": {"atoms": ["C4'", "C3'", "O3'"], "index": [0, 0, 0]},
}

TORSION_BOND_LENGTHS = {
    "alpha": 1.42,
    "beta": 1.5,
    "gamma": 1.52,
    "delta": 1.41,
    "epsilon": 1.6,
    "zeta": 1.59,
    "torsion_OP1": 1.48,
    "torsion_OP2": 1.48,
}
TORSION_BOND_ANGLES = {
    # "alpha": 59.01,
    # "beta": 68.75,
    # "gamma": 64.17,
    # "delta": 68.75,
    # "epsilon": 60.16,
    # "zeta": 76.2,
    # "torsion_OP1": 72.19,
    # "torsion_OP2": 71.62,
    "alpha": np.nan,
    "beta":np.nan,
    "gamma": np.nan,
    "delta": np.nan,
    "epsilon": np.nan,
    "zeta": np.nan,
    "torsion_OP1": np.nan,
    "torsion_OP2": np.nan,
}
TORSION_PEAK = {
    # "alpha": 295,
    # "beta": 170,
    # "gamma": 50,
    # "delta": 80,
    # "epsilon": 210,
    # "zeta": 285,
    # "torsion_OP1": 170,
    # "torsion_OP2": 40,
    "alpha": np.nan,
    "beta": np.nan,
    "gamma": np.nan,
    "delta": np.nan,
    "epsilon": np.nan,
    "zeta": np.nan,
    "torsion_OP1": np.nan,
    "torsion_OP2": np.nan,
}

CG_ATOMS = [
    "P",
    "O5'",
    "C5'",
    "C4'",
    "C3'",
    "O3'",
]  # Atoms for torsional angles reconstruction

ANGLES_CLEAN = {
            "alpha": r"$\alpha$",
            "beta": r"$\beta$",
            "gamma": r"$\gamma$",
            "delta": r"$\delta$",
            "epsilon": r"$\epsilon$",
            "zeta": r"$\zeta$",
            "chi": r"$\chi$",
            "eta": r"$\eta$",
            "theta": r"$\theta$",
        }