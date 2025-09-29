import os
from typing import List, Optional, Tuple

import tqdm



class ExtractorAbstract:
    def __init__(self, cg_atoms: Optional[List] = None, *args, **kwargs):
        self.cg_atoms = cg_atoms

    def extract_from_pdb_dir(self, pdb_dir: str, pdb_out: str):
        """
        Extract the data from a pdb directory into another directory depending on the
        extraction algorithm.
        :param pdb_dir: path to a directory with pdb files
        :param pdb_out: path to a directory where to save the current modality
        """
        if os.path.isfile(pdb_dir):
            self.extract_from_pdb_file(pdb_dir, pdb_out)
        else:
            in_pdb_files, out_pdb_files = self.init_dirs(pdb_dir, pdb_out)
            for pdb_path, pdb_out_path in tqdm.tqdm(
                zip(in_pdb_files, out_pdb_files), total=len(in_pdb_files)
            ):
                if not os.path.exists(pdb_out_path):
                    self.extract_from_pdb_file(pdb_path, pdb_out_path)

    @staticmethod
    def init_dirs(pdb_dir: str, pdb_out: str) -> Tuple[List, List]:
        """
        Convert the directory to a list of .pdb file.
        Check also if the input is a single file or a directory.
        :param pdb_dir: path to a directory or to a single .pdb file
        :param pdb_out: path to a directory where to save the extracted modalities. Can be a file path.
        :return: list of full path to input pdb files and list of full path to output pdb files
        """
        if os.path.isdir(pdb_dir):
            pdb_files = [
                os.path.join(pdb_dir, name) for name in os.listdir(pdb_dir) if name.endswith(".pdb")
            ]
            os.makedirs(pdb_out, exist_ok=True)
            pdb_out_files = [
                os.path.join(pdb_out, os.path.basename(name).replace(".pdb", ""))
                for name in pdb_files
            ]
            return pdb_files, pdb_out_files
        elif os.path.isfile(pdb_dir):
            os.makedirs(os.path.dirname(pdb_out), exist_ok=True)
            return [pdb_dir], [pdb_out]
        else:
            raise ValueError(f"Path {pdb_dir} is not a valid file or directory")

    def extract_from_pdb_file(self, pdb_path: str, pdb_out: str):
        """
        Extract the structure into a modality
        :param pdb_path: path to a .pdb file
        :param pdb_out: path where to save the modality
        """
        raise NotImplementedError
