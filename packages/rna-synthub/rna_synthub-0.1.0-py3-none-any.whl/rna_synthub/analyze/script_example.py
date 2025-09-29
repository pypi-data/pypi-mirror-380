import os
import pandas as pd

from rna_synthub.analyze.extract_angles import ExtractorAngles
from rna_synthub.analyze.extract_distance import ExtractorDistance
from rna_synthub.enum.angles import CG_ATOMS
from rna_synthub.filter.extract_2d import Extract2D
from rna_synthub.filter.locarna_helper import LocaRNAHelper
from rna_synthub.filter.molprobity_helper import MolProbityHelper
from rna_synthub.filter.rnaspider_helper import RNASpiderHelper
from rna_synthub.pdb_helper.sf_models import SFModels


class ScriptExample:
    PREFIX = os.path.join("data", "examples")
    PDB_PATH = os.path.join(PREFIX, "pdb")

    @staticmethod
    def merge_clash_output(in_dir: str, out_path: str):
        """
        Merge all the .csv from a folder into a single .csv
        """
        all_df = []
        list_rnas = [name for name in os.listdir(in_dir) if name.endswith(".csv")]
        for rna in list_rnas:
            in_path = os.path.join(in_dir, rna)
            df = pd.read_csv(in_path, index_col=0)
            all_df.append(df)
        all_df = pd.concat(all_df)
        all_df.to_csv(out_path)


    @staticmethod
    def run_clash():
        out_path = os.path.join(ScriptExample.PREFIX, "filter", "clash_scores.csv")
        out_time_path = out_path.replace(".csv", "_times.csv")
        params = {"score": ["clash"],
                  "in_dir": ScriptExample.PDB_PATH,
                  "out_path": out_path,
                  "out_time_path": out_time_path}
        SFModels(**params).run()

    @staticmethod
    def compute_n_meta():
        params = {"score": ["dfire", "lociparse", "tb-mcq", "rs-rnasp"],
                  "in_dir": ScriptExample.PDB_PATH,
                  "out_path": os.path.join(ScriptExample.PREFIX, "sf", "sf_scores.csv"),
                  "out_time_path": os.path.join(ScriptExample.PREFIX, "sf", "sf_times.csv")}
        SFModels(**params).run()

    @staticmethod
    def run_rnaspider():
        out_path = os.path.join(ScriptExample.PREFIX, "filter", "rnaspider.csv")
        out_time_path = out_path.replace(".csv", "_time.csv")
        params = {"in_dir_path": ScriptExample.PDB_PATH,
                  "out_path": out_path,
                  "out_time_path": out_time_path}
        rnaspider_helper = RNASpiderHelper()
        rnaspider_helper.predict_files(**params)

    @staticmethod
    def run_molprobity():
        out_path = os.path.join(ScriptExample.PREFIX, "filter", "molprobity.csv")
        out_time_path = out_path.replace(".csv", "_time.csv")
        params = {
            "in_dir_path": ScriptExample.PDB_PATH,
            "out_path": out_path,
            "out_time_path": out_time_path
        }
        mol_helper = MolProbityHelper()
        mol_helper.predict_files(**params)

    @staticmethod
    def compute_filter():
        """
        Compute CLASH-score, Molprobity and entanglements
        """
        os.makedirs(os.path.join(ScriptExample.PREFIX, "filter"), exist_ok=True)
        ScriptExample.run_clash()
        ScriptExample.run_rnaspider()
        ScriptExample.run_molprobity()

    @staticmethod
    def compute_2d():
        prefix = os.path.join(ScriptExample.PREFIX, "2d")
        os.makedirs(prefix, exist_ok=True)
        out_path = os.path.join(prefix, "structures.csv")
        out_time_path = out_path.replace(".csv", "_time.csv")
        params = {
            "in_dir": ScriptExample.PDB_PATH,
            "out_path": out_path,
            "out_time_path": out_time_path,
        }
        Extract2D(**params).extract()

    @staticmethod
    def compute_clustering():
        params = {
           "in_fasta_file" : "data/times/2d/structures.csv",
            "out_path": "data/times/2d/clustering.csv"
        }
        LocaRNAHelper(**params).run()

    @staticmethod
    def extract_angles():
        extractor_angles = ExtractorAngles(CG_ATOMS)
        pdb_dir = ScriptExample.PDB_PATH
        out_dir = "data/examples/angles"
        extractor_angles.extract_from_pdb_dir(pdb_dir, out_dir)

    @staticmethod
    def extract_distances():
        extractor_distance = ExtractorDistance(["C3'"])
        pdb_dir = ScriptExample.PDB_PATH
        out_path = "data/examples/distances"
        extractor_distance.extract_from_pdb_dir(pdb_dir, out_path)

        if __name__ == "__main__":
            main()


def main():
    # ScriptExample.compute_n_meta()
    # ScriptExample.compute_filter()
    # ScriptExample.compute_2d()
    # ScriptExample.compute_clustering()

    # Script to extract angles and distances
    # ScriptExample.extract_angles()
    ScriptExample.extract_distances()

if __name__ == "__main__":
    main()