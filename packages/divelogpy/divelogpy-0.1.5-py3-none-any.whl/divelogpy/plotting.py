"""Plotting helpers for dive visualisations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Mapping, Sequence

import matplotlib.pyplot as plt

try:  # optional dependency
    import plotly.graph_objects as go
except ImportError:  # pragma: no cover - optional dependency
    go = None

from .models import Dive
import pandas as pd


@dataclass
class _ScaleField:
    field: str
    label: str | None = None
    color: str | None = None
    dash: str | None = None
    width: float | None = None


@dataclass
class _ScaleGroup:
    fields: List[_ScaleField]
    title: str | None = None
    side: str | None = None
    range: Sequence[float] | None = None


def _ensure_plotly():
    if go is None:  # pragma: no cover - depends on optional dependency
        raise RuntimeError("Plotly is required for interactive timeseries plotting. Install it with 'pip install plotly'.")


def _normalise_scale_groups(scale_groups: Sequence[object] | None) -> List[_ScaleGroup]:
    if not scale_groups:
        return []

    palette = [
        "#FF851B",
        "#FF4136",
        "#2ECC40",
        "#FFDC00",
        "#0074D9",
        "#B10DC9",
    ]

    palette_index = 0

    result: List[_ScaleGroup] = []
    for group in scale_groups:
        if isinstance(group, str):
            group_map: Mapping[str, object] = {"fields": [group]}
        elif isinstance(group, Mapping):
            group_map = group
        elif isinstance(group, Sequence) and not isinstance(group, (bytes, bytearray)):
            group_map = {"fields": list(group)}
        else:
            raise TypeError(
                "Each scale group must be a mapping of options, a list/tuple of field names, or a single field name."
            )

        raw_fields = group_map.get("fields")
        if not raw_fields:
            raise ValueError("Scale group requires a non-empty 'fields' list.")

        normalised_fields: List[_ScaleField] = []
        for payload in raw_fields:
            if isinstance(payload, str):
                payload_map = {"field": payload}
            elif isinstance(payload, Mapping):
                payload_map = dict(payload)
            else:
                raise TypeError("Scale group fields must be either field names or mapping descriptors.")

            field_name = payload_map.get("field")
            if not field_name:
                raise ValueError("Scale group field descriptors must include a 'field' entry.")

            color = payload_map.get("color")
            if color is None:
                color = palette[palette_index % len(palette)]
                palette_index += 1

            normalised_fields.append(
                _ScaleField(
                    field=field_name,
                    label=payload_map.get("label"),
                    color=color,
                    dash=payload_map.get("dash"),
                    width=payload_map.get("width"),
                )
            )

        result.append(
            _ScaleGroup(
                fields=normalised_fields,
                title=group_map.get("title"),
                side=group_map.get("side"),
                range=group_map.get("range"),
            )
        )

    return result



def plot_timeseries(
    timeseries,
    *,
    include_depth: bool = True,
    depth_field: str | None = None,
    depth_label: str | None = None,
    depth_color: str = "#1f77b4",
    depth_fillcolor: str = "rgba(31, 119, 180, 0.25)",
    depth_side: str = "left",
    scale_groups: Sequence[Mapping[str, object]] | None = None,
    template: str = "plotly_dark",
    time_units: str = "minutes",
    time_axis_label: str | None = None,
    figure_title: str | None = None,
) -> "go.Figure":
    """Render an interactive Plotly figure for a dive timeseries.

    Parameters
    ----------
    timeseries:
        Either a :class:`divelogpy.timeseries.DiveTimeSeries` instance or any
        object that exposes ``to_df`` with a matching signature.
    include_depth:
        When True (default) the depth trace is added as the primary axis.
    depth_field:
        Optional override for the depth column to display. When omitted the
        function prefers ``depth_ft`` then ``depth_m`` if present.
    depth_label:
        Custom axis label for depth. If omitted a label derived from the depth
        field is used.
    depth_color / depth_fillcolor:
        Styling for the depth trace and area fill.
    depth_side:
        Position of the depth axis (``'left'`` or ``'right'``).
    scale_groups:
        Sequence describing additional y-axes. Each element may be one of:

        * A single field name (``"average_ppo2"``)
        * A list/tuple of field names (``["average_ppo2", "ppo2_setpoint"]``)
        * A mapping with ``fields`` and optional styling keys (``{"fields": [...], "title": "ppO₂"}``).

        Field descriptors within a mapping can override ``label``, ``color``,
        ``dash`` and ``width`` for each trace. Group-level options include
        ``title`` (axis label), ``side`` (``"left"``/``"right"``) and ``range``.
        When omitted no additional axes are drawn.
    template:
        Plotly template, defaults to ``plotly_dark``.
    time_units:
        Units for the x-axis; either ``'minutes'`` (default) or ``'seconds'``.
    time_axis_label:
        Optional label for the x-axis. If omitted a label is derived from
        ``time_units``.
    figure_title:
        Optional figure title.
    """

    _ensure_plotly()

    groups = _normalise_scale_groups(scale_groups)
    df = timeseries
    if not isinstance(timeseries,pd.DataFrame):
        if not hasattr(timeseries, "to_df"):
            raise TypeError("timeseries must provide a 'to_df' method.")
        df = timeseries.to_df()
        

    available_fields = df.columns

    depth_candidates: Iterable[str]
    if depth_field:
        depth_candidates = (depth_field,)
    else:
        depth_candidates = ("depth_ft", "depth_m", "depth")

    chosen_depth_field = None
    derived_label = depth_label
    if include_depth:
        if isinstance(available_fields, Sequence) and not isinstance(available_fields, str):
            available_set = set(available_fields)
        else:
            available_set = None

        for candidate in depth_candidates:
            if candidate is None:
                continue
            if available_set is not None and candidate not in available_set:
                continue
            chosen_depth_field = candidate
            break
        if chosen_depth_field is None:
            raise ValueError("Depth data was requested but no depth field was supplied or discovered.")

    required_fields = {field.field for group in groups for field in group.fields}
    if include_depth and chosen_depth_field:
        required_fields.add(chosen_depth_field)

    if not required_fields:
        raise ValueError("No fields were provided to plot. Supply scale groups or enable depth.")


    if df.empty:
        raise ValueError("The requested timeseries fields contain no data.")

    df = df.reset_index().rename(columns={"time_seconds": "seconds"})
    if "seconds" not in df.columns:
        raise ValueError("Timeseries must expose a 'time_seconds' column when converted to a DataFrame.")
    seconds_series = df["seconds"].astype(float)

    time_units_normalised = time_units.lower()
    if time_units_normalised == "seconds":
        time_values = seconds_series
        xaxis_title = time_axis_label or "Time (s)"
    elif time_units_normalised == "minutes":
        time_values = seconds_series / 60.0
        xaxis_title = time_axis_label or "Time (min)"
    else:
        raise ValueError("time_units must be either 'seconds' or 'minutes'.")

    fig = go.Figure()

    depth_side_normalised = depth_side.lower()
    if depth_side_normalised not in {"left", "right"}:
        raise ValueError("depth_side must be either 'left' or 'right'.")

    if include_depth and chosen_depth_field:
        if chosen_depth_field not in df.columns:
            raise ValueError(f"Depth field '{chosen_depth_field}' is not present in the timeseries data.")
        derived_label = depth_label
        if derived_label is None:
            if chosen_depth_field.endswith("_ft"):
                derived_label = "Depth (ft)"
            elif chosen_depth_field.endswith("_m"):
                derived_label = "Depth (m)"
            else:
                derived_label = "Depth"

        fig.add_trace(
            go.Scatter(
                x=time_values,
                y=df[chosen_depth_field],
                mode="lines",
                name=derived_label,
                line=dict(color=depth_color, width=2),
                fill="tozeroy",
                fillcolor=depth_fillcolor,
                hovertemplate="%{y:.2f}<extra>" + derived_label + "</extra>",
            )
        )

    axis_layout: dict[str, object] = {
        "template": template,
        "xaxis": dict(title=xaxis_title, zeroline=False),
        "legend": dict(orientation="h", y=1.05, x=0.5, xanchor="center"),
    }

    has_primary_axis = include_depth and chosen_depth_field is not None
    if has_primary_axis:
        axis_layout["yaxis"] = dict(title=depth_label or derived_label, autorange="reversed", side=depth_side_normalised)
    else:
        axis_layout["yaxis"] = dict(title="Value", side="left")

    next_axis_index = 2 if has_primary_axis else 1

    for idx, group in enumerate(groups):
        if not has_primary_axis and idx == 0:
            axis_name = "y"
            axis_key = "yaxis"
            axis_layout[axis_key]["side"] = (group.side or "left").lower()
            if group.title:
                axis_layout[axis_key]["title"] = group.title
            if group.range:
                axis_layout[axis_key]["range"] = list(group.range)
        else:
            axis_name = f"y{next_axis_index}"
            axis_key = f"yaxis{next_axis_index}"
            axis_layout[axis_key] = dict(overlaying="y", side=(group.side or "right").lower())
            if group.title:
                axis_layout[axis_key]["title"] = group.title
            if group.range:
                axis_layout[axis_key]["range"] = list(group.range)
            next_axis_index += 1

        for field in group.fields:
            column = field.field
            if column not in df.columns:
                raise ValueError(f"Field '{column}' is not available in the timeseries DataFrame.")
            trace_kwargs = dict(
                x=time_values,
                y=df[column],
                mode="lines",
                name=field.label or column,
                line=dict(color=field.color, dash=field.dash, width=field.width or 2),
            )
            if axis_name != "y":
                trace_kwargs["yaxis"] = axis_name
            fig.add_trace(go.Scatter(**trace_kwargs))

    if figure_title:
        axis_layout["title"] = figure_title

    fig.update_layout(**axis_layout)

    return fig


__all__ = ["plot_dive", "plot_timeseries"]
