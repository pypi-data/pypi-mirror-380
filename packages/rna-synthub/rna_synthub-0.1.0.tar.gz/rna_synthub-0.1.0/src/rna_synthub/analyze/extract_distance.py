import numpy as np
import os

from rna_synthub.analyze.extractor_abstract import ExtractorAbstract
from rna_synthub.filter.utils import get_matrix_from_pdb, compute_distances, get_sequence_from_pdb


class ExtractorDistance(ExtractorAbstract):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def extract_from_pdb_file(self, pdb_path: str, pdb_out: str):
        """
        Extract the distances from a pdb file.
        Save into a `.npz` file with the following keys:
            - `distances`: a matrix of distances between atoms. Shape: (L, L, N_atoms*N_atoms)
            - `sequence`: a string with the residues. Shape: (L, )
            - `atoms`: a list of atoms. Shape: (N_atoms, )
        :param pdb_path: path to a `.pdb` file
        :param pdb_out: path to a `.npz` file
        """
        out_name = pdb_out + ".npy"
        if os.path.exists(out_name):
            return
        if isinstance(self.cg_atoms, str):
            self.cg_atoms = [self.cg_atoms]
        try:
            points = get_matrix_from_pdb(pdb_path, self.cg_atoms, to_torch=False)
            distances = compute_distances(points)
        except ValueError:
            print(f"Error computing distances for {pdb_path}. Skipping.")
            return
        sequence = get_sequence_from_pdb(pdb_path)
        if len(sequence) != distances.shape[0]:
            raise ValueError(
                f"Sequence length ({len(sequence)}) and distance matrix length ({distances.shape[0]}) do not match"
            )
        tri_vals = distances[np.triu_indices(distances.shape[0], k=1)]
        hist, _ = np.histogram(tri_vals, bins=100, range=(0, 150), density=True)
        np.save(
            out_name, {
                "distances": distances,
                "d_bins": hist,
                "sequence": sequence,
                "atoms": self.cg_atoms,
            }, allow_pickle=True)

