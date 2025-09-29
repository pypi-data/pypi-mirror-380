from __future__ import annotations

from typing import Optional

from pyspark.sql import functions as F
from graphframes import GraphFrame

from .base import GraphSampler


class NUVSNSampler(GraphSampler):
    """Non-uniform Vertex Sampling with Neighborhood.

    Sample vertices with probability proportional to degree, include neighbors, and return
    induced subgraph.
    """

    name = "nuvsn"

    def __init__(self, fraction: float = 0.1, num_vertices: Optional[int] = None, seed: Optional[int] = None) -> None:
        if num_vertices is None and not (0.0 < fraction <= 1.0):
            raise ValueError("fraction must be in (0, 1] when num_vertices is not provided")
        self.fraction = float(fraction)
        self.num_vertices = num_vertices
        self.seed = seed

    def sample(self, graph: GraphFrame) -> GraphFrame:
        v = graph.vertices
        e = graph.edges

        # Use total degree as weight
        indeg = e.groupBy("dst").count().withColumnRenamed("dst", "id").withColumnRenamed("count", "in")
        outdeg = e.groupBy("src").count().withColumnRenamed("src", "id").withColumnRenamed("count", "out")
        deg = v.select("id").join(indeg, on="id", how="left").join(outdeg, on="id", how="left").fillna(0, ["in", "out"]).withColumn("w", F.col("in") + F.col("out"))

        # Weighted sampling: approximate via sorting by rand^(1/w)
        # Gumbel-top-k trick surrogate: -log(rand)/w; smaller is better
        rand = F.rand(self.seed)
        scored = deg.withColumn("score", -F.log(rand) / F.when(F.col("w") > 0, F.col("w")).otherwise(1.0))

        if self.num_vertices is not None:
            base = scored.orderBy("score").limit(self.num_vertices).select("id")
        else:
            # Approximate fraction by taking top fraction of scores
            # Use window-free approach: filter by quantile approx via percentile_approx
            quant = scored.approxQuantile("score", [self.fraction], 0.01)[0]
            base = scored.where(F.col("score") <= quant).select("id")

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


