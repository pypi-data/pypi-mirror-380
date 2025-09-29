from __future__ import annotations

from typing import Iterable, Optional

from pyspark.sql import functions as F
from graphframes import GraphFrame

from .base import GraphSampler


class DFSSampler(GraphSampler):
    """Depth-First Search sampling (approximate via greedy next-neighbor choice).

    DFS order is approximated by iteratively following one neighbor until dead-end,
    then picking another from last frontier; implemented with DataFrame operations.
    """

    name = "dfs"

    def __init__(
        self, seeds: Optional[Iterable[str]] = None, num_seeds: int = 1, max_steps: int = 100
    ) -> None:
        if num_seeds <= 0:
            raise ValueError("num_seeds must be > 0")
        if max_steps <= 0:
            raise ValueError("max_steps must be > 0")
        self.seeds = list(seeds) if seeds is not None else None
        self.num_seeds = int(num_seeds)
        self.max_steps = int(max_steps)

    def sample(self, graph: GraphFrame) -> GraphFrame:
        v = graph.vertices
        e = graph.edges

        if self.seeds is not None:
            frontier = v.join(
                F.broadcast(F.createDataFrame([(s,) for s in self.seeds], ["id"])),
                on="id",
                how="inner",
            ).select(F.col("id").alias("curr"))
        else:
            frontier = v.orderBy(F.rand()).limit(self.num_seeds).select(F.col("id").alias("curr"))

        visited = frontier.select(F.col("curr").alias("id")).distinct()

        steps = 0
        while steps < self.max_steps:
            # Prefer neighbors that are not visited; pick one per current node
            out_edges = frontier.join(e, frontier["curr"] == e["src"], "left")
            # Left-anti join to exclude visited
            candidates = out_edges.join(visited, out_edges["dst"] == visited["id"], "left_anti")
            pick = candidates.groupBy("curr").agg(F.first("dst").alias("next"))
            new_frontier = pick.where(F.col("next").isNotNull()).select(F.col("next").alias("curr"))
            if new_frontier.rdd.isEmpty():
                break
            visited = visited.union(new_frontier.select(F.col("curr").alias("id"))).distinct()
            frontier = new_frontier
            steps += 1

        sampled_vertices = visited.join(v, on="id", how="inner")
        sv = sampled_vertices.select(F.col("id").alias("vid"))
        edges_src = e.join(sv, e["src"] == sv["vid"], "inner").drop("vid")
        sv2 = sampled_vertices.select(F.col("id").alias("vid"))
        induced_edges = edges_src.join(sv2, edges_src["dst"] == sv2["vid"], "inner").drop("vid")
        return GraphFrame(sampled_vertices, induced_edges)


