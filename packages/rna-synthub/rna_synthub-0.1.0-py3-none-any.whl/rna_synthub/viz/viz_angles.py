import os
from typing import Dict, List

import numpy as np

from rna_synthub.enum.angles import ANGLES_CLEAN
from rna_synthub.enum.scoring_functions import COLORS_MODELS
import tqdm
import pandas as pd

import plotly.graph_objects as go

from rna_synthub.viz.utils import rename_angles, clean_fig


class VizAngles:
    def __init__(self, data_paths: Dict):
        self.data_paths = data_paths
        self.data = self.read_data(data_paths)

    def read_data(self, data_paths: Dict) -> pd.DataFrame:
        """
        Read the data with angles and return a dataframe
        :param data_paths:
        :return:
        """
        data = {"angles": [], "dataset": [], "angle_names": []}
        for name, path in data_paths.items():
            list_files = os.listdir(path)
            for file in tqdm.tqdm(list_files):
                in_path = os.path.join(path, file)
                df = pd.read_csv(in_path, index_col = [0])
                # Convert angles from radians to degree
                df.drop(columns = ["sequence"], inplace = True, errors = "ignore")
                df[df.columns] = np.degrees(df[df.columns])
                # df = df * 180 / np.pi
                for angle_name in df.columns:
                    data["angles"].extend(df[angle_name].tolist())
                    data["angle_names"].extend([angle_name] * len(df))
                    data["dataset"].extend([name] * len(df))
        df = pd.DataFrame(data)
        return df

    def plot_polar(self, model: List, save_path: str):
        df = self.data.copy()
        df = df[df["dataset"].isin(model)]
        df = rename_angles(df)
        df = df.rename(columns={"angles": "Angles", "dataset": "Dataset"})
        frequencies_dict = self.convert_df_to_frequencies(df)
        angles = df["angle_names"].unique().tolist()
        for angle in angles:
            fig = self._plot_polar(frequencies_dict, angle, colors=None, to_show=False)
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(showticklabels=True, ticks=''),
                    angularaxis=dict(
                        showticklabels=False,
                    ),
                ),
            )
            c_path = save_path.replace(".png", f"{angle}_.png")
            fig.write_image(c_path, scale=2, width=1200, height=800)

    def _plot_polar(
        self, frequencies_dict: dict, angle: str, colors=None, to_show: bool = False
    ):
        fig = self.get_polar_plot_single(frequencies_dict, angle)
        fig = clean_fig(fig, x_title="Test", y_title="Test")
        fig.update_layout(margin=dict(b=20, t=50, r=20, l=50))
        new_polars = {
            f"polar{i}": dict(
                radialaxis=dict(
                    type="log",
                    showline=True,
                    showgrid=True,
                    ticks=None,
                    linewidth=1,
                    linecolor="black",
                    gridcolor="grey",
                    gridwidth=1,
                    dtick=1,
                ),
                angularaxis=dict(
                    linewidth=2, visible=True, linecolor="black", showline=True
                ),
                radialaxis_tickfont_size=24,
                bgcolor="white",
            )
            for i in range(1, 10)
        }
        if to_show:
            fig.update_layout(
                font_size=16,
            )
            fig.update_layout(
                **new_polars,
                showlegend=False,
            )
            fig.show()
        fig.update_layout(
            **new_polars,
            showlegend=False,
        )
        fig.update_layout(paper_bgcolor="white")
        fig.update_layout(
            font_size=24,
        )
        for annotation in fig.layout.annotations:
            annotation.y += 1
        return fig

    def get_polar_plot_single(self, frequencies_dict: Dict, angle: str):
        fig = go.Figure()
        for split, frequencies in frequencies_dict.items():
            clean_name = ANGLES_CLEAN.get(angle, angle)
            fig.add_trace(
                go.Barpolar(
                    r=frequencies[clean_name],
                    theta=np.arange(0, 360, 5),
                    marker_color=COLORS_MODELS.get(split, "gray"),
                    marker_line_color="black",
                    marker_line_width=1,
                    opacity=0.8,
                    name=split,
                )
            )
        fig.update_layout(
            title=angle,
            polar=dict(
                radialaxis=dict(showticklabels=True, ticks=''),
                angularaxis=dict(direction="clockwise", rotation=0)
            ),
            showlegend=True,
        )

        return fig

    def convert_df_to_frequencies(self, df: pd.DataFrame):
        output = {}
        for dataset in df["Dataset"].unique():
            c_df = df[df["Dataset"] == dataset]
            output[dataset] = {}
            for angle in df["angle_names"].unique():
                c_angles = c_df[c_df["angle_names"] == angle]
                c_angles = c_angles[c_angles.notnull()]
                angle_values = c_angles["Angles"].values
                angle_values[angle_values < 0] = angle_values[angle_values < 0] + 360
                frequencies = self.get_angles_frequencies(angle_values)
                output[dataset][angle] = frequencies
        return output

    def get_angles_frequencies(self, angles):
        bins = np.arange(0, 360, 5)
        frequencies = np.histogram(angles, bins=bins)[0]
        frequencies = frequencies / np.sum(frequencies)
        return frequencies

    @staticmethod
    def plot_distribution_polar_data(save_dir: str):
        prefix = os.path.join("data", "raw", "angles_bis")
        data_paths = {
            name: os.path.join(prefix, name) for name in os.listdir(prefix)
        }
        # all_models = [["Native"]]
        all_models = [["Boltz1", "RNAComposer", "RFDiffusion"]]
        for model in all_models:
            data_p = {key: value for key, value in data_paths.items() if key in model}
            suffix = "native" if len(model) == 1 else "model"
            c_dir = os.path.join(save_dir, suffix)
            os.makedirs(c_dir, exist_ok=True)
            save_path = os.path.join(c_dir, "polar.png")
            viz_angles = VizAngles(data_p)
            viz_angles.plot_polar(model, save_path)
            break