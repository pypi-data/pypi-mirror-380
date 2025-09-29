from __future__ import annotations

from abc import ABC, abstractmethod

from graphframes import GraphFrame


class GraphSampler(ABC):
    """Base interface for graph samplers.

    Implementations should be stateless or hold only configuration passed at init.
    """

    name: str | None = None

    @abstractmethod
    def sample(self, graph: GraphFrame) -> GraphFrame:  # pragma: no cover - interface
        """Return a sampled GraphFrame given the input GraphFrame."""
        raise NotImplementedError


