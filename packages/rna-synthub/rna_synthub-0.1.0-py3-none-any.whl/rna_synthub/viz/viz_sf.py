import os
from typing import Any, Dict

import numpy as np
import plotly.express as px
import pandas as pd
from sklearn.preprocessing import StandardScaler


ALL_SF_1 = {
    "3drnascore": "3dRNAscore",
    "PAMNet": "PAMNet",
    "cgRNASP": "cgRNASP",
    "RASP-ENERGY": "RASP",
    "BARNABA-eSCORE": "eSCORE",
}
ALL_SF_2 = {
    "LociPARSE": "LociPARSE",
    "TB-MCQ": "TB-MCQ",
    "DFIRE": "DFIRE",
    "rsRNASP": "rsRNASP",
    "N-META": "N-META",
}
COLORS_MODELS = {
    "RNAComposer": "#ef8927",
    "RFDiffusion": "#32a02d",
    "Boltz1": "#00569e",
}
SCORING_FUNCTIONS = ["DFIRE", "rsRNASP", "TB-MCQ", "LociPARSE"]


class VizSF:
    def __init__(self, in_dir: str, out_dir: str):
        self.list_sf = SCORING_FUNCTIONS
        self.df = self.read_all_df(in_dir)
        self.out_dir = out_dir

    def read_all_df(self, in_dir: str):
        files = [os.path.join(in_dir, name) for name in os.listdir(in_dir) if name.endswith(".csv")]
        all_data = {"rna": [], "model": [], "split": []}
        all_columns = set()

        for name in files:
            df = pd.read_csv(name, index_col=0)
            all_columns.update(df.columns)

        for col in all_columns:
            all_data[col] = []

        for name in files:
            df = pd.read_csv(name, index_col=0)
            base = os.path.basename(name).split("_")
            model, split = base[0], base[1]

            for rna, row in df.iterrows():
                all_data["rna"].append(rna)
                all_data["model"].append(model)
                all_data["split"].append(split)

                for col in all_columns:
                    all_data[col].append(row[col] if col in row else np.nan)

        all_df = pd.DataFrame(all_data)
        df_norm = all_df[self.list_sf].copy()
        return all_df


    def clean_fig(self, fig: Any, x_title: str, y_title: str):
        fig.update_yaxes(matches=None, showticklabels=True)
        params_axes = dict(
            showgrid=True,
            gridcolor="#d6d6d6",
            linecolor="black",
            zeroline=False,
            linewidth=1,
            showline=True,
            mirror=True,
            gridwidth=1,
            griddash="dot",
        )
        fig.update_xaxes(**params_axes, title=x_title)
        fig.update_yaxes(**params_axes, title=y_title)
        fig.update_layout(dict(plot_bgcolor="white"), margin=dict(l=0, r=5, b=0, t=20))
        param_marker = dict(
            opacity=1, line=dict(width=0.5, color="DarkSlateGrey"), size=6
        )
        fig.update_traces(marker=param_marker, selector=dict(mode="markers"))
        fig.update_layout(
            font=dict(
                family="Computer Modern",
                size=28,
            )
        )
        fig.update_layout(
            showlegend=False,
            legend_title_text=None,
        )
        return fig

    def update_fig_box_plot(self,
            fig: Any, contour: bool = True
    ) -> Any:
        fig.update_yaxes(matches=None, showticklabels=True)
        params_axes = dict(
            showgrid=True,
            gridcolor="#d6d6d6",
            linecolor="black",
            zeroline=False,
            linewidth=1,
            showline=True,
            mirror=True,
            gridwidth=1,
            griddash="dot",
            title=None,
        )
        fig.update_xaxes(**params_axes)
        fig.update_yaxes(**params_axes)
        fig.update_layout(dict(plot_bgcolor="white"), margin=dict(l=5, r=5, b=5, t=20))
        param_marker = dict(opacity=1, line=dict(width=0.5, color="DarkSlateGrey"), size=6)
        fig.update_traces(marker=param_marker, selector=dict(mode="markers"))
        fig.update_layout(
            font=dict(
                family="Computer Modern",
                size=20,
            )
        )
        fig.update_layout(
            showlegend=False,
            legend_title_text=None,
        )
        fig.update_xaxes(visible=True, showticklabels=True)
        if contour:
            fig.for_each_trace(
                lambda t: t.update(
                    line=dict(color="black"),
                    fillcolor=t.marker.color
                )
            )
        return fig


    def run_boxplot(self, out_path: str, dict_sf: Dict):
        scaler = StandardScaler()
        df_scaled = self.df.copy()
        columns = list(dict_sf.keys())
        df_scaled[columns] = scaler.fit_transform(self.df[columns])
        df_long = df_scaled.melt(id_vars=["model"], value_vars = list(dict_sf.keys()),
                               var_name = "Scoring function", value_name = "Values")
        df_long = df_long.replace(dict_sf)
        # fig = px.box(df_long, x="Scoring function", y="Values", color="model", points = "all",
        #              boxmode="group", color_discrete_map=COLORS_MODELS)
        fig = px.violin(df_long, x="Scoring function", y="Values", color="model", points = False,
                     color_discrete_map=COLORS_MODELS)
        fig = self.update_fig_box_plot(fig)
        fig.update_yaxes(title="Standardized values", range=[-6, 6])
        fig.write_image(out_path, scale=3, width=800, height=400)
        # fig.show()

    @staticmethod
    def viz_sf():
        prefix = "data/img/sf"
        params = {
            "in_dir": "data/metadata/scoring_functions",
            "out_dir": prefix
        }
        viz_sf = VizSF(**params)

        viz_sf.run_boxplot(os.path.join(prefix, "boxplot_1.png"), ALL_SF_1)
        viz_sf.run_boxplot(os.path.join(prefix, "boxplot_2.png"), ALL_SF_2)
