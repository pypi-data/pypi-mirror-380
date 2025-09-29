from __future__ import annotations

from typing import Optional

from pyspark.sql import functions as F
from graphframes import GraphFrame

from .base import GraphSampler


class RandomEdgeSampler(GraphSampler):
    """Randomly sample a fraction of edges and keep their endpoint vertices.

    Parameters
    ----------
    fraction: float
        Fraction of edges to keep (0 < fraction <= 1.0). Ignored if num_edges is set.
    num_edges: Optional[int]
        If provided, approximate this many edges by sampling a fraction and limiting.
    seed: Optional[int]
        Random seed.
    """

    name = "random_edge"

    def __init__(
        self, fraction: float = 0.1, num_edges: Optional[int] = None, seed: Optional[int] = None
    ) -> None:
        if num_edges is None and not (0.0 < fraction <= 1.0):
            raise ValueError("fraction must be in (0, 1] when num_edges is not provided")
        self.fraction = float(fraction)
        self.num_edges = num_edges
        self.seed = seed

    def sample(self, graph: GraphFrame) -> GraphFrame:
        v = graph.vertices
        e = graph.edges

        if self.num_edges is not None:
            total = e.count()
            if total == 0:
                return GraphFrame(v.limit(0), e.limit(0))
            frac = min(1.0, max(1, self.num_edges) / float(total))
            sampled_edges = e.sample(False, frac, self.seed).limit(self.num_edges)
        else:
            sampled_edges = e.sample(False, self.fraction, self.seed)

        # Collect endpoint vertex ids and select corresponding vertices
        endpoints = (
            sampled_edges.select(F.col("src").alias("id"))
            .union(sampled_edges.select(F.col("dst").alias("id")))
            .distinct()
        )
        sampled_vertices = endpoints.join(v, on="id", how="inner")

        return GraphFrame(sampled_vertices, sampled_edges)


