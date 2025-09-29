import os
import time
from typing import List, Optional, Tuple, Any

import click
import pandas as pd
import tqdm

from rna_synthub.filter.utils import get_sequence_from_pdb, get_number_first_residue, read_txt

FR3D_COMMAND = (
    "docker run -it --rm -v ${PWD}/$IN_DIR:/rna/input -v ${PWD}/$TMP_OUT:/rna/output "
    "sayby77/fr3d-image python fr3d/classifiers/NA_pairwise_interactions.py -i /rna/input -o /rna/output $RNA_NAME"
    " > /dev/null "
)

class Extract2D:
    def __init__(
        self,
        in_dir: str,
        out_path: Optional[str] = None,
        out_time_path: Optional[str] = None,
        tmp_dir: str = os.path.join("tmp", "fr3d"),
    ):
        """
        Extract 2D coordinates from pdb files
        :param in_dir: directory to the pdb files
        :param out_path: path to a .csv file where to save all the 2D structures
        :param out_time_path: path to a .csv file where to save the computation time
        """
        self.in_dir = in_dir
        self.out_path = out_path
        self.out_time_path = out_time_path
        os.makedirs(tmp_dir, exist_ok=True)
        self.tmp_dir = tmp_dir

    def extract(self):
        if os.path.exists(self.out_path):
            out = pd.read_csv(self.out_path)
            known_files = [name + ".pdb" for name in out["rna"].values]
            out_time = pd.read_csv(self.out_time_path)
        else:
            out = pd.DataFrame({"rna": [], "sequence": [], "dot_bracket": []})
            known_files = []
            out_time = pd.DataFrame({"rna": [], "time": []})
        files = [
            name
            for name in os.listdir(self.in_dir)
            if name.endswith(".pdb") and name not in known_files
        ]
        in_dir = self.in_dir
        index = 0
        for file in tqdm.tqdm(files):
            in_path = os.path.join(in_dir, file)
            try:
                seq, dot_bracket, c_time = self.extract_file(in_path)
            except FileNotFoundError:
                seq, dot_bracket, c_time = None, None, None
            rna_name = file.replace(".pdb", "")
            out.loc[len(out)] = [rna_name, seq, dot_bracket]
            out_time.loc[len(out_time)] = [rna_name, c_time]
            index += 1
            if index % 10 == 0 and self.out_path is not None:
                out.to_csv(self.out_path, index=False)
                out_time.to_csv(self.out_time_path, index=False)
        if self.out_path is not None:
            out.to_csv(self.out_path, index=False)
        if self.out_time_path is not None:
            out_time.to_csv(self.out_time_path, index=False)
        return out

    def extract_file(self, in_path: str) -> Tuple[str, str, int]:
        """
        Extract the 2D structure using FR3D
        :param in_path: path to a .pdb file
        :return: the RNA sequence as well as the dot-bracket 2D structure
        """
        time_b = time.time()
        interactions = self.extract_fr3d(in_path)
        seq = get_sequence_from_pdb(in_path)
        num_first_res = get_number_first_residue(in_path)
        dot_bracket = self.get_2d_from_fr3d(interactions, seq, num_first_res)
        time_e = time.time() - time_b
        return seq, dot_bracket, time_e

    def get_2d_from_fr3d(self, interactions: Any, sequence: str, num_first_res: int):
        """
        Return the dot-bracket 2D structure from list of interactions
        :param interactions: list of interactions (start_index and end_index)
        :param sequence: nucleotide sequence
        :param: num_first_residue: number of the first residue. Used to remove this as an offset.
        :return: dot-bracket 2D structure
        """
        dot_bracket = ["."] * len(sequence)
        for i_start, i_end in interactions:
            dot_bracket[i_start - num_first_res] = "("
            try:
                dot_bracket[i_end - num_first_res] = ")"
            except IndexError:
                pass
        return "".join(dot_bracket)

    def extract_fr3d(self, in_path: str) -> List[Tuple[int, int]]:
        """
        Extract the interactions using FR3D.
        :param in_path: path to '.pdb' 3D structure
        :return: a list of interactions (with the index of the nucleotides involved in the interaction)
        """
        in_dir = os.path.dirname(in_path)
        rna_name = os.path.basename(in_path)
        command = (
            FR3D_COMMAND.replace("$IN_DIR", in_dir)
            .replace("$RNA_NAME", rna_name)
            .replace("$TMP_OUT", self.tmp_dir)
        )
        os.system(command)  # nosec
        fr3d_out_path = os.path.join(self.tmp_dir, rna_name.replace(".pdb", "_basepair.txt"))
        try:
            interactions = self._get_interactions_from_fr3d_output(fr3d_out_path)
        except FileNotFoundError:
            interactions = None
        os.remove(fr3d_out_path)
        return interactions  # type: ignore

    def _get_interactions_from_fr3d_output(self, in_path: str) -> List:
        """
        Get the interactions from the FR3D output
        :param in_path: path to the output of FR3D
        :return: a list of interactions
        """
        content = read_txt(in_path)
        indexes = []
        for line in content:
            c_line = line.split("\t")
            i_start = int(c_line[0].split("|")[-1])
            i_end = int(c_line[-2].split("|")[-1])
            # Check only once the interactions
            if i_start < i_end:
                indexes.append((i_start, i_end))
        return indexes


@click.command()
@click.option("--in_dir", type=str, help="directory to the pdb files")
@click.option(
    "--out_path", type=str, help="path to a .csv file where to save all the 2D structures"
)
@click.option(
    "--out_time_path", type=str, help="path to a .csv file where to save the computation time"
)
def main(in_dir: str, out_path: Optional[str] = None, out_time_path: Optional[str] = None):
    extractor = Extract2D(in_dir, out_path, out_time_path)
    extractor.extract()


if __name__ == "__main__":
    main()
