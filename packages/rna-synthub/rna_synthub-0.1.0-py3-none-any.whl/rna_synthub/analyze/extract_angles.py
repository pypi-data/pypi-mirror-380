from typing import Dict

import numpy as np
import pandas as pd
import torch

from rna_synthub.analyze.extractor_abstract import ExtractorAbstract
from rna_synthub.enum.angles import CG_ATOMS, TORSION_PEAK, TORSION_DEFS, TORSION_BOND_ANGLES
from rna_synthub.filter.utils import get_matrix_from_pdb, get_sequence_from_pdb


class ExtractorAngles(ExtractorAbstract):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def extract_from_pdb_file(self, pdb_path: str, pdb_out: str):
        """
        Extract the angles from a pdb file and save it into .csv file
        :param pdb_path: path to a .pdb file
        :param pdb_out: path to a .csv file
        """
        try:
            points = get_matrix_from_pdb(pdb_path, self.cg_atoms, to_torch=True)
            sequence = get_sequence_from_pdb(pdb_path)
            torsion_angles = self._compute_angles(points)
            bond_angles = self._compute_bond_angles(points)
            bond_angles = {f"bond_{key}": value for key, value in bond_angles.items()}
            df = pd.DataFrame(
                {**{"sequence": list(sequence)}, **torsion_angles, **bond_angles},
                index=range(1, len(sequence) + 1),
            )
            df = df.round(3)
            df.to_csv(pdb_out+".csv")
        except (RuntimeError, ValueError) as e:
            print(f"Error computing angles for {pdb_path}: {e}. Skipping.")
            return

    @staticmethod
    def compute_torsion(p0, p1, p2, p3):
        """
        Compute torsion angle for 4 points (batched)
        """
        b0 = p1 - p0
        b1 = p2 - p1
        b2 = p3 - p2

        b1_norm = b1 / torch.norm(b1, dim=-1, keepdim=True)

        n1 = torch.cross(b0, b1)
        n2 = torch.cross(b1, b2)

        n1 = n1 / torch.norm(n1, dim=-1, keepdim=True)
        n2 = n2 / torch.norm(n2, dim=-1, keepdim=True)

        m1 = torch.cross(n1, b1_norm)

        x = (n1 * n2).sum(dim=-1)
        y = (m1 * n2).sum(dim=-1)
        return torch.atan2(y, x)

    def _compute_angles(self, points: np.ndarray, default_values=TORSION_PEAK) -> Dict:
        """
        Compute all the angles for the given structure.
        :param points: the matrix with the coordinates
        :return: a list with the angle values
        """
        L = points.shape[0]
        torsions = {k: [] for k in TORSION_DEFS}
        name_to_idx = {name: i for i, name in enumerate(CG_ATOMS)}

        for i in range(L):
            for name, defn in TORSION_DEFS.items():
                # Fallback value if undefined
                fallback = np.radians(default_values.get(name, 0.0)) if default_values else 0.0

                # Check index bounds
                if any(i + offset < 0 or i + offset >= L for offset in defn["index"]):
                    torsions[name].append(torch.tensor(fallback, device=points.device))
                    continue

                idxs = [i + offset for offset in defn["index"]]
                atom_idxs = [name_to_idx[a] for a in defn["atoms"]]

                try:
                    pts = [points[idx, atom_idx] for idx, atom_idx in zip(idxs, atom_idxs)]
                    torsion = self.compute_torsion(*pts)
                    torsions[name].append(torsion)
                except IndexError:
                    torsions[name].append(torch.tensor(fallback, device=points.device))

        torsions = {k: torch.stack(v, dim=0) for k, v in torsions.items()}
        return torsions

    def pad_and_replace_nan(self, x, key, target_len, default_values):
        # Pad if needed
        pad_size = target_len - x.shape[0]
        if pad_size > 0:
            pad = torch.full((pad_size,), float("nan"), device=x.device, dtype=x.dtype)
            x = torch.cat([x, pad], dim=0)
        # Replace NaNs with defaults if specified
        if default_values and key in default_values:
            default = torch.tensor(default_values[key], device=x.device, dtype=x.dtype)
            x = torch.where(torch.isnan(x), default, x)
        return x

    def bond_angle_for_nerf(self, prev, center, next_):
        """
        Compute internal bond angles at 'center' (B–C–D) in batch mode.
        Inputs:
            prev, center, next_: Tensors of shape (..., 3)
        Returns:
            angles: Tensor of shape (...)
        """
        v1 = prev - center
        v2 = next_ - center

        v1 = v1 / torch.norm(v1, dim=-1, keepdim=True)
        v2 = v2 / torch.norm(v2, dim=-1, keepdim=True)

        cos_angle = (v1 * v2).sum(dim=-1).clamp(-1.0, 1.0)
        angle = torch.acos(cos_angle)

        return torch.pi - angle  # NeRF convention: internal angle

    def _compute_bond_angles(
        self, points: torch.Tensor, default_values=TORSION_BOND_ANGLES
    ) -> Dict:
        """
        Compute all the bond angles for the given structure.
        :param points: the matrix with the coordinates
        :return: a list of bond angles
        """
        L = points.shape[0]
        default_values = {key: np.radians(value) for key, value in default_values.items()}
        bond_angles = {}

        bond_angles["alpha"] = self.pad_and_replace_nan(
            self.bond_angle_for_nerf(points[:, 0], points[:, 1], points[:, 2]),
            "alpha",
            L,
            default_values,
        )
        bond_angles["beta"] = self.pad_and_replace_nan(
            self.bond_angle_for_nerf(points[:, 1], points[:, 2], points[:, 3]),
            "beta",
            L,
            default_values,
        )
        bond_angles["gamma"] = self.pad_and_replace_nan(
            self.bond_angle_for_nerf(points[:, 2], points[:, 3], points[:, 4]),
            "gamma",
            L,
            default_values,
        )
        bond_angles["delta"] = self.pad_and_replace_nan(
            self.bond_angle_for_nerf(points[:, 3], points[:, 4], points[:, 5]),
            "delta",
            L,
            default_values,
        )
        bond_angles["epsilon"] = self.pad_and_replace_nan(
            self.bond_angle_for_nerf(points[:-1, 4], points[:-1, 5], points[1:, 0]),
            "epsilon",
            L,
            default_values,
        )
        bond_angles["zeta"] = self.pad_and_replace_nan(
            self.bond_angle_for_nerf(points[:-1, 5], points[1:, 0], points[1:, 1]),
            "zeta",
            L,
            default_values,
        )

        return bond_angles


