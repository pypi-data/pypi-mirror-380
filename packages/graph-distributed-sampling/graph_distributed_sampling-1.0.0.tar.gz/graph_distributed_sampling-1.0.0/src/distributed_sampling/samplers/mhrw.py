from __future__ import annotations

from typing import Iterable, Optional

from pyspark.sql import functions as F
from graphframes import GraphFrame

from .base import GraphSampler


class MHRWSampler(GraphSampler):
    """Metropolis-Hastings Random Walk (degree-corrected).

    Transition from u to v with probability min(1, deg(u)/deg(v)) after proposing a random neighbor.
    """

    name = "mhrw"

    def __init__(
        self,
        walk_length: int = 100,
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

    def sample(self, graph: GraphFrame) -> GraphFrame:
        v = graph.vertices
        e = graph.edges

        # degrees
        indeg = e.groupBy("dst").count().withColumnRenamed("dst", "id").withColumnRenamed("count", "in")
        outdeg = e.groupBy("src").count().withColumnRenamed("src", "id").withColumnRenamed("count", "out")
        deg = v.select("id").join(indeg, on="id", how="left").join(outdeg, on="id", how="left").fillna(0, ["in", "out"]).withColumn("deg", F.col("in") + F.col("out"))

        # starting points
        if self.start_nodes is not None:
            starts = v.join(F.broadcast(F.createDataFrame([(s,) for s in self.start_nodes], ["id"])), on="id", how="inner").select(F.col("id").alias("curr"))
        else:
            starts = v.orderBy(F.rand(self.seed)).limit(self.num_walks).select(F.col("id").alias("curr"))

        visited = starts.select(F.col("curr").alias("id")).distinct()
        frontier = starts

        for step in range(self.walk_length):
            # Propose neighbor: pick random outgoing neighbor
            out_edges = frontier.join(e, frontier["curr"] == e["src"], "left")
            cand = out_edges.withColumn("rand", F.rand(self.seed + step if self.seed else None))
            prop = cand.groupBy("curr").agg(F.first(F.struct("rand", "dst")).alias("picked"))
            proposal = prop.select(F.col("curr"), F.col("picked.dst").alias("next"))

            # Compute acceptance ratio
            deg_u = proposal.join(deg.select(F.col("id").alias("uid"), F.col("deg").alias("du")), proposal["curr"] == F.col("uid"), "left")
            deg_uv = deg_u.join(deg.select(F.col("id").alias("vid"), F.col("deg").alias("dv")), deg_u["next"] == F.col("vid"), "left")
            accept_prob = F.when(F.col("dv") > 0, F.least(F.lit(1.0), F.col("du") / F.col("dv"))).otherwise(F.lit(1.0))
            with_accept = deg_uv.withColumn("acc_rand", F.rand(self.seed + 1000 + step if self.seed else None))
            accepted = with_accept.where((F.col("next").isNotNull()) & (F.col("acc_rand") < accept_prob))

            new_frontier = accepted.select(F.col("next").alias("curr"))
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


