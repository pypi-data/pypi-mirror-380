import importlib


def test_import_public_api():
    m = importlib.import_module("distributed_sampling")
    assert hasattr(m, "sample_graph")


