from __future__ import annotations

from typing import Any, Dict

from graphframes import GraphFrame

from .registry import get_sampler


def sample_graph(graph: GraphFrame, method: str, /, **kwargs: Dict[str, Any]) -> GraphFrame:
    """
    Sample a GraphFrame using a named method and return the resulting GraphFrame.

    Parameters
    ----------
    graph: GraphFrame
        Input graph.
    method: str
        Sampler method name (discovered via entry points), e.g. "random_node".
    **kwargs: Dict[str, Any]
        Parameters forwarded to the sampler constructor.
    """
    sampler_cls = get_sampler(method)
    sampler = sampler_cls(**kwargs)
    return sampler.sample(graph)


