from __future__ import annotations

from typing import Optional

from pyspark.sql import functions as F
from graphframes import GraphFrame

from .base import GraphSampler


class UVSNSampler(GraphSampler):
    """Uniform Vertex Sampling with Neighborhood.

    Sample a fraction (or number) of vertices uniformly, then include all their neighbors
    and return the induced subgraph.
    """

    name = "uvsn"

    def __init__(self, fraction: float = 0.1, num_vertices: Optional[int] = None, seed: Optional[int] = None) -> None:
        if num_vertices is None and not (0.0 < fraction <= 1.0):
            raise ValueError("fraction must be in (0, 1] when num_vertices is not provided")
        self.fraction = float(fraction)
        self.num_vertices = num_vertices
        self.seed = seed

    def sample(self, graph: GraphFrame) -> GraphFrame:
        v = graph.vertices
        e = graph.edges

        if self.num_vertices is not None:
            total = v.count()
            if total == 0:
                return GraphFrame(v.limit(0), e.limit(0))
            frac = min(1.0, max(1, self.num_vertices) / float(total))
            base = v.sample(False, frac, self.seed).limit(self.num_vertices)
        else:
            base = v.sample(False, self.fraction, self.seed)

        # Neighborhood: nodes adjacent via src or dst
        base_ids = base.select(F.col("id").alias("bid"))
        nbrs_out = e.join(base_ids, e["src"] == base_ids["bid"], "inner").select(F.col("dst").alias("id"))
        nbrs_in = e.join(base_ids, e["dst"] == base_ids["bid"], "inner").select(F.col("src").alias("id"))
        neighborhood = base.select("id").union(nbrs_out).union(nbrs_in).distinct()

        sampled_vertices = neighborhood.join(v, on="id", how="inner")

        sv = sampled_vertices.select(F.col("id").alias("vid"))
        edges_src = e.join(sv, e["src"] == sv["vid"], "inner").drop("vid")
        sv2 = sampled_vertices.select(F.col("id").alias("vid"))
        induced_edges = edges_src.join(sv2, edges_src["dst"] == sv2["vid"], "inner").drop("vid")

        return GraphFrame(sampled_vertices, induced_edges)


