from typing import List, Optional, Dict, Tuple, no_type_check
import re
import numpy as np
TYPE_MATRIX = np.ndarray
import torch

from Bio.PDB import PDBParser


def get_number_first_residue(in_pdb_path: str) -> int:
    """
    Return the number of the first residue.
    :param in_pdb_path: path to a .pdb file
    :return: the number in the chain of the first residue.
    """
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("RNA", in_pdb_path)
    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.id[0] == " ":
                    return residue.id[1]
    return 0

def read_txt(in_file: str) -> List:
    """
    Read a .txt file
    :param in_file: path to a .txt file
    :return: a list with the content for each line
    """
    with open(in_file, "r") as f:
        out = f.readlines()
    return out

def save_to_txt(out_list: List, out_path: str):
    """
    Save a list to a .txt file
    :param out_list: the list to save
    :param out_path: path to save the .txt file
    :return:
    """
    with open(out_path, "w") as f:
        for item in out_list:
            f.write(f"{item}\n")

def save_sequences_as_fasta(
    sequences: List, rna_names: List, out_fasta_path: str, dot_brackets: Optional[List] = None
):
    """
    Save the RNAs as a fasta file
    :param sequences: the RNA sequences
    :param rna_names: the RNA names
    :param out_fasta_path: path to save the .fasta format file
    :param dot_brackets: the dot-bracket structures of the RNAs
    :return:
    """
    with open(out_fasta_path, "w") as f:
        for index, (rna_name, sequence) in enumerate(zip(rna_names, sequences)):
            f.write(f">{rna_name}\n")
            f.write(f"{sequence}\n")
            if dot_brackets is not None and dot_brackets[index] is not None:
                f.write(f"{dot_brackets[index]}\n")

def parse_clusters(file_path: str) -> List[Tuple[str, str]]:
    """
    Read the output of CD-HIT and return the name of the RNA with their cluster number
    :param file_path: path to a .clstr file output by CD-HIT.
    """
    clusters = []
    current_cluster = None
    with open(file_path, "r") as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith(">Cluster"):
            current_cluster = line.split()[1]
        elif ">" in line:
            match = re.search(r">(\w+_\w+_\w+)", line)
            if match:
                rna_name = match.group(1)
                clusters.append((rna_name, current_cluster))
    return clusters  # type: ignore

def read_aln(in_path: str) -> Dict:
    """
    Read the output of LocaRNA file (.aln file)
    :param in_path: path to the output file of LocaRNA
    :return: names and sequences
    """
    with open(in_path, "r") as file:
        file_content = file.read()
    file_content = file_content.replace("CLUSTAL W --- LocARNA 1.9.1", "")
    matches = re.findall(r"(\S+)\s+([AUGC\-]+)", file_content)
    out: Dict = {}
    for name, seq in matches:
        out[name] = out.get(name, "") + seq
    return out


def read_fasta_multiple(in_fasta_path: str) -> Dict[str, List[str]]:
    """
    Read a fasta file with multiple sequences and convert it into a dictionary.

    :param in_fasta_path: Path to a .fasta file
    :return: A dictionary with the names, sequences, and dot-bracket structures from the fasta file
    """
    fasta_dict: Dict = {"name": [], "sequence": [], "dot-bracket": []}
    with open(in_fasta_path, "r") as f:
        name, sequence = None, []  # type: ignore
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if name:
                    fasta_dict["name"].append(name)
                    fasta_dict["sequence"].append("".join(sequence[:-1]))
                    fasta_dict["dot-bracket"].append(sequence[-1] if sequence else "")
                name, sequence = line[1:], []
            else:
                sequence.append(line)
        if name:
            fasta_dict["name"].append(name)
            fasta_dict["sequence"].append("".join(sequence[:-1]))
            fasta_dict["dot-bracket"].append(sequence[-1] if sequence else "")
    return fasta_dict

def save_sequences_as_fasta(
    sequences: List, rna_names: List, out_fasta_path: str, dot_brackets: Optional[List] = None
):
    """
    Save the RNAs as a fasta file
    :param sequences: the RNA sequences
    :param rna_names: the RNA names
    :param out_fasta_path: path to save the .fasta format file
    :param dot_brackets: the dot-bracket structures of the RNAs
    :return:
    """
    with open(out_fasta_path, "w") as f:
        for index, (rna_name, sequence) in enumerate(zip(rna_names, sequences)):
            f.write(f">{rna_name}\n")
            f.write(f"{sequence}\n")
            if dot_brackets is not None and dot_brackets[index] is not None:
                f.write(f"{dot_brackets[index]}\n")


def get_sequence_from_pdb(in_pdb: str) -> str:
    """
    Return the residual sequence of a given .pdb file
    """
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("RNA", in_pdb)
    sequence = ""
    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.id[0] == " ":
                    sequence += residue.resname
    return sequence


@no_type_check
def get_matrix_from_pdb(in_path: str, cg_atoms: List, to_torch: bool = False) -> TYPE_MATRIX:
    """
    Convert input matrix into a matrix (either numpy or tensor)
    :param in_path: path to a .pdb file
    :param cg_atoms: list of atoms to keep when reading the .pdb file
    :param to_torch: whether to convert the output to a torch tensor

    The output is of size (L, N_atoms, 3) where :
        - L is the number of residues
        - N_atoms is the number of coarse-grained atoms
        - 3 is the number of coordinates (x, y, z)
    """
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("RNA", in_path)
    output = []
    base_specific_atom_map = {"N": {"A": "N9", "G": "N9", "C": "N1", "U": "N1"}}
    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.id[0] == " ":
                    atoms = {atom.name: atom.get_coord() for atom in residue}
                    out = []
                    for atom in cg_atoms:
                        actual_atom = atom
                        if (
                                atom in base_specific_atom_map
                                and residue.resname in base_specific_atom_map[atom]
                        ):
                            actual_atom = base_specific_atom_map[atom][residue.resname]
                        if (
                                actual_atom in atoms
                                and (atoms[actual_atom] > np.array([-999] * 3)).all()
                        ):
                            out.append(atoms[actual_atom])
                        else:
                            out.append([np.nan] * 3)
                    output.append(out)
    output = np.array(output)
    if to_torch:
        output = torch.tensor(output, dtype=torch.float32)
    return output



def compute_distances(matrix: np.ndarray) -> np.ndarray:
    """
    Compute the distance matrix between each atom of the input

    :param matrix: a matrix of size (L, N_atoms, 3)
    :return: the distance matrix of size (L, L, N_atoms*N_atoms)
    """
    n_res, n_atoms, _ = matrix.shape

    coords1 = matrix[:, None, :, :]
    coords2 = matrix[None, :, :, :]

    diff = coords1[..., None, :, :] - coords2[..., :, None, :]
    distances = np.linalg.norm(diff, axis=-1)
    distances = distances.reshape(n_res, n_res, n_atoms ** 2)[:, :, 0]
    return distances
