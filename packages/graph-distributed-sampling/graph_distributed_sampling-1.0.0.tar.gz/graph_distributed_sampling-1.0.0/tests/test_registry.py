from distributed_sampling.registry import available_samplers


def test_entry_points_registered():
    names = set(available_samplers().keys())
    expected = {
        "random_node",
        "random_edge",
        "snowball",
        "random_walk",
        "forest_fire",
        "topk",
        "bfs",
        "uvsn",
        "nuvsn",
        "mhrw",
        "rwe",
        "mirw",
        "mdrw",
        "dfs",
    }
    assert expected.issubset(names)


