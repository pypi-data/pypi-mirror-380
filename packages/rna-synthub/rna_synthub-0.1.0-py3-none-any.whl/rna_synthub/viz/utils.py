from typing import Any
import pandas as pd

from rna_synthub.enum.angles import ANGLES_CLEAN


def clean_fig(fig: Any, x_title: str, y_title: str, font_size: int = 28):
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
            size=font_size,
        )
    )
    return fig

def update_fig_box_plot(
        fig: Any,
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
            size=12,
        )
    )
    fig.update_layout(
        legend=dict(
            orientation="v",
            bgcolor="#f3f3f3",
            bordercolor="Black",
            borderwidth=1,
        ),
    )
    fig.update_xaxes(visible=True, showticklabels=True)
    return fig


def rename_angles(df: pd.DataFrame):
    return df.replace(
        ANGLES_CLEAN,
    )
