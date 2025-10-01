"""Domain models used by the dive log client."""

from __future__ import annotations
import pandas as pd
import numpy as np
from dataclasses import dataclass, field
import math
from datetime import datetime
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Sequence, Tuple, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - type hints only
    from .timeseries import DiveTimeSeries


class UnitMeasure:
    """Wrap a numeric value with unit conversion helpers."""

    _CONVERSIONS = {
        ("F", "C"): lambda value: (value - 32.0) * 5.0 / 9.0,
        ("C", "F"): lambda value: value * 9.0 / 5.0 + 32.0,
    }

    def __init__(self, value: float | None, unit: str) -> None:
        self._value = value
        self._unit = unit.upper() if unit else unit

    @property
    def value(self) -> float | None:
        return self._value

    @property
    def unit(self) -> str:
        return self._unit

    @property
    def available_units(self) -> Sequence[str]:
        units = set()
        if self._unit:
            units.add(self._unit)
        for base, target in self._CONVERSIONS:
            units.add(base)
            units.add(target)
        return sorted(u for u in units if u)

    def as_unit(self, target_unit: str) -> float | None:
        """Return the value converted to *target_unit* (if possible)."""
        if self._value is None:
            return None
        target = target_unit.upper()
        if target == self._unit:
            return self._value
        key = (self._unit, target)
        if key not in self._CONVERSIONS:
            raise ValueError(f"Unsupported conversion {self._unit} -> {target}")
        return self._CONVERSIONS[key](self._value)

    def convert(self, target_unit: str) -> "UnitMeasure":
        """Return a new :class:`UnitMeasure` in the requested unit."""
        return UnitMeasure(self.as_unit(target_unit), target_unit)

    def __repr__(self) -> str:  # pragma: no cover - convenience only
        return f"UnitMeasure(value={self._value!r}, unit='{self._unit}')"


@dataclass(frozen=True)
class SensorSeries:
    """PO₂ sensor samples for a single sensor."""

    sensor_index: int
    timeseries: Sequence[Tuple[float, float]]  # (seconds offset, value)

    def as_dataframe(self):  # pragma: no cover - convenience for notebooks
        import pandas as pd

        return pd.DataFrame(self.timeseries, columns=["seconds", "value"])

    def to_df(self):  # pragma: no cover - convenience alias
        return self.as_dataframe()

    def _despiked(self, *, threshold: float = 0.5) -> "SensorSeries":
        """Return a new series with isolated spikes replaced by neighbouring average."""

        if not self.timeseries or len(self.timeseries) < 3:
            return SensorSeries(self.sensor_index, tuple(self.timeseries))

        cleaned: List[Tuple[float, float]] = []
        total = len(self.timeseries)
        for idx, (sec, value) in enumerate(self.timeseries):
            if 0 < idx < total - 1:
                prev = self.timeseries[idx - 1][1]
                nxt = self.timeseries[idx + 1][1]
                if (
                    abs(value - prev) > threshold
                    and abs(value - nxt) > threshold
                    and abs(prev - nxt) <= threshold
                ):
                    value = (prev + nxt) / 2.0
            cleaned.append((sec, value))

        return SensorSeries(self.sensor_index, tuple(cleaned))



    @staticmethod
    def _mad_sigma(x, center, win, c=1.4826):
        # Rolling MAD scaled to sigma
        mad = (x - center).abs().rolling(win, center=True, min_periods=1).median()
        return c * mad

    @staticmethod
    def _find_short_outlier_runs(is_outlier: pd.Series, seconds: pd.Series, max_duration: int):
        """
        Return a boolean mask marking only the outlier samples that belong to
        contiguous outlier runs whose duration <= max_duration seconds.
        Contiguity is defined by consecutive seconds (diff == 1).
        """
        mask = pd.Series(False, index=is_outlier.index)
        n = len(is_outlier)
        i = 0
        while i < n:
            if not is_outlier.iat[i]:
                i += 1
                continue
            start_i = i
            start_t = seconds.iat[i]
            i += 1
            # advance while still outlier and seconds are consecutive
            while i < n and is_outlier.iat[i] and (seconds.iat[i] - seconds.iat[i-1] == 1):
                i += 1
            end_i = i - 1
            end_t = seconds.iat[end_i]
            duration = end_t - start_t + 1
            if duration <= max_duration:
                mask.iloc[start_i:end_i+1] = True
        return mask

    def despiked(
            self, *,
            threshold: float = 0.5,    # spike detection threshold
            max_duration: int = 10,     # seconds
            win: int = 21,              # rolling window in samples (≈ seconds if per-sec)
            k: float = 3.5,             # outlier threshold in MAD-sigmas
            fill_strategy: str = "ffill"  # "ffill" or "median"
    ):
        df = self._despiked(threshold=threshold).to_df()

        # Ensure proper types & sort
        gdf = df[['seconds', 'value']].copy()
        gdf['seconds'] = gdf['seconds'].astype(int)
        
        gdf = gdf.sort_values(['seconds'])

        cleaned_chunks = []
        s = gdf['value'].astype(float).reset_index(drop=True)
        t = gdf['seconds'].reset_index(drop=True)

        # Robust center & scale
        med = s.rolling(win, center=True, min_periods=1).median()
        sigma = self._mad_sigma(s, med, win)

        # Outlier mask vs rolling median
        is_out = (s - med).abs() > (k * sigma)

        # Only suppress short outlier runs (<= max_duration)
        short_run_mask = self._find_short_outlier_runs(is_out, t, max_duration)

        # Replace short-run outliers with previous good value (or median)
        s_clean = s.copy()
        if fill_strategy == "ffill":
            tmp = s_clean.mask(short_run_mask, np.nan)
            # forward-fill from last good sample; if at start, fall back to median
            s_clean = tmp.ffill().fillna(med)
        else:
            s_clean = s_clean.where(~short_run_mask, med)

        out = pd.DataFrame({'seconds': t, 'value': s_clean})
        cleaned_chunks.append(out)

        cleaned_long = pd.concat(cleaned_chunks, ignore_index=True)
        # wide = cleaned_long.pivot(index='seconds',  values='value').sort_index()
        # wide.columns.name = None
        return SensorSeries(self.sensor_index, list(cleaned_long.itertuples(index=False, name=None)))


class SensorCollection(Sequence[SensorSeries]):
    """Thin wrapper that offers helpers across all sensor series."""

    def __init__(self, series: Iterable[SensorSeries]):
        self._series: List[SensorSeries] = list(series)

    def __getitem__(self, index):
        return self._series[index]

    def __len__(self) -> int:
        return len(self._series)

    def __iter__(self) -> Iterator[SensorSeries]:  # pragma: no cover - trivial
        return iter(self._series)

    def to_df(self):  # pragma: no cover - convenience only
        import pandas as pd

        frames = []
        for series in self._series:
            df = series.as_dataframe()
            df["sensor_index"] = series.sensor_index
            frames.append(df)
        if not frames:
            df = pd.DataFrame(columns=["seconds", "value", "sensor_index"])
            return df.pivot(index='seconds', columns='sensor_index', values='value').sort_index()
        return pd.concat(frames, ignore_index=True).pivot(index='seconds', columns='sensor_index', values='value').sort_index()

    def despiked(self, *, threshold: float = 0.5) -> "SensorCollection":
        return SensorCollection(series.despiked(threshold=threshold) for series in self._series)


@dataclass(frozen=True)
class AirIntegrationSeries:
    """Metadata and samples for a wireless air-integration transmitter."""

    name: str
    tank_index: int | None
    start_pressure_psi: float | None
    end_pressure_psi: float | None
    samples: Tuple[Tuple[float, float], ...] = field(default_factory=tuple)
    default_script_term: str | None = None
    transmitter_serial: str | None = None
    is_enabled: bool | None = None
    gas_profile: Mapping[str, Any] | None = None
    sensor_field: str | None = None

    @property
    def pressure_drop_psi(self) -> float | None:
        if self.start_pressure_psi is None or self.end_pressure_psi is None:
            return None
        return self.start_pressure_psi - self.end_pressure_psi

    @property
    def sample_count(self) -> int:
        return len(self.samples)

    @property
    def start_time_seconds(self) -> float | None:
        return self.samples[0][0] if self.samples else None

    @property
    def end_time_seconds(self) -> float | None:
        return self.samples[-1][0] if self.samples else None

    def to_dataframe(self):  # pragma: no cover - convenience helper
        import pandas as pd

        if not self.samples:
            return pd.DataFrame(columns=["seconds", "pressure_psi"])
        return pd.DataFrame(self.samples, columns=["seconds", "pressure_psi"]).set_index("seconds")


@dataclass(frozen=True)
class DivePayload:
    """Container for raw computer payloads and decoded helpers."""

    data_bytes_1: bytes | None = None
    decompressed_bytes_1: bytes | None = None
    floats_1: Sequence[float] = field(default_factory=tuple)
    frames_1: Sequence[Tuple[float, ...]] = field(default_factory=tuple)
    samples: Sequence[Dict[str, Any]] = field(default_factory=tuple)
    sample_records_raw: Sequence[bytes] = field(default_factory=tuple)
    data_bytes_2: Dict[str, Any] = field(default_factory=dict)
    data_bytes_3: Dict[str, Any] = field(default_factory=dict)
    timeseries: "DiveTimeSeries" | None = None


@dataclass(frozen=True)
class Dive:
    """A dive event aggregated across matching computers."""

    dive_id: str
    computer_name: str
    start: datetime | None
    end: datetime | None
    duration_seconds: float | None
    mode: str
    temp: UnitMeasure
     
    max_depth: float | None
    computer_names: Sequence[str]
    sensors: SensorCollection = field(default_factory=lambda: SensorCollection([]))
    payload: DivePayload | None = None
    primary_computer: "Dive" | None = None
    controller: "Dive" | None = None
    monitor: "Dive" | None = None
    secondary_computer: "Dive" | None = None
    gas_profiles: Sequence[Dict[str, Any]] = field(default_factory=tuple)
    tank_data: Sequence[Dict[str, Any]] = field(default_factory=tuple)
    linked_dives: Tuple["Dive", ...] = field(default_factory=tuple)

    def __repr__(self) -> str:  # pragma: no cover - convenience only
        primary = self._link_label(self.primary_computer)
        return (
            "Dive("
            f"id={self.dive_id!r}, mode={self.mode!r}, start={self.start}, duration_seconds={self.duration_seconds}, "
            f"primary={primary!r}, computers={list(self.computer_names)}"
            ")"
        )

    def display_name(self) -> str:
        """Return a friendly label for the dive's computer."""

        return self.computer_name 

    @property
    def timeseries(self) -> "DiveTimeSeries | None":
        if self.payload:
            return self.payload.timeseries
        return None

    @property
    def air_integration(self) -> Tuple[AirIntegrationSeries, ...]:
        if not self.tank_data:
            return tuple()
        samples = self.payload.samples if (self.payload and self.payload.samples) else ()
        return _build_air_integration_entries(self.tank_data, samples)

    @staticmethod
    def _link_label(link: "Dive" | None) -> str | None:
        if isinstance(link, Dive):
            return link.display_name()
        if isinstance(link, str):  # backwards compatibility
            return link
        return None

    @property
    def primary_label(self) -> str | None:
        return self._link_label(self.primary_computer)

    @property
    def primary_computer_name(self) -> str | None:
        return self.primary_label

    @property
    def controller_label(self) -> str | None:
        return self._link_label(self.controller)

    @property
    def controller_name(self) -> str | None:
        return self.controller_label

    @property
    def monitor_label(self) -> str | None:
        return self._link_label(self.monitor)

    @property
    def monitor_name(self) -> str | None:
        return self.monitor_label

    @property
    def secondary_label(self) -> str | None:
        return self._link_label(self.secondary_computer)

    @property
    def secondary_computer_name(self) -> str | None:
        return self.secondary_label


_TANK_INDEX_CANDIDATE_FIELDS: Dict[int, Tuple[str, ...]] = {
    0: ("wai_sensor0_pressure",),
    1: ("wai_sensor1_pressure",),
    2: ("wai_sensor2_pressure",),
    3: ("wai_sensor3_pressure",),
}

_SENTINEL_PRESSURES = {0, 65535, 65534}

_PRESSURE_FIELD_SCALE: Dict[str, float] = {
    "wai_sensor0_pressure": 2.0,
    "wai_sensor1_pressure": 2.0,
    "wai_sensor2_pressure": 2.0,
    "wai_sensor3_pressure": 2.0,
}


def _select_first_available_field(
    samples: Sequence[Dict[str, Any]] | None,
    candidates: Sequence[str],
) -> str | None:
    if not candidates:
        return None
    if not samples:
        return candidates[0]

    for field in candidates:
        for sample in samples:
            value = _retrieve_sample_value(sample, field)
            if value not in (None, 0, 65535, 65534):
                return field
    return candidates[0]


def _build_air_integration_entries(
    tank_entries: Sequence[Dict[str, Any]],
    samples: Sequence[Dict[str, Any]] | None,
) -> Tuple[AirIntegrationSeries, ...]:
    selected = _select_tank_entries(tank_entries)
    if not selected:
        return tuple()

    sample_series_cache: Dict[str, Tuple[Tuple[float, float], ...]] = {}
    results: List[AirIntegrationSeries] = []

    for entry in selected:
        transmitter = entry.get("DiveTransmitter") or {}
        tank_index = transmitter.get("TankIndex")
        candidates = _TANK_INDEX_CANDIDATE_FIELDS.get(tank_index, tuple())
        sensor_field = _select_first_available_field(samples, candidates)
        if sensor_field is None:
            continue
        if sensor_field not in sample_series_cache:
            sample_series_cache[sensor_field] = _extract_pressure_series(samples, sensor_field)
        series = sample_series_cache[sensor_field]

        results.append(
            AirIntegrationSeries(
                name=_resolve_transmitter_name(transmitter, tank_index),
                tank_index=tank_index,
                start_pressure_psi=_coerce_pressure(entry.get("StartPressurePSI")),
                end_pressure_psi=_coerce_pressure(entry.get("EndPressurePSI")),
                samples=series,
                default_script_term=transmitter.get("DefaultScriptTerm"),
                transmitter_serial=transmitter.get("UnformattedSerialNumber"),
                is_enabled=transmitter.get("IsOn"),
                gas_profile=entry.get("GasProfile"),
                sensor_field=sensor_field,
            )
        )

    results.sort(key=lambda item: (item.tank_index if item.tank_index is not None else 99))
    return tuple(results)


def _select_tank_entries(tank_entries: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    best: Dict[Any, Dict[str, Any]] = {}
    for entry in tank_entries or []:
        transmitter = entry.get("DiveTransmitter") or {}
        if not transmitter.get("IsOn"):
            continue
        key = transmitter.get("TankIndex")
        if key is None:
            script_term = transmitter.get("DefaultScriptTerm")
            if not script_term:
                continue
            key = script_term

        current = best.get(key)
        if current is None or _entry_score(entry) > _entry_score(current):
            best[key] = entry

    ordered_keys = sorted(best.keys(), key=lambda value: value if isinstance(value, int) else 99)
    return [best[key] for key in ordered_keys]


def _entry_score(entry: Dict[str, Any]) -> Tuple[int, int, int]:
    transmitter = entry.get("DiveTransmitter") or {}
    is_on = 1 if transmitter.get("IsOn") else 0
    start = 1 if _coerce_pressure(entry.get("StartPressurePSI")) is not None else 0
    end = 1 if _coerce_pressure(entry.get("EndPressurePSI")) is not None else 0
    return (is_on, start, end)


def _resolve_transmitter_name(transmitter: Dict[str, Any], tank_index: int | None) -> str:
    name = transmitter.get("Name") if isinstance(transmitter, dict) else None
    if isinstance(name, str):
        cleaned = name.replace("\x00", "").strip()
        if cleaned:
            return cleaned
    if tank_index is not None:
        return f"Tank {tank_index + 1}"
    term = transmitter.get("DefaultScriptTerm") if isinstance(transmitter, dict) else None
    if isinstance(term, str) and term:
        return term.rsplit("/", 1)[-1]
    return "Unknown Tank"


def _coerce_pressure(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        if isinstance(value, float) and math.isnan(value):
            return None
        if value in _SENTINEL_PRESSURES:
            return None
        return float(value)
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return None
        try:
            numeric = float(stripped)
        except ValueError:
            return None
        if numeric in _SENTINEL_PRESSURES:
            return None
        return numeric
    return None


def _extract_pressure_series(
    samples: Sequence[Dict[str, Any]] | None,
    field: str,
) -> Tuple[Tuple[float, float], ...]:
    if not samples:
        return tuple()

    series: List[Tuple[float, float]] = []
    for sample in samples:
        raw_value = _retrieve_sample_value(sample, field)
        pressure = _coerce_pressure(raw_value)
        if pressure is not None:
            pressure *= _PRESSURE_FIELD_SCALE.get(field, 1.0)
        if pressure is None:
            continue
        time_value = sample.get("time_seconds")
        if isinstance(time_value, (int, float)):
            series.append((float(time_value), pressure))

    return tuple(series)


def _retrieve_sample_value(sample: Dict[str, Any], field: str) -> Any:
    return sample.get(field)


def build_tank_alias_map(
    tank_entries: Sequence[Dict[str, Any]] | None,
) -> Tuple[Dict[str, Tuple[str, str]], Tuple[Tuple[str, str], ...]]:
    """Return alias lookups for active wireless transmitters."""

    alias_map: Dict[str, Tuple[str, str]] = {}
    display_order: List[Tuple[str, str]] = []
    seen_fields: set[str] = set()

    for entry in tank_entries or []:
        transmitter = entry.get("DiveTransmitter") or {}
        if not transmitter.get("IsOn"):
            continue

        index = transmitter.get("TankIndex")
        sensor_field = _select_first_available_field(None, _TANK_INDEX_CANDIDATE_FIELDS.get(index, tuple()))
        if sensor_field is None:
            continue

        display_name = _resolve_transmitter_name(transmitter, index)
        if sensor_field not in seen_fields:
            display_order.append((display_name, sensor_field))
            seen_fields.add(sensor_field)

        for alias in _iter_tank_aliases(transmitter, index, display_name):
            normalized = alias.strip().lower()
            if normalized:
                alias_map[normalized] = (sensor_field, display_name)

    return alias_map, tuple(display_order)


def _iter_tank_aliases(transmitter: Dict[str, Any], index: int | None, display_name: str) -> Iterable[str]:
    aliases = set()

    if isinstance(display_name, str) and display_name:
        aliases.add(display_name)

    name = transmitter.get("Name") if isinstance(transmitter, dict) else None
    if isinstance(name, str):
        aliases.add(name.replace("\x00", ""))

    if index is not None:
        aliases.add(f"tank{index + 1}")
        aliases.add(f"tank_{index + 1}")

    script_term = transmitter.get("DefaultScriptTerm")
    if isinstance(script_term, str) and script_term:
        aliases.add(script_term)
        aliases.add(script_term.rsplit("/", 1)[-1])

    serial = transmitter.get("UnformattedSerialNumber")
    if serial is not None:
        aliases.add(str(serial))

    return aliases
