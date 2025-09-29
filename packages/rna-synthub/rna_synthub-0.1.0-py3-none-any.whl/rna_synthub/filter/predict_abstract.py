import os
from typing import Tuple

import tqdm
import pandas as pd


class PredictAbstract:
    def __init__(self, name: str):
        self.name = name

    def predict_dir(self, in_dir: str, out_dir: str, out_time_dir: str = None):
        """
        Given a directory of directories of RNAs, it will predict the scoring function
        :param in_dir:
        :param out_dir:
        :return:
        """
        rna_dir = os.listdir(in_dir)
        for rna_d in tqdm.tqdm(rna_dir):
            in_dir_path = os.path.join(in_dir, rna_d)
            out_path = os.path.join(out_dir, rna_d+".csv")
            out_time_path = None if out_time_dir is None else os.path.join(out_time_dir, rna_d+".csv")
            if os.path.exists(out_path):
                df = pd.read_csv(out_path, index_col=[0])
                if self.name in df.columns:
                    continue
            self.predict_files(in_dir_path, out_path, out_time_path)

    def predict_files(self, in_dir_path: str, out_path: str, out_time_path: str):
        """
        Given a directory of RNAs, it will predict the scoring function
        If out_path already exists, it will add to the file
        :return:
        """
        rnas = os.listdir(in_dir_path)
        out = {"rna": [], self.name: []}
        out_time = {"rna": [], "time": []}
        for rna in tqdm.tqdm(rnas):
            rna_path = os.path.join(in_dir_path, rna)
            scores, times = self.predict_single_file(rna_path)
            out["rna"].append(rna)
            out_time["rna"].append(rna)
            out[self.name].append(scores)
            out_time["time"].append(times)
        out = pd.DataFrame(out, index=out["rna"])
        out = out.drop(["rna"], axis=1)
        out_time = pd.DataFrame(out_time, index=out_time["rna"])
        out_time = out_time.drop(["rna"], axis=1)
        self.merge_dfs(out, out_path)
        self.merge_dfs(out_time, out_time_path)

    def merge_dfs(self, df: pd.DataFrame, out_path: str):
        """
        Merge the df if it exists otherwise save it
        """
        if os.path.exists(out_path):
            c_df = pd.read_csv(out_path, index_col=[0])
            if "normalized" in c_df.index[0]:
                df.index = df.index.map(lambda x: f"normalized_{x}")
            df = pd.concat([c_df, df], axis=1)
        df.to_csv(out_path)

    def predict_single_file(self, rna_path: str) -> Tuple[float, float]:
        raise NotImplementedError("This method should be implemented in the child class")