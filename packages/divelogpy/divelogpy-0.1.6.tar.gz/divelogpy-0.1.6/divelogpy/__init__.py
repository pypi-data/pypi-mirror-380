"""Convenience entry points for the dive log library."""

from .client import get_client, DiveLogClient
from .models import Dive, UnitMeasure, SensorSeries, SensorCollection
from .plotting import plot_timeseries
from .decoders import (
    decode_petrel_po2_series,
    decode_petrel_raw_floats,
    decode_petrel_frames,
    decompress_petrel_blob,
    decode_metadata_blob,
)
from .pnf_decoder import decode_petrel_v14
from .pnf_constants import PNF_V14_CONSTANTS
from .timeseries import DiveTimeSeries

__all__ = [
    "get_client",
    "DiveLogClient",
    "Dive",
    "UnitMeasure",
    "SensorSeries",
    "SensorCollection",
    "decode_petrel_po2_series",
    "decode_petrel_raw_floats",
    "decode_petrel_frames",
    "decompress_petrel_blob",
    "decode_metadata_blob",
    "decode_petrel_v14",
    "PNF_V14_CONSTANTS",
    "DiveTimeSeries",
    "plot_timeseries",
]
