import os
import tqdm
import pandas as pd

class Selector:
    def __init__(self, in_dir: str, out_path: str):
        self.in_dir = in_dir
        self.df = self.read_df()
        self.out_path = out_path

    def read_df(self):
        csvs = [f"{name}.csv" for name in ["clash", "top_meta_scores", "molprobity", "rnaspider"]]
        all_dfs = []
        for filter in csvs:
            in_path = os.path.join(self.in_dir, filter)
            if os.path.exists(in_path):
                df = pd.read_csv(in_path, index_col=0)
                df.index = df.index.str.replace("/", "_")
                all_dfs.append(df)
        all_dfs = [d[~d.index.duplicated(keep="first")] for d in all_dfs]
        all_dfs = pd.concat(all_dfs, axis=1)
        return all_dfs

    def condition_filtering(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Select the structures with the following conditions:
            - Clash-score < 35
            - No entanglements
            - badAnglesCategory = Good|Caution and rankCategory = Good.
        :param df: df to select the structures from
        :return: a new dataframe with the selected structures
        """
        df = df[df["CLASH"] < 50]
        df = df[df["rnaspider"] == 0]
        df = df[
            (df["badAnglesCategory"].isin(["Good", "Caution",]))
            & (df["rankCategory"].isin(["Good", "Caution", "Warning"]) &
               (df["badBondsCategory"].isin(["Good", "Caution", "Warning"])))
            ]
        return df


    def run(self):
        df = self.condition_filtering(self.df)
        df.to_csv(self.out_path)
        return df

    def select_rnas(self, df: pd.DataFrame, in_path: str, out_dir: str):
        folders = os.listdir(in_path)
        os.makedirs(out_dir, exist_ok=True)
        all_len = 0
        all_rnas = []
        for folder in folders:
            c_in_dir = os.path.join(in_path, folder)
            rnas = [name for name in os.listdir(c_in_dir) if name in df.index]
            all_rnas.extend(rnas)
            all_len+= len(rnas)
            for rna in tqdm.tqdm(rnas):
                c_in_path = os.path.join(c_in_dir, rna)
                out_path = os.path.join(out_dir, rna)
                if not os.path.exists(out_path):
                    os.system(f"cp {c_in_path} {out_path}")
        missing_rnas = [rna for rna in df.index if rna not in all_rnas]
        breakpoint()
        print(f"Selected {all_len} RNAs")

def main():
    params = {
        "in_dir": "data/metadata/filter",
        "out_path": "data/metadata/results/filtered.csv",
    }
    selector = Selector(**params)
    df = selector.run()
    # in_path = "data/raw/PDB/missing"
    in_path = "../synthetic_dataset/data_official/models_clean/RFDiffusion"
    out_dir = "data/raw/PDB/filtered"
    selector.select_rnas(df, in_path, out_dir)

if __name__ == "__main__":
    main()