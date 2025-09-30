"""Plotting helpers for dive visualisations."""

from __future__ import annotations

from typing import Sequence

import matplotlib.pyplot as plt

from .models import Dive

_SUPPORTED_METRICS = {"po2", "po2_avg", "temperature"}


def _prepare_po2_series(dive: Dive, *, despike: bool, threshold: float):
    collection = dive.sensors.despiked(threshold=threshold) if despike else dive.sensors
    for series in collection:
        df = series.as_dataframe()
        label = f"Sensor {series.sensor_index + 1}"
        yield label, df["seconds"], df["value"]


def _prepare_po2_average(dive: Dive, *, despike: bool, threshold: float):
    collection = dive.sensors.despiked(threshold=threshold) if despike else dive.sensors
    if len(collection) == 0:
        return None
    data_frames = [series.as_dataframe() for series in collection]
    base = data_frames[0]
    combined = base[["seconds"]].copy()
    total = base["value"].copy()
    for frame in data_frames[1:]:
        combined = combined.merge(frame[["seconds", "value"]], on="seconds", how="inner", suffixes=("", "_alt"))
        total = combined["value"] + combined.filter(like="value_", axis=1).sum(axis=1)
    count = len(collection)
    avg = total / count
    return combined["seconds"], avg


def plot_dive(
    dive: Dive,
    metrics: Sequence[str] = ("po2",),
    *,
    despike: bool = True,
    spike_threshold: float = 0.5,
    ax=None,
):
    """Plot the requested metrics for a dive."""

    unknown = [metric for metric in metrics if metric not in _SUPPORTED_METRICS]
    if unknown:
        raise ValueError(f"Unsupported metrics: {', '.join(unknown)}")

    if ax is None:
        _, ax = plt.subplots(figsize=(10, 5))

    plotted = False

    temp_ax = None
    po2_plotted = False

    if "po2" in metrics:
        for label, seconds, values in _prepare_po2_series(dive, despike=despike, threshold=spike_threshold):
            ax.plot(seconds, values, label=label)
            plotted = True
            po2_plotted = True

    if "po2_avg" in metrics:
        result = _prepare_po2_average(dive, despike=despike, threshold=spike_threshold)
        if result:
            seconds, avg = result
            ax.plot(seconds, avg, label="Sensor Avg", linestyle="--")
            plotted = True
            po2_plotted = True

    if "temperature" in metrics and dive.temp.value is not None:
        temp_ax = temp_ax or ax.twinx()
        temp_color = "tab:red"
        temp_ax.axhline(
            dive.temp.value,
            label=f"Water Temp ({dive.temp.unit})",
            linestyle=":",
            color=temp_color,
        )
        temp_ax.set_ylabel(f"Water Temp ({dive.temp.unit})")
        temp_ax.tick_params(axis="y", colors=temp_color)
        temp_ax.spines["right"].set_color(temp_color)
        temp_ax.yaxis.label.set_color(temp_color)
        plotted = True

    if plotted:
        ax.set_xlabel("Seconds into dive")
        ax.set_ylabel("PO2 (ATA)" if po2_plotted else "Value")
        ax.set_title(f"Dive {dive.dive_id}")
        ax.grid(True, alpha=0.3)
        handles, labels = ax.get_legend_handles_labels()
        if temp_ax is not None:
            temp_handles, temp_labels = temp_ax.get_legend_handles_labels()
            handles += temp_handles
            labels += temp_labels
        ax.legend(handles, labels, loc="best")

    return ax


__all__ = ["plot_dive"]
