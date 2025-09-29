from __future__ import annotations

from typing import Iterable, Optional

from pyspark.sql import DataFrame, functions as F
from graphframes import GraphFrame

from .base import GraphSampler


class ForestFireSampler(GraphSampler):
    """Forest Fire sampling (approximate) as per Leskovec et al.

    At each step, a node burns a random fraction `p` of its outgoing neighbors
    (without replacement), which become the next frontier. Process repeats until
    a maximum number of nodes is reached or frontier is empty.
    """

    name = "forest_fire"

    def __init__(
        self,
        p: float = 0.3,
        max_nodes: Optional[int] = None,
        seeds: Optional[Iterable[str]] = None,
        num_seeds: int = 1,
        seed: Optional[int] = None,
    ) -> None:
        if not (0.0 <= p <= 1.0):
            raise ValueError("p must be in [0,1]")
        if num_seeds <= 0:
            raise ValueError("num_seeds must be > 0")
        self.p = float(p)
        self.max_nodes = max_nodes
        self.seeds = list(seeds) if seeds is not None else None
        self.num_seeds = int(num_seeds)
        self.seed = seed

    def _choose_seeds(self, vertices: DataFrame) -> DataFrame:
        if self.seeds is not None:
            return vertices.join(
                F.broadcast(F.createDataFrame([(s,) for s in self.seeds], ["id"])),
                on="id",
                how="inner",
            )
        return vertices.orderBy(F.rand(self.seed)).limit(self.num_seeds).select("id")

    def sample(self, graph: GraphFrame) -> GraphFrame:
        v = graph.vertices
        e = graph.edges

        seeds_df = self._choose_seeds(v)
        frontier = seeds_df.select(F.col("id").alias("curr"))
        visited = frontier.select(F.col("curr").alias("id")).distinct()

        step = 0
        while True:
            # For each current node, sample a fraction p of its outgoing neighbors
            outgoing = frontier.join(e, frontier["curr"] == e["src"], "left")
            # Assign random and keep those with rand < p
            rand = F.rand(self.seed + step if self.seed else None)
            burn = outgoing.withColumn("burn", rand < F.lit(self.p)).where(F.col("burn"))
            next_frontier = burn.select(F.col("dst").alias("curr")).distinct()

            # Remove already visited
            next_frontier = next_frontier.join(visited, next_frontier["curr"] == visited["id"], "left_anti")

            if next_frontier.rdd.isEmpty():
                break

            visited = visited.union(next_frontier.select(F.col("curr").alias("id"))).distinct()

            if self.max_nodes is not None and visited.count() >= self.max_nodes:
                # Truncate to max_nodes approximately
                visited = visited.limit(self.max_nodes)
                break

            frontier = next_frontier
            step += 1

        sampled_vertices = visited.join(v, on="id", how="inner")

        # Induced edges
        sv = sampled_vertices.select(F.col("id").alias("vid"))
        edges_src = e.join(sv, e["src"] == sv["vid"], "inner").drop("vid")
        sv2 = sampled_vertices.select(F.col("id").alias("vid"))
        induced_edges = edges_src.join(sv2, edges_src["dst"] == sv2["vid"], "inner").drop("vid")

        return GraphFrame(sampled_vertices, induced_edges)


