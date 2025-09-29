from __future__ import annotations

from typing import Literal

from pyspark.sql import functions as F
from graphframes import GraphFrame

from .base import GraphSampler


class TopKSampler(GraphSampler):
    """Select top-K vertices by degree (in/out/total) and induced subgraph.

    Parameters
    ----------
    k: int
        Number of vertices to keep.
    by: Literal["in", "out", "total"]
        Which degree to rank by.
    """

    name = "topk"

    def __init__(self, k: int = 100, by: Literal["in", "out", "total"] = "total") -> None:
        if k <= 0:
            raise ValueError("k must be > 0")
        if by not in ("in", "out", "total"):
            raise ValueError("by must be one of 'in', 'out', 'total'")
        self.k = int(k)
        self.by = by

    def sample(self, graph: GraphFrame) -> GraphFrame:
        v = graph.vertices
        e = graph.edges

        indeg = e.groupBy("dst").count().withColumnRenamed("dst", "id").withColumnRenamed("count", "in")
        outdeg = e.groupBy("src").count().withColumnRenamed("src", "id").withColumnRenamed("count", "out")

        degrees = v.select("id").join(indeg, on="id", how="left").join(outdeg, on="id", how="left")
        degrees = degrees.fillna(0, subset=["in", "out"]).withColumn("total", F.col("in") + F.col("out"))

        top = degrees.orderBy(F.col(self.by).desc()).limit(self.k).select("id")
        sampled_vertices = top.join(v, on="id", how="inner")

        # Induced edges among top vertices
        sv = sampled_vertices.select(F.col("id").alias("vid"))
        edges_src = e.join(sv, e["src"] == sv["vid"], "inner").drop("vid")
        sv2 = sampled_vertices.select(F.col("id").alias("vid"))
        induced_edges = edges_src.join(sv2, edges_src["dst"] == sv2["vid"], "inner").drop("vid")

        return GraphFrame(sampled_vertices, induced_edges)


