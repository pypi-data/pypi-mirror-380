from __future__ import annotations

from typing import Optional

from pyspark.sql import functions as F
from graphframes import GraphFrame

from .base import GraphSampler


class RandomNodeSampler(GraphSampler):
    """Randomly sample a fraction of vertices and return the induced subgraph.

    Parameters
    ----------
    fraction: float
        Fraction of vertices to keep (0 < fraction <= 1.0).
    seed: Optional[int]
        Random seed for reproducibility.
    """

    name = "random_node"

    def __init__(self, fraction: float = 0.1, seed: Optional[int] = None) -> None:
        if not (0.0 < fraction <= 1.0):
            raise ValueError("fraction must be in (0, 1]")
        self.fraction = float(fraction)
        self.seed = seed

    def sample(self, graph: GraphFrame) -> GraphFrame:
        v = graph.vertices
        e = graph.edges

        sampled_vertices = v.sample(withReplacement=False, fraction=self.fraction, seed=self.seed)

        # Keep edges where both endpoints are in the sampled vertex set (induced subgraph)
        sv = sampled_vertices.select(F.col("id").alias("vid"))
        edges_src = e.join(sv, e["src"] == sv["vid"], "inner").drop("vid")
        sv2 = sampled_vertices.select(F.col("id").alias("vid"))
        induced_edges = edges_src.join(sv2, edges_src["dst"] == sv2["vid"], "inner").drop("vid")

        return GraphFrame(sampled_vertices, induced_edges)


