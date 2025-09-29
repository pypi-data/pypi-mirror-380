from typing import Dict, Tuple
import pandas as pd
import tqdm
import time

import os
import json
import numpy as np

from rna_synthub.filter.predict_abstract import PredictAbstract

COMMAND_SINGLE = "./helper/rnaqua/rnaqua-binary/bin/rnaqua.sh --command MOLPROBITY-SCORES " \
          "--single-model-file-path $INPUT_PATH --output-file-path $OUTPUT_PATH 2>&1 > /dev/null"



class MolProbityHelper(PredictAbstract):
    def __init__(self, tmp_dir: str = os.path.join("tmp", "clash_mol")):
        super().__init__(name="molprobity")
        self.tmp_dir = tmp_dir

    def predict_files(self, in_dir_path: str, out_path: str, out_time_path: str):
        """
        Given a directory of RNAs, it will predict the scoring function
        If out_path already exists, it will add to the file
        :return:
        """
        rnas = os.listdir(in_dir_path)
        names = ["badBondsCategory", "badAnglesCategory", "rankCategory"]

        # Load already processed RNAs if CSV exists
        if os.path.exists(out_path):
            print(f"LOADING : {out_path}")
            existing_df = pd.read_csv(out_path, index_col=0)
            processed_rnas = set(existing_df.index)
        else:
            processed_rnas = set()

        # Batch storage
        batch_out = {"rna": []}
        batch_out_time = {"rna": [], "time": []}
        for name in names:
            batch_out[name] = []

        for i, rna in enumerate(tqdm.tqdm(rnas), 1):
            if rna in processed_rnas:
                continue  # skip already processed RNA

            rna_path = os.path.join(in_dir_path, rna)
            scores, times = self.predict_single_file(rna_path)

            batch_out["rna"].append(rna)
            batch_out_time["rna"].append(rna)
            batch_out_time["time"].append(times)

            for score, name in zip(scores, names):
                batch_out[name].append(score)

            if len(batch_out["rna"]) == 1:
                df_out = pd.DataFrame(batch_out).set_index("rna")
                df_out_time = pd.DataFrame(batch_out_time).set_index("rna")

                df_out.to_csv(out_path, mode="a", header=not os.path.exists(out_path))
                df_out_time.to_csv(out_time_path, mode="a",
                                   header=not os.path.exists(out_time_path))

                # Update processed set and clear batch
                processed_rnas.update(batch_out["rna"])
                batch_out = {"rna": []}
                batch_out_time = {"rna": [], "time": []}
                for name in names:
                    batch_out[name] = []

        if batch_out["rna"]:
            df_out = pd.DataFrame(batch_out).set_index("rna")
            df_out_time = pd.DataFrame(batch_out_time).set_index("rna")

            df_out.to_csv(out_path, mode="a", header=not os.path.exists(out_path))
            df_out_time.to_csv(out_time_path, mode="a", header=not os.path.exists(out_time_path))

    def predict_single_file(self, rna_path: str) -> Tuple[float, float]:
        tmp_out = os.path.join(self.tmp_dir, "tmp.json")
        command = COMMAND_SINGLE.replace("$INPUT_PATH", rna_path).replace("$OUTPUT_PATH", tmp_out)
        time_b = time.time()
        os.system(command)
        time_e = time.time() - time_b
        try:
            mol_score = self.get_mol_scores(tmp_out)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            mol_score = [np.nan, np.nan, np.nan]
        if os.path.exists(tmp_out):
            os.system(f"rm {tmp_out}")
        return mol_score, time_e

    def get_mol_scores(self, in_path: str):
        """
        Extract the Molprobity scores
        """
        data = self.read_json(in_path).get("structure", {})
        badBondsCategory = data.get("badBondsCategory", None)
        badAnglesCategory = data.get("badAnglesCategory", None)
        rankCategory = data.get("rankCategory", None)
        return [badBondsCategory, badAnglesCategory, rankCategory]

    def read_json(self, in_path: str)->Dict:
        with open(in_path, "r") as f:
            data = json.load(f)
        return data


def main():
    folder = "folder_0"
    params = {
        # "in_dir_path": f"data/raw/PDB/missing/{folder}",
        "in_dir_path": f"data/raw/PDB/tmp/molprobity/{folder}",
        "out_path": f"data/tmp/molprobity/missing/scores_tmp/{folder}.csv",
        "out_time_path": f"data/tmp/molprobity/missing/times_tmp/{folder}.csv",
    }
    mol_helper = MolProbityHelper(tmp_dir = f"tmp/molprobity/{folder}_bis")
    mol_helper.predict_files(**params)

if __name__ == "__main__":
    main()