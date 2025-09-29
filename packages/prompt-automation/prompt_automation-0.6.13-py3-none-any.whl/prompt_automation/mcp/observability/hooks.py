"""Simple observability toggles for MCP integrations."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

from ...features import is_mcp_observability_enabled


@dataclass(slots=True)
class ObservabilityState:
    metrics_enabled: bool = False
    tracing_enabled: bool = False
    logger: Optional[Callable[[str], None]] = None

    def log(self, message: str) -> None:
        if self.logger:
            self.logger(message)


def _default_logger(message: str) -> None:  # pragma: no cover - fallback logging only
    print(message)


def _initial_enabled() -> bool:
    try:
        return is_mcp_observability_enabled()
    except Exception:  # pragma: no cover - defensive
        return False


_DEFAULT_OBSERVABILITY = _initial_enabled()

global_state = ObservabilityState(
    metrics_enabled=_DEFAULT_OBSERVABILITY,
    tracing_enabled=_DEFAULT_OBSERVABILITY,
    logger=_default_logger,
)


def configure(metrics: Optional[bool] = None, tracing: Optional[bool] = None, logger: Optional[Callable[[str], None]] = None) -> None:
    """Update the observability state atomically."""

    if metrics is not None:
        global_state.metrics_enabled = metrics
    if tracing is not None:
        global_state.tracing_enabled = tracing
    if logger is not None:
        global_state.logger = logger


class ObservabilityToggle:
    """Context manager used to temporarily override observability."""

    def __init__(self, metrics: Optional[bool] = None, tracing: Optional[bool] = None) -> None:
        self.metrics = metrics
        self.tracing = tracing
        self._previous = ObservabilityState(
            metrics_enabled=global_state.metrics_enabled,
            tracing_enabled=global_state.tracing_enabled,
            logger=global_state.logger,
        )

    def __enter__(self) -> ObservabilityState:
        configure(metrics=self.metrics, tracing=self.tracing)
        return global_state

    def __exit__(self, exc_type, exc, tb) -> None:
        configure(
            metrics=self._previous.metrics_enabled,
            tracing=self._previous.tracing_enabled,
            logger=self._previous.logger,
        )


def sync_with_features() -> ObservabilityState:
    """Refresh the global observability state from feature resolution."""

    enabled = is_mcp_observability_enabled()
    configure(metrics=enabled, tracing=enabled)
    return global_state


sync_with_features()


__all__ = ["ObservabilityState", "ObservabilityToggle", "configure", "global_state", "sync_with_features"]


