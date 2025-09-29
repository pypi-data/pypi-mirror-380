from __future__ import annotations

from typing import Optional

from pyspark.sql import functions as F
from graphframes import GraphFrame

from .base import GraphSampler


class MDRWSampler(GraphSampler):
    """Multi-Dimensional Random Walk (approximated as simple random walk with attribute bias).

    If vertex column `attr` is provided, bias transition by attr weight; else behaves like RW.
    """

    name = "mdrw"

    def __init__(self, walk_length: int = 10, num_walks: int = 10, attr: Optional[str] = None, seed: Optional[int] = None) -> None:
        if walk_length <= 0:
            raise ValueError("walk_length must be > 0")
        if num_walks <= 0:
            raise ValueError("num_walks must be > 0")
        self.walk_length = int(walk_length)
        self.num_walks = int(num_walks)
        self.attr = attr
        self.seed = seed

    def sample(self, graph: GraphFrame) -> GraphFrame:
        v = graph.vertices
        e = graph.edges

        starts = v.orderBy(F.rand(self.seed)).limit(self.num_walks).select(F.col("id").alias("curr"))
        visited = starts.select(F.col("curr").alias("id")).distinct()
        frontier = starts

        for step in range(self.walk_length):
            out_edges = frontier.join(e, frontier["curr"] == e["src"], "left")
            if self.attr and self.attr in v.columns:
                # Join destination attribute as weight and sample by rand^(1/w)
                dst_attr = out_edges.join(v.select(F.col("id").alias("vid"), F.col(self.attr).alias("w")), out_edges["dst"] == F.col("vid"), "left")
                scored = dst_attr.withColumn("score", -F.log(F.rand(self.seed + step if self.seed else None)) / F.when(F.col("w") > 0, F.col("w")).otherwise(1.0))
                pick = scored.groupBy("curr").agg(F.first(F.struct("score", "dst")).alias("picked"))
            else:
                cand = out_edges.withColumn("rand", F.rand(self.seed + step if self.seed else None))
                pick = cand.groupBy("curr").agg(F.first(F.struct("rand", "dst")).alias("picked"))

            new_frontier = pick.select(F.col("picked.dst").alias("curr"))
            if new_frontier.rdd.isEmpty():
                break
            visited = visited.union(new_frontier.select(F.col("curr").alias("id"))).distinct()
            frontier = new_frontier

        sampled_vertices = visited.join(v, on="id", how="inner")
        sv = sampled_vertices.select(F.col("id").alias("vid"))
        edges_src = e.join(sv, e["src"] == sv["vid"], "inner").drop("vid")
        sv2 = sampled_vertices.select(F.col("id").alias("vid"))
        induced_edges = edges_src.join(sv2, edges_src["dst"] == sv2["vid"], "inner").drop("vid")
        return GraphFrame(sampled_vertices, induced_edges)


