import os
from collections import Counter
import numpy as np
from sklearn.manifold import TSNE
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import tqdm

from rna_synthub.enum.scoring_functions import COLORS_MODELS
from rna_synthub.viz.utils import clean_fig


class VizDistance:
    def __init__(self, in_dir: str, out_path: str, bins: bool = False):
        """
        Compute the t-SNE based on the distance matrices
        :param in_dir: directory where are stored the different .npy files
        :param out_path: where to save the output of the t-SNE
        """
        self.df_dict = self.read_data(in_dir, bins)
        self.out_path = out_path

    def read_data(self, in_dir: str, bins: bool):
        models = ["RNAComposer", "RFDiffusion", "Boltz1", "Native"]
        all_data = {"model": [], "distances": [], "sequences": [],
                    "rna": []}
        for model in models:
            c_in_dir = os.path.join(in_dir, model)
            out_dist, out_seq, out_rna = self.read_dir(c_in_dir, bins)
            all_data["model"].extend([model] * len(out_dist))
            all_data["distances"].extend(out_dist)
            all_data["sequences"].extend(out_seq)
            all_data["rna"].extend(out_rna)
        try:
            all_data["distances"] = np.array(all_data["distances"])
        except ValueError:
            pass
        return all_data


    def read_dir(self, in_dir: str, bins: bool = True):
        list_files = [os.path.join(in_dir, name) for name in os.listdir(in_dir) if name.endswith(".npy")]
        out_dist, out_seq, out_rna = [], [], []
        for name in tqdm.tqdm(list_files):
            data = np.load(name, allow_pickle=True).item()
            if bins:
                distances = data["d_bins"]
            else:
                distances = data["distances"]
                distances = distances[np.triu_indices(distances.shape[0], k=1)]
            if np.isnan(distances).any():
                continue
            sequence = data["sequence"]
            rna = name.split("/")[-1].replace(".npy", "")
            out_dist.append(distances.flatten())
            out_seq.append(sequence)
            out_rna.append(rna)
        try:
            out_dist = np.array(out_dist)
        except ValueError:
            pass
        return out_dist, out_seq, out_rna


    def run(self, n_per_model: int = 1000):
        tsne = TSNE(n_components=2, random_state=77)
        data = np.array(self.df_dict["distances"])
        embedding = tsne.fit_transform(data)
        df = pd.DataFrame({
            "x": embedding[:, 0],
            "y": embedding[:, 1],
            "model": self.df_dict["model"],
            "rna": self.df_dict["rna"],
        })
        if n_per_model != "all":
            df = (
                df.groupby("model")
                .apply(lambda x: x.sample(n=min(len(x), n_per_model), random_state=77))
                .reset_index(drop=True)
            )
        fig = px.scatter(
            df,
            x="x",
            y="y",
            color="model",
            opacity=0.6,
            color_discrete_map=COLORS_MODELS,
            hover_data=["rna"],
        )
        fig.update_traces(marker=dict(size=4, line=dict(width=0)))
        fig = self.clean_fig(fig)
        fig.write_image(self.out_path, scale=1.5, width=800, height=600)

    def clean_fig(self, fig):
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
                size=12,
            )
        )
        fig.update_layout(
            showlegend=False,
            legend_title_text=None,
        )
        return fig

    def _viz_distribution_distance(self):
        nbins = 50
        fig = go.Figure()
        unique_models = set(self.df_dict['model'])

        for model in unique_models:
            all_distances = []
            for m, distances in zip(self.df_dict['model'], self.df_dict['distances']):
                if m == model:
                    all_distances.extend(np.array(distances).flatten())
            counts, edges = np.histogram(all_distances, bins=nbins)
            fig.add_trace(go.Bar(
                x=(edges[:-1] + edges[1:]) / 2,
                y=counts,
                name=model,
                opacity=0.6,
                marker_color=COLORS_MODELS.get(model, "gray"),
            ))
        fig = clean_fig(fig, x_title="Distance (Å)", y_title="Atom pairs", font_size=20)
        fig.update_layout(
            showlegend=False,
            legend_title_text=None,
        )
        fig.update_layout(
            barmode='overlay',
            showlegend=True,
            legend = dict(x = 1, y = 1, xanchor = 'right', yanchor = 'top')
        )
        fig.write_image(self.out_path, scale=2, width=800, height=400)

    def run_length(self):
        sequences = self.df_dict["sequences"]
        len_sequences = [len(seq) for seq in sequences]
        counts = Counter(sequences)
        most_common_seq, most_common_count = counts.most_common(1)[0]
        df = pd.DataFrame({"length": len_sequences, "model": self.df_dict["model"]})
        c_df = df[df["model"] == "RFDiffusion"]["length"]
        min_len, max_len, mean_len = c_df.min(), c_df.max(), c_df.mean()
        print(f"RFDiffusion length: min {min_len}, max {max_len}, mean {mean_len:.2f}")

    @staticmethod
    def viz_distribution_distance():
        in_dir = os.path.join("data", "raw", "distance")
        out_path = os.path.join("data", "img", "distance", "distribution_distance.png")
        clustering = VizDistance(in_dir, out_path)
        clustering._viz_distribution_distance()

    @staticmethod
    def viz_tsne():
        n_per_sample = "all"
        in_dir = os.path.join("data", "raw", "distance")
        out_path = os.path.join("data", "img", "distance",f"tsne_subsample_{n_per_sample}.png")
        clustering = VizDistance(in_dir, out_path, bins=True)
        clustering.run(n_per_sample)

    @staticmethod
    def viz_length():
        in_dir = os.path.join("data", "raw", "distance")
        out_path = None
        clustering = VizDistance(in_dir, out_path)
        clustering.run_length()


def main():
    VizDistance.viz_tsne()
    # VizDistance.viz_length()
    # VizDistance.viz_distribution_distance()

if __name__ == "__main__":
    main()