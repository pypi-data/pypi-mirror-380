from __future__ import annotations

from typing import Iterable, Optional

from pyspark.sql import functions as F
from graphframes import GraphFrame

from .base import GraphSampler


class RWESampler(GraphSampler):
    """Random Walk with Escaping (restart to seeds with probability alpha)."""

    name = "rwe"

    def __init__(
        self,
        walk_length: int = 100,
        num_walks: int = 10,
        start_nodes: Optional[Iterable[str]] = None,
        alpha: float = 0.15,
        seed: Optional[int] = None,
    ) -> None:
        if not (0.0 <= alpha <= 1.0):
            raise ValueError("alpha must be in [0,1]")
        self.walk_length = int(walk_length)
        self.num_walks = int(num_walks)
        self.start_nodes = list(start_nodes) if start_nodes is not None else None
        self.alpha = float(alpha)
        self.seed = seed

    def sample(self, graph: GraphFrame) -> GraphFrame:
        v = graph.vertices
        e = graph.edges

        if self.start_nodes is not None:
            starts = v.join(F.broadcast(F.createDataFrame([(s,) for s in self.start_nodes], ["id"])), on="id", how="inner").select(F.col("id").alias("curr"))
        else:
            starts = v.orderBy(F.rand(self.seed)).limit(self.num_walks).select(F.col("id").alias("curr"))

        visited = starts.select(F.col("curr").alias("id")).distinct()
        frontier = starts

        for step in range(self.walk_length):
            # Decide to restart or continue
            do_restart = F.rand(self.seed + 2000 + step if self.seed else None) < F.lit(self.alpha)

            # Restart positions
            restart_frontier = v.orderBy(F.rand(self.seed + 3000 + step if self.seed else None)).limit(self.num_walks).select(F.col("id").alias("curr")) if self.start_nodes is None else starts

            # Continue random step for those not restarting
            out_edges = frontier.join(e, frontier["curr"] == e["src"], "left")
            cand = out_edges.withColumn("rand", F.rand(self.seed + step if self.seed else None))
            next_edge = cand.groupBy("curr").agg(F.first(F.struct("rand", "dst")).alias("picked"))
            cont_frontier = next_edge.select(F.col("picked.dst").alias("curr"))

            # Mix restart and continue by union; approximate partition
            new_frontier = cont_frontier.union(restart_frontier).distinct()
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


