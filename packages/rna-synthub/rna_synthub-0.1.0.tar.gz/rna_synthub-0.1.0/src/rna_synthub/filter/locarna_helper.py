import os
import shutil
import time
from typing import Dict, List

import click
import pandas as pd
import tqdm

from rna_synthub.filter.utils import parse_clusters, read_aln, save_sequences_as_fasta

COMMAND_LOCARNA = "mlocarna $IN_PATH --tgtdir $OUT_DIR -q --keep-sequence-order --cpus=8"
COMMAND_CD_HIT = "lib/cd_hit/cd-hit -i $IN_PATH -o $OUT_DIR -n 5 -c 0.9 -M 16000 -d 0 -T 0 -l 100"


class LocaRNAHelper:
    def __init__(
        self,
        in_fasta_file: str,
        out_path: str,
        n_limit: int = 10,
        tmp_dir: str = os.path.join("tmp", "locarna"),
    ):
        self.in_fasta_file = in_fasta_file
        self.out_path = out_path
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        self.tmp_dir = tmp_dir
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)
        self.n_limit = n_limit

    def run(self):
        out = pd.read_csv(self.in_fasta_file, index_col=0)
        out["name"] = out.index
        out = out.rename(columns={"dot_bracket": "dot-bracket"})
        out = out.to_dict(orient="list")
        self.prepare_locarna(out)
        time_locarna = self.run_locarna()
        self.prepare_cd_hit()
        time_cd_hit = self.run_cd_hit()
        self.postprocess_cd_hit()
        save_path = os.path.join("data", "times", "2d")
        time_locarna.to_csv(os.path.join(save_path, "locarna_times.csv"), index=False)
        df_cd_hit = pd.DataFrame({"cd_hit": ["all"], "time": [time_cd_hit]})
        df_cd_hit.to_csv(os.path.join(save_path, "cd_hit_times.csv"), index=False)



    def postprocess_cd_hit(self):
        in_path = os.path.join(self.tmp_dir, "cd_hit", "output.clstr")
        clusters = parse_clusters(in_path)
        df_cluster = pd.DataFrame(clusters)
        df_cluster.columns = ["Name", "Cluster"]
        df_cluster.to_csv(self.out_path)
        shutil.rmtree(self.tmp_dir)

    def run_cd_hit(self):
        in_path = os.path.join(self.tmp_dir, "cd_hit", "input.fasta")
        out_dir = os.path.join(self.tmp_dir, "cd_hit", "output")
        command = COMMAND_CD_HIT.replace("$IN_PATH", in_path).replace("$OUT_DIR", out_dir)
        time_b = time.time()
        os.system(command)  # nosec
        time_e = time.time() - time_b
        return time_e

    def prepare_cd_hit(self):
        """
        Get the results from LocaRNA and merge it into one fasta file
        :return:
        """
        in_dir = os.path.join(self.tmp_dir, "output")
        files = os.listdir(in_dir)
        fasta_file = os.path.join(self.tmp_dir, "cd_hit", "input.fasta")
        os.makedirs(os.path.dirname(fasta_file), exist_ok=True)
        names, sequences = [], []
        for file in tqdm.tqdm(files):
            in_result_path = os.path.join(in_dir, file, "results", "result.aln")
            out = read_aln(in_result_path)
            for name, seq in out.items():
                if name not in names:
                    names.append(name)
                    sequences.append(seq.replace("-", "N"))
        save_sequences_as_fasta(sequences, names, fasta_file)

    def run_locarna(self):
        """
        Run the LocaRNA alignment based on the fasta subfiles.
        """
        tmp_dir = os.path.join(self.tmp_dir, "input")
        fasta_files = os.listdir(tmp_dir)
        out_dir = os.path.join(self.tmp_dir, "output")
        os.makedirs(out_dir, exist_ok=True)
        time_out = {"rna": [], "time": []}
        for fasta_file in tqdm.tqdm(fasta_files):
            in_path = os.path.join(tmp_dir, fasta_file)
            in_fasta = read_fasta_multiple(in_path)
            n_examples = len(in_fasta["name"])
            c_out_dir = os.path.join(out_dir, fasta_file.replace(".fasta", ""))
            command = COMMAND_LOCARNA.replace("$IN_PATH", in_path).replace("$OUT_DIR", c_out_dir)
            time_b = time.time()
            os.system(command)  # nosec
            time_e = time.time() - time_b
            time_e = time_e / n_examples
            time_out["rna"].append(fasta_file)
            time_out["time"].append(time_e)
        df = pd.DataFrame(time_out)
        return df


    def batch_fasta(self, fasta_dict: Dict[str, List[str]]):
        names = fasta_dict["name"]
        sequences = fasta_dict["sequence"]
        dot_brackets = fasta_dict["dot-bracket"]
        n_limit = min(len(names), self.n_limit)
        for i in range(0, len(names), n_limit):
            yield {
                "name": names[i : i + n_limit],
                "sequence": sequences[i : i + n_limit],
                "dot-bracket": dot_brackets[i : i + n_limit],
            }

    def prepare_locarna(self, fasta_content: Dict):
        """
        Splits the fasta file into small fasta files to be able to run LocaRNA.
        Keep the first RNA in head of each subfasta files.
        :param fasta_content: dictionary with the names, sequences and dot-bracket of structures
        to align
        """
        name0, seq0, dot0 = (
            fasta_content["name"][0],
            fasta_content["sequence"][0],
            fasta_content["dot-bracket"][0],
        )
        tmp_dir = os.path.join(self.tmp_dir, "input")
        os.makedirs(tmp_dir, exist_ok=True)
        for index, batch in enumerate(self.batch_fasta(fasta_content)):
            tmp_fasta_path = os.path.join(tmp_dir, f"file_{index}.fasta")
            seq, name, dot_bracket = batch["sequence"], batch["name"], batch["dot-bracket"]
            if index != 0:
                seq = [seq0] + seq
                name = [name0] + name
                dot_bracket = [dot0] + dot_bracket
            save_sequences_as_fasta(seq, name, tmp_fasta_path, dot_bracket)


@click.command()
@click.option("--in_fasta_file", type=str, help="Path to a file with sequence and 2D structure")
@click.option(
    "--out_path",
    type=str,
    help="Path where to save the .csv file with the clusters obtained with CD-HIT",
)
@click.option("--n_limit", type=int, help="Number of structures to consider in the LocaRNA part")
def main(in_fasta_file: str, out_path: str, n_limit: int = 10):
    locarna_helper = LocaRNAHelper(in_fasta_file, out_path, n_limit)
    locarna_helper.run()


if __name__ == "__main__":
    main()
