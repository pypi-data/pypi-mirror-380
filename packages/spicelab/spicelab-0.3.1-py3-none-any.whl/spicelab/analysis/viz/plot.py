"""Compatibility wrappers for Plotly-based visualization helpers."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from ...io.raw_reader import TraceSet
from ...viz import (
    VizFigure,
    bode_view,
    monte_carlo_histogram,
    monte_carlo_kde,
    monte_carlo_param_scatter,
    nyquist_view,
    params_scatter_matrix,
    step_response_view,
    sweep_curve,
    time_series_view,
)


def _ensure_traceset(obj: TraceSet | Any) -> TraceSet:
    if isinstance(obj, TraceSet):
        return obj
    if hasattr(obj, "data_vars"):
        return TraceSet.from_dataset(obj)
    raise TypeError("Expected TraceSet or xarray.Dataset-like object")


def plot_traces(
    ts: TraceSet | Any,
    ys: Sequence[str] | None = None,
    *,
    title: str | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    legend: bool = True,
    grid: bool = True,
    tight: bool = True,
    ax: Any | None = None,
    template: str | None = "plotly_white",
    markers: bool = False,
    color_map: Mapping[str, str] | None = None,
    x: str | None = None,
    line_width: float | None = None,
    marker_size: int | None = None,
) -> VizFigure:
    """Render time-domain traces using the Plotly backend.

    Parameters mirror the historical Matplotlib API; ``ax`` is no longer supported and
    ``tight`` is kept for compatibility (no effect).
    """

    if ax is not None:  # pragma: no cover - compatibility guard
        raise ValueError("plot_traces no longer accepts a Matplotlib axis; pass ax=None")
    ts = _ensure_traceset(ts)
    fig = time_series_view(
        ts,
        ys,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        legend=legend,
        grid=grid,
        template=template,
        markers=markers,
        color_map=color_map,
        x=x,
        line_width=line_width,
        marker_size=marker_size,
    )
    return fig


def plot_bode(
    ts: TraceSet | Any,
    y: str,
    *,
    unwrap_phase: bool = True,
    title_mag: str | None = None,
    title_phase: str | None = None,
    template: str | None = "plotly_white",
    x: str | None = None,
) -> VizFigure:
    ts = _ensure_traceset(ts)
    title = title_mag or title_phase
    return bode_view(ts, y, unwrap_phase=unwrap_phase, title=title, template=template, x=x)


def plot_step_response(
    ts: TraceSet | Any,
    y: str,
    *,
    steady_state: float | None = None,
    initial_value: float | None = None,
    settle_tolerance: float = 0.02,
    title: str | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    template: str | None = "plotly_white",
    show_annotations: bool = True,
    x: str | None = None,
) -> VizFigure:
    ts = _ensure_traceset(ts)
    return step_response_view(
        ts,
        y,
        x=x,
        steady_state=steady_state,
        initial_value=initial_value,
        settle_tolerance=settle_tolerance,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        template=template,
        show_annotations=show_annotations,
    )


def plot_nyquist(
    ts: TraceSet | Any,
    y: str,
    *,
    title: str | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    template: str | None = "plotly_white",
    show_arrow: bool = True,
) -> VizFigure:
    ts = _ensure_traceset(ts)
    return nyquist_view(
        ts,
        y,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        template=template,
        show_arrow=show_arrow,
    )


def plot_sweep_df(
    df: Any,
    x: str,
    y: str,
    hue: str,
    title: str | None = None,
    *,
    xlabel: str | None = None,
    ylabel: str | None = None,
    legend: bool = True,
    grid: bool = True,
    tight: bool = True,
    ax: Any | None = None,
    template: str | None = "plotly_white",
) -> VizFigure:
    if ax is not None:  # pragma: no cover - compatibility guard
        raise ValueError("plot_sweep_df no longer accepts a Matplotlib axis; pass ax=None")
    fig = sweep_curve(
        df,
        x,
        y,
        hue,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        legend=legend,
        template=template,
    )
    if not grid:
        fig.figure.update_xaxes(showgrid=False)
        fig.figure.update_yaxes(showgrid=False)
    return fig


def plot_mc_metric_hist(
    metrics: Sequence[float] | None = None,
    title: str | None = None,
    bins: int | None = 50,
    *,
    xlabel: str | None = None,
    ylabel: str | None = None,
    grid: bool = True,
    tight: bool = True,
    ax: Any | None = None,
    template: str | None = "plotly_white",
) -> VizFigure:
    if metrics is None:
        raise ValueError("metrics list is required")
    if ax is not None:  # pragma: no cover - compatibility guard
        raise ValueError("plot_mc_metric_hist no longer accepts a Matplotlib axis; pass ax=None")
    fig = monte_carlo_histogram(
        metrics,
        title=title,
        bins=bins or 50,
        xlabel=xlabel,
        ylabel=ylabel,
        template=template,
    )
    if not grid:
        fig.figure.update_xaxes(showgrid=False)
        fig.figure.update_yaxes(showgrid=False)
    return fig


def plot_param_vs_metric(
    samples: Sequence[Mapping[str, float]],
    metrics: Sequence[float],
    param: str,
    *,
    title: str | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    grid: bool = True,
    tight: bool = True,
    ax: Any | None = None,
    template: str | None = "plotly_white",
) -> VizFigure:
    if ax is not None:  # pragma: no cover - compatibility guard
        raise ValueError("plot_param_vs_metric no longer accepts a Matplotlib axis; pass ax=None")
    fig = monte_carlo_param_scatter(
        samples,
        metrics,
        param,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        template=template,
    )
    if not grid:
        fig.figure.update_xaxes(showgrid=False)
        fig.figure.update_yaxes(showgrid=False)
    return fig


def plot_mc_kde(
    metrics: Sequence[float],
    *,
    title: str | None = None,
    bandwidth: float | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    grid: bool = True,
    tight: bool = True,
    ax: Any | None = None,
    template: str | None = "plotly_white",
) -> VizFigure:
    if ax is not None:  # pragma: no cover - compatibility guard
        raise ValueError("plot_mc_kde no longer accepts a Matplotlib axis; pass ax=None")
    fig = monte_carlo_kde(metrics, title=title, xlabel=xlabel, template=template)
    if ylabel is not None:
        fig.figure.update_layout(yaxis_title=ylabel)
    if not grid:
        fig.figure.update_xaxes(showgrid=False)
        fig.figure.update_yaxes(showgrid=False)
    return fig


def plot_params_matrix(
    samples: Sequence[Mapping[str, float]],
    params: Sequence[str] | None = None,
    *,
    figsize: tuple[int, int] | None = None,
    tight: bool = True,
    template: str | None = "plotly_white",
) -> VizFigure:
    """Create a pairwise scatter matrix for Monte Carlo samples using Plotly."""

    return params_scatter_matrix(samples, params=params, template=template)
