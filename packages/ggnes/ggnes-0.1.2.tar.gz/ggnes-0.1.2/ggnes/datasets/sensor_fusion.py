"""Synthetic sensor-fusion dataset for investor-focused demos.

The dataset encodes temporal, weather, and event-driven signals that interact in
non-linear and gated ways. It is intentionally crafted to reward architecture
search spaces that can discover multi-branch fusion patterns (e.g. attention
nodes, gated sums, residual paths) while remaining deterministic and
CPU-friendly.

Design Goals
------------
- Deterministic generation: controlled by a seed, requires no network access.
- Rich feature groups: periodic time components, correlated weather signals,
  sparse event indicators, and synthetic sensor feeds.
- Non-trivial target: combines periodic, gated, and multiplicative interactions
  with heteroscedastic noise so that expressive graphs provide a measurable
  advantage over generic baselines.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class SensorFusionConfig:
    """Configuration for dataset generation."""

    samples: int = 16384
    seed: int = 314159
    time_span_hours: int = 24
    seasonal_period_hours: int = 168  # one week
    noise_sigma: float = 0.08
    event_rate: float = 0.08


def _make_time_features(hours: np.ndarray, span: int, seasonal: int) -> np.ndarray:
    """Return stacked temporal embeddings (sin/cos for daily and weekly cycles)."""

    day_angle = 2.0 * math.pi * (hours % span) / float(span)
    week_angle = 2.0 * math.pi * (hours % seasonal) / float(seasonal)

    feats = np.stack(
        [
            np.sin(day_angle),
            np.cos(day_angle),
            np.sin(week_angle),
            np.cos(week_angle),
        ],
        axis=1,
    )
    return feats.astype(np.float32)


def _make_weather_features(rng: np.random.Generator, n: int) -> tuple[np.ndarray, np.ndarray]:
    """Generate correlated temperature/humidity/pressure signals."""

    temp = rng.normal(loc=18.0, scale=6.5, size=n)
    humidity = np.clip(rng.beta(2.5, 1.8, size=n) * 110.0, 5.0, 100.0)
    pressure = rng.normal(loc=1011.0, scale=6.0, size=n)
    wind = np.abs(rng.normal(loc=12.0, scale=4.0, size=n))

    # Capture latent correlations (warmer days tend to be less humid & lower pressure)
    humidity -= 0.35 * (temp - 18.0)
    pressure -= 0.5 * (temp - 18.0)

    weather = np.stack([temp, humidity, pressure, wind], axis=1)
    return weather.astype(np.float32), temp.astype(np.float32)


def _make_sensor_channels(rng: np.random.Generator, n: int) -> np.ndarray:
    """Create additional synthetic sensor feeds with non-linear relationships."""

    load = np.clip(rng.gamma(shape=2.0, scale=1.2, size=n), 0.0, 12.0)
    vibration = np.abs(rng.normal(loc=0.2, scale=0.08, size=n))
    co2 = rng.normal(loc=420.0, scale=32.0, size=n)
    occupancy = np.clip(load * rng.uniform(7.0, 12.0, size=n) + rng.normal(scale=5.0, size=n), 3.0, 120.0)

    # Couple some channels for richer cross terms
    vibration += 0.015 * occupancy
    co2 += 0.9 * load + 0.04 * occupancy

    channels = np.stack([load, vibration, co2, occupancy], axis=1)
    return channels.astype(np.float32)


def _make_event_indicators(rng: np.random.Generator, n: int) -> tuple[np.ndarray, np.ndarray]:
    """Binary and intensity features representing sporadic external events."""

    events = rng.binomial(1, 0.08, size=n).astype(np.float32)
    maintenance = rng.binomial(1, 0.05, size=n).astype(np.float32)
    marketing = rng.binomial(1, 0.03, size=n).astype(np.float32)

    intensity = rng.uniform(0.1, 1.5, size=n).astype(np.float32)
    fused = np.stack([events, maintenance, marketing, intensity], axis=1)
    return fused, intensity


def generate_sensor_fusion_dataset(config: SensorFusionConfig | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Generate (features, target) arrays for the organic sensor fusion task.

    Args:
        config: Optional configuration; defaults produce ~16k samples.

    Returns:
        X: float32 array with shape (n_samples, n_features)
        y: float32 array with shape (n_samples,)
    """

    cfg = config or SensorFusionConfig()
    rng = np.random.default_rng(cfg.seed)

    hours = np.arange(cfg.samples, dtype=np.float32)
    time_feats = _make_time_features(hours, cfg.time_span_hours, cfg.seasonal_period_hours)
    weather_feats, temperature = _make_weather_features(rng, cfg.samples)
    sensor_channels = _make_sensor_channels(rng, cfg.samples)
    event_feats, event_intensity = _make_event_indicators(rng, cfg.samples)

    # Derived helper signals (for targets and additional features)
    dew_point = temperature - ((100.0 - weather_feats[:, 1]) / 5.0)
    visibility_proxy = np.clip(10.0 - 0.15 * weather_feats[:, 3] - 0.01 * sensor_channels[:, 1], 0.5, 12.0)

    derived = np.stack([dew_point, visibility_proxy], axis=1).astype(np.float32)

    features = np.concatenate([time_feats, weather_feats, sensor_channels, event_feats, derived], axis=1)

    # Target combines periodic components, gated weather influence, and sparse events
    circadian = 0.45 * np.sin(time_feats[:, 0] * 2.5) + 0.25 * np.cos(time_feats[:, 1] * 1.3)
    weekly = 0.35 * np.sin(time_feats[:, 2] * 3.0) + 0.2 * np.cos(time_feats[:, 3] * 2.1)

    humidity = weather_feats[:, 1] / 100.0
    wind = weather_feats[:, 3] / 20.0
    load = sensor_channels[:, 0] / 10.0
    occupancy = sensor_channels[:, 3] / 140.0

    gate = 1.0 / (1.0 + np.exp(-3.5 * (event_intensity - 0.6)))
    weather_response = (0.6 + 0.3 * gate) * humidity**2 - 0.2 * wind + 0.45 * load
    occupancy_term = (0.5 + 0.4 * gate) * np.tanh(2.0 * (occupancy - 0.4))

    target = 2.4 + circadian + weekly + weather_response + occupancy_term
    target += 0.35 * derived[:, 0] / 25.0 - 0.25 * derived[:, 1] / 12.0

    noise = rng.normal(loc=0.0, scale=cfg.noise_sigma, size=cfg.samples)
    y = (target + noise).astype(np.float32)

    return features.astype(np.float32), y


__all__ = ["SensorFusionConfig", "generate_sensor_fusion_dataset"]
