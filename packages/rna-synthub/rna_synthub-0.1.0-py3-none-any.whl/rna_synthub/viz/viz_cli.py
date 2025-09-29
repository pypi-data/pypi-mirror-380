import os
from typing import List

import pandas as pd

from rna_synthub.viz.viz_angles import VizAngles
from rna_synthub.viz.viz_distance import VizDistance
from rna_synthub.viz.viz_funnel import VizFunnel
from rna_synthub.viz.viz_helper import VizHelper
from rna_synthub.viz.viz_sf import VizSF


class VizCLI:
    @staticmethod
    def viz_funnel():
        VizFunnel.viz()

    @staticmethod
    def viz_filter():
        VizHelper.viz_all()

    @staticmethod
    def viz_best_worst():
        df = pd.read_csv("data/metadata/results/top_50k.csv", index_col=[0])
        df = df.sort_values(by="META", ascending=False)
        columns = ["META", "CLASH"]
        best = df.head(5)[columns]
        worst = df.tail(5)[columns]
        print(best)
        print(worst)
        df = pd.read_csv("data/metadata/filter/meta_scores.csv", index_col=[0])
        df = df.dropna()
        df = df.sort_values(by="META", ascending=False)
        worst = df.tail(5)["META"]
        print(worst)

    @staticmethod
    def viz_distance():
        # VizDistance.viz_distribution_distance()
        VizDistance.viz_tsne()

    @staticmethod
    def viz_sf():
        VizSF.viz_sf()

    @staticmethod
    def get_time_specific(df: pd.DataFrame, name: List):
        df_filter = df[df.columns[df.columns.str.contains(name)]]
        df_filter["SUM"] = df_filter.sum(axis=1)
        df_mean = df_filter["SUM"].mean()
        df_std = df_filter["SUM"].std()
        print(f"Mean time for {name}: {df_mean:.1f} +/- {df_std:.1f}")

    @staticmethod
    def viz_times():
        prefix = os.path.join("data", "times")
        list_files = ["filter/clash_scores_times.csv", "filter/molprobity_time.csv",
                      "filter/rnaspider_time.csv", "sf/sf_times.csv",
                      "2d/structures_time.csv", "2d/cd_hit_times.csv", "2d/locarna_times.csv"]
        all_df = None
        for file in list_files:
            path = os.path.join(prefix, file)
            df = pd.read_csv(path, index_col=[0])
            df = df.rename({"time": file.replace(".csv", "")}, axis=1)
            df.index = df.index.str.replace("/", "_")
            if all_df is None:
                all_df = df
            else:
                try:
                    all_df = all_df.join(df, how="outer")
                except ValueError:
                    breakpoint()
        df_stats = all_df.agg(["mean", "std"]).T.round(1)
        VizCLI.get_time_specific(all_df, "filter|CLASH")
        VizCLI.get_time_specific(all_df, "LociPARSE|rsRNASP|DFIRE|TB-MCQ")
        print(df_stats)

    @staticmethod
    def viz_angles():
        save_dir = os.path.join("data", "img", "angles")
        VizAngles.plot_distribution_polar_data(save_dir)

    @staticmethod
    def main():
        # VizCLI.viz_funnel()
        # VizCLI.viz_filter()
        # VizCLI.viz_best_worst()
        # VizCLI.viz_distance()
        # VizCLI.viz_sf()
        # VizCLI.viz_times()
        VizCLI.viz_angles()

def main():
    VizCLI.main()

if __name__ == "__main__":
    main()