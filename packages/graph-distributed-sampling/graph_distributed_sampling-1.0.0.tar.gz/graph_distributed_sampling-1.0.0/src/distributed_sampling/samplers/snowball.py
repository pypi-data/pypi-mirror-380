from __future__ import annotations

from typing import Iterable, Optional

from pyspark.sql import DataFrame, functions as F
from graphframes import GraphFrame

from .base import GraphSampler


class SnowballSampler(GraphSampler):
    """Snowball (BFS) sampling starting from one or more seed vertices.

    Parameters
    ----------
    seeds: Optional[Iterable[str]]
        Seed vertex ids. If None, seeds are chosen randomly according to `num_seeds`.
    num_seeds: int
        Number of random seeds to pick when `seeds` is None.
    depth: int
        Number of BFS layers to expand.
    """

    name = "snowball"

    def __init__(
        self, seeds: Optional[Iterable[str]] = None, num_seeds: int = 1, depth: int = 2
    ) -> None:
        if num_seeds <= 0:
            raise ValueError("num_seeds must be > 0")
        if depth < 0:
            raise ValueError("depth must be >= 0")
        self.seeds = list(seeds) if seeds is not None else None
        self.num_seeds = int(num_seeds)
        self.depth = int(depth)

    def _pick_random_seeds(self, vertices: DataFrame) -> DataFrame:
        return (
            vertices
            .orderBy(F.rand())
            .limit(self.num_seeds)
            .select("id")
            .withColumnRenamed("id", "seed")
        )

    def sample(self, graph: GraphFrame) -> GraphFrame:
        v = graph.vertices
        e = graph.edges

        if self.seeds is None:
            seeds_df = self._pick_random_seeds(v)
        else:
            seeds_df = v.join(F.broadcast(F.createDataFrame([(s,) for s in self.seeds], ["seed"])), v["id"] == F.col("seed"), "inner").select(F.col("seed"))

        # Initialize frontier with seeds
        frontier = seeds_df.select(F.col("seed").alias("id")).distinct()
        visited = frontier

        for _ in range(self.depth):
            # Neighbors via edges in either direction
            nbrs_out = frontier.join(e, frontier["id"] == e["src"], "inner").select(e["dst"].alias("id"))
            nbrs_in = frontier.join(e, frontier["id"] == e["dst"], "inner").select(e["src"].alias("id"))
            neighbors = nbrs_out.union(nbrs_in).distinct()

            new_frontier = neighbors.join(visited, on="id", how="left_anti")
            if new_frontier.rdd.isEmpty():  # short-circuit if no expansion
                break
            visited = visited.union(new_frontier).distinct()
            frontier = new_frontier

        sampled_vertices = visited.join(v, on="id", how="inner")

        # Induced edges among sampled vertices
        sv = sampled_vertices.select(F.col("id").alias("vid"))
        edges_src = e.join(sv, e["src"] == sv["vid"], "inner").drop("vid")
        sv2 = sampled_vertices.select(F.col("id").alias("vid"))
        induced_edges = edges_src.join(sv2, edges_src["dst"] == sv2["vid"], "inner").drop("vid")

        return GraphFrame(sampled_vertices, induced_edges)


