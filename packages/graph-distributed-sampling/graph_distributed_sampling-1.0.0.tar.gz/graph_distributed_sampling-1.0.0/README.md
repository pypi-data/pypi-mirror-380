# distributed-sampling

Extensible distributed graph sampling library for Spark [GraphFrames].

## Install

This library is a pure Python package. It expects to run inside a Spark environment
where `pyspark` is available, and the GraphFrames package is attached to the Spark
session.

```bash
pip install distributed-sampling
```

GraphFrames is provided as a Spark package. Start Spark with GraphFrames attached, e.g.:

```bash
# Adjust versions to your Spark/Scala setup
pyspark \
  --packages graphframes:graphframes:0.8.3-spark3.5-s_2.12
```

Or in code when creating a SparkSession:

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("sampling")
    .config("spark.jars.packages", "graphframes:graphframes:0.8.3-spark3.5-s_2.12")
    .getOrCreate()
)
```

## Usage

```python
from graphframes import GraphFrame
from distributed_sampling import sample_graph

# gf: a GraphFrame with columns id, src, dst
sampled = sample_graph(gf, "random_node", fraction=0.1, seed=42)
```

### API

- `sample_graph(graph: GraphFrame, method: str, **kwargs) -> GraphFrame` — top-level API.
- Samplers implement the interface `GraphSampler` with a `sample` method.

## Built-in methods

- `random_node` — random node sampling with induced subgraph.
- `random_edge` — randomly sample edges and keep their endpoints.
- `snowball` — BFS-style expansion from seeds up to a given depth.
- `random_walk` — multiple random walks; induced subgraph of visited nodes.
- `forest_fire` — burn a fraction of neighbors iteratively.
- `topk` — keep top-K vertices by degree (in/out/total).
- `bfs(seeds=None, num_seeds=1, depth=2)` — breadth-first expansion.
- `uvsn(fraction=0.1|num_vertices, seed=None)` — uniform vertex sampling with neighborhood.
- `nuvsn(fraction=0.1|num_vertices, seed=None)` — non-uniform (degree-weighted) vertex sampling with neighborhood.
- `mhrw(walk_length=100, num_walks=10, start_nodes=None, seed=None)` — Metropolis-Hastings random walk.
- `rwe(walk_length=100, num_walks=10, start_nodes=None, alpha=0.15, seed=None)` — random walk with escaping/restarts.
- `mirw(walk_length=10, num_walks=100, seed=None)` — multiple independent walkers.
- `mdrw(walk_length=10, num_walks=10, attr=None, seed=None)` — multi-dimensional walk biased by vertex attribute.
- `dfs(seeds=None, num_seeds=1, max_steps=100)` — approximate depth-first sampling.

## Extending with your own sampler

1. Implement a class that subclasses `GraphSampler`:

```python
from distributed_sampling.samplers import GraphSampler

class MySampler(GraphSampler):
    name = "my_method"  # optional convenience

    def __init__(self, my_param: float = 0.5):
        self.my_param = my_param

    def sample(self, graph):
        # return a GraphFrame
        ...
```

2. Expose it via entry points in your own package `pyproject.toml`:

```toml
[project.entry-points."distributed_sampling.samplers"]
my_method = "my_pkg.my_module:MySampler"
```

Your sampler will be discoverable by name `"my_method"` at runtime without code changes here.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

[GraphFrames]: https://graphframes.github.io/
https://arxiv.org/pdf/1308.5865


