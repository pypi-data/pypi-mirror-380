import pytest
import unittest
import importlib
import matplotlib as mpl

mpl.use("agg")
import matplotlib.pyplot as plt
import iplotx as ipx
from utils import image_comparison

if importlib.util.find_spec("igraph") is None:
    raise unittest.SkipTest("igraph not found, skipping tests")


@pytest.fixture
def graph_and_layout_small():
    import igraph as ig

    g = ig.Graph.Ring(5)
    layout = g.layout("circle").coords
    zs = [0, 1, 0.5, 0.8, 0.2]
    layout3d = [(x, y, z) for (x, y), z in zip(layout, zs)]

    return {
        "graph": g,
        "layout2d": layout,
        "layout3d": layout3d,
    }


@image_comparison(baseline_images=["undirected"], remove_text=True)
def test_undirected(graph_and_layout_small):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(1, 1, 1, projection="3d")

    ipx.network(
        graph_and_layout_small["graph"],
        layout=graph_and_layout_small["layout3d"],
        ax=ax,
    )
