from __future__ import annotations

from importlib.metadata import entry_points
from typing import Dict, Mapping, Type

from .samplers.base import GraphSampler


_CACHE: Dict[str, Type[GraphSampler]] | None = None


def _load_entry_point_samplers() -> Mapping[str, Type[GraphSampler]]:
    eps = entry_points()
    group = eps.select(group="distributed_sampling.samplers")
    discovered: Dict[str, Type[GraphSampler]] = {}
    for ep in group:
        try:
            cls = ep.load()
        except Exception as exc:  # pragma: no cover - discovery errors at runtime
            raise RuntimeError(f"Failed to load sampler entry point '{ep.name}': {exc}") from exc
        if not isinstance(cls, type) or not issubclass(cls, GraphSampler):
            raise TypeError(
                f"Entry point '{ep.name}' must reference a GraphSampler subclass, got {cls!r}"
            )
        discovered[ep.name] = cls
    return discovered


def _ensure_cache() -> Dict[str, Type[GraphSampler]]:
    global _CACHE
    if _CACHE is None:
        _CACHE = dict(_load_entry_point_samplers())
    return _CACHE


def available_samplers() -> Mapping[str, Type[GraphSampler]]:
    """Return mapping of available sampler name -> class."""
    return _ensure_cache()


def get_sampler(name: str) -> Type[GraphSampler]:
    cache = _ensure_cache()
    try:
        return cache[name]
    except KeyError as exc:
        available = ", ".join(sorted(cache)) or "<none>"
        raise KeyError(f"Sampler '{name}' not found. Available: {available}") from exc


