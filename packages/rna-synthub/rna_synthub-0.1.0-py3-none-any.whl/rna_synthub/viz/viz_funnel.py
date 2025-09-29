from plotly import graph_objects as go

import os

class VizFunnel:
    def __init__(self, out_path: str):
        self.out_path = out_path
        os.makedirs(os.path.dirname(out_path), exist_ok=True)

    def clean_fig(self, fig):
        fig.update_layout(
            dict(plot_bgcolor="white"), margin=dict(l=10, r=5, b=10, t=20)
        )
        fig.update_layout(
            font=dict(
                family="Computer Modern",
                size=20,
            )
        )
        return fig

    def run(self):
        fig = go.Figure(go.Funnel(
            y=["Top structures based on N-META", "Clash score < 50", "Entanglements (RNAspider)",
               "MolProbity scores", "Redundancy (clustering)"],
            x=[50000, 23051, 21213, 18682, 16734],
            textinfo="label+value+percent initial",
            texttemplate="%{label}<br>%{value:,.0f}<br>%{percentInitial:.0%}",
            textposition="inside",
            opacity=1,
            marker={
                "color": ["#34808f", "#c3abd0", "#01695c", "#cccc98", "#745644"],
                "line": {"color": "black", "width": 1}, }
        )
        )
        fig = self.clean_fig(fig)
        fig.write_image(self.out_path, scale=4, width=800, height=400)

    @staticmethod
    def viz():
        out_path = os.path.join("data", "img", "figures", "funnel.png")
        viz_funnel = VizFunnel(out_path)
        viz_funnel.run()



def main():
    VizFunnel.viz()

if __name__ == "__main__":
    main()