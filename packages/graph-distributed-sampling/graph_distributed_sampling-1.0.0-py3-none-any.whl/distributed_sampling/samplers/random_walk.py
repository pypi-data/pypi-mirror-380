from __future__ import annotations

from typing import Iterable, Optional

from pyspark.sql import DataFrame, Row, functions as F
from graphframes import GraphFrame

from .base import GraphSampler


class RandomWalkSampler(GraphSampler):
    """Perform multiple random walks and take induced subgraph of visited nodes.

    Notes: This is a simple unbiased walk. For large graphs, consider using
    checkpoints/persist to manage lineage. This implementation is driver-light
    and avoids collecting graph structure to the driver.
    """

    name = "random_walk"

    def __init__(
        self,
        walk_length: int = 10,
        num_walks: int = 10,
        start_nodes: Optional[Iterable[str]] = None,
        seed: Optional[int] = None,
    ) -> None:
        if walk_length <= 0:
            raise ValueError("walk_length must be > 0")
        if num_walks <= 0:
            raise ValueError("num_walks must be > 0")
        self.walk_length = int(walk_length)
        self.num_walks = int(num_walks)
        self.start_nodes = list(start_nodes) if start_nodes is not None else None
        self.seed = seed

    def _choose_starts(self, vertices: DataFrame) -> DataFrame:
        if self.start_nodes is not None:
            return vertices.join(
                F.broadcast(F.createDataFrame([(s,) for s in self.start_nodes], ["id"])),
                on="id",
                how="inner",
            )
        return vertices.orderBy(F.rand(self.seed)).limit(self.num_walks).select("id")

    def sample(self, graph: GraphFrame) -> GraphFrame:
        v = graph.vertices
        e = graph.edges

        starts = self._choose_starts(v).withColumnRenamed("id", "curr")

        visited = starts.select(F.col("curr").alias("id")).distinct()
        frontier = starts

        for step in range(self.walk_length):
            # For each current node, pick one random outgoing neighbor if exists; otherwise stay.
            out_edges = frontier.join(e, frontier["curr"] == e["src"], "left")

            # Assign random value per potential next edge and pick min per curr to simulate random pick
            cand = out_edges.withColumn("rand", F.rand(self.seed + step if self.seed else None))
            next_edge = cand.groupBy("curr").agg(F.first(F.struct("rand", "dst")).alias("picked"))
            next_vertices = next_edge.select(F.col("curr"), F.col("picked.dst").alias("next"))

            # If a node had no outgoing edges, next will be null; keep it as is (walk stops there)
            next_vertices = next_vertices.fillna({"next": None})

            new_frontier = next_vertices.where(F.col("next").isNotNull()).select(F.col("next").alias("curr"))
            if new_frontier.rdd.isEmpty():
                break

            visited = visited.union(new_frontier.select(F.col("curr").alias("id"))).distinct()
            frontier = new_frontier

        sampled_vertices = visited.join(v, on="id", how="inner")

        # Induced edges among sampled vertices
        sv = sampled_vertices.select(F.col("id").alias("vid"))
        edges_src = e.join(sv, e["src"] == sv["vid"], "inner").drop("vid")
        sv2 = sampled_vertices.select(F.col("id").alias("vid"))
        induced_edges = edges_src.join(sv2, edges_src["dst"] == sv2["vid"], "inner").drop("vid")

        return GraphFrame(sampled_vertices, induced_edges)


