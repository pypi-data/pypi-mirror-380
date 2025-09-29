import os
import pandas as pd
import plotly.express as px

from rna_synthub.viz.utils import clean_fig


class VizHelper:
    clean_cat = {"CLASH": "Clash score", "META": "N-META",
                 "rnaspider": "Entanglements (RNAspider)"}
    colors = {"CLASH": ["#c3abce"], "META": ["#358292"], "rnaspider": ["#0c6856"]}

    def __init__(self, in_dir_path: str, out_path: str):
        self.in_dir_path = in_dir_path
        self.out_path = out_path
        self.df_seq = pd.read_csv("data/metadata/meta_scores.csv", index_col=[0])

    def run(self):
        list_files = os.listdir(self.in_dir_path)
        categories = {
            "clash.csv": "CLASH",
            "meta_scores.csv": "META",
            "top_meta_scores.csv": None,
            "rnaspider.csv": "rnaspider",
            "molprobity.csv": ["badBondsCategory", "badAnglesCategory", "rankCategory"]
        }
        for name in list_files:
            in_path = os.path.join(self.in_dir_path, name)
            out_path = os.path.join(self.out_path, name.replace(".csv", ".png"))
            df = pd.read_csv(in_path, index_col=[0])
            self.viz(df, categories[name], out_path)

    def _viz_molprobity(self, df: pd.DataFrame):
        df_long = df.melt(ignore_index=False, var_name="CategoryType", value_name="CategoryValue")
        df_long = df_long.replace({"badAnglesCategory": "Bad angles",
                                   "badBondsCategory": "Bad bonds",
                                   "rankCategory": "Rank"})
        fig = px.histogram(
            df_long,
            x="CategoryType",
            color="CategoryValue",
            barmode="group",
            text_auto=True,
            color_discrete_map={
                "Warning": "#B22222",
                "Caution": "#F08B51",
                "Good": "#33A1E0",
            },
            category_orders={
                "CategoryValue": ["Warning", "Caution", "Good"]
            }
        )
        fig = clean_fig(fig, y_title="Structures", x_title="MolProbity scores")
        fig = fig.update_traces(texttemplate="<br>%{value:,.0f}<br>", )
        fig.update_layout(
            legend=dict(
                orientation="h",
                bgcolor="rgba(0,0,0,0)",
                bordercolor="rgba(0,0,0,0)",
                borderwidth=1,
                yanchor="top",
                xanchor="right",
                x=1,
                y=1.03,
                font=dict(size=24, family="Computer Modern"),
            ),
            legend_title_text=None,
        )
        return fig

    def viz_rnaspider(self, df: pd.DataFrame, category: str, nbins: int = 200,
                      val_line: float = 35, text_vline: str = "Clash score < 35"):
        fig = px.histogram(df, x=category, nbins=nbins,
                           color_discrete_sequence=self.colors[category])
        fig.add_vline(
            x=val_line,
            line=dict(color="red", width=2, dash="dash"),
        )
        y_title = "Structures"
        if category in ["CLASH", "rnaspider"]:
            fig.update_yaxes(type="log")
            y_title = "Structures (log scale)"
        fig = clean_fig(fig, y_title=y_title, x_title=self.clean_cat[category])
        return fig

    def viz(self, df: pd.DataFrame, category: str, out_path: str):
        if category is None:
            return
        elif category == "rnaspider":
            fig = self.viz_rnaspider(df, category, nbins=40, val_line=0.5,
                                     text_vline="Structures without entanglements")
        elif category == "CLASH":
            fig = self.viz_rnaspider(df, category, nbins=200, val_line=50,
                                     text_vline="Clash score < 50")
        elif category == "META":
            df["sequence"] = self.df_seq["sequence"]
            c_df = df.drop_duplicates(subset="sequence", keep="first").sort_values(by=category,
                                                                                   ascending=False)
            val_line = c_df.head(50000)[category].min()
            fig = self.viz_rnaspider(c_df, category, nbins=200, val_line=val_line,
                                     text_vline="Top 100,000 structures")
        else:
            fig = self._viz_molprobity(df)
        fig.write_image(out_path, scale=3, width=800, height=500)
        # fig.show()

    @staticmethod
    def viz_all():
        params = {
            "in_dir_path": "data/metadata/filter",
            "out_path": "data/img/filter"
        }
        viz_helper = VizHelper(**params)
        viz_helper.run()


def main():
    VizHelper.viz()


if __name__ == "__main__":
    main()

