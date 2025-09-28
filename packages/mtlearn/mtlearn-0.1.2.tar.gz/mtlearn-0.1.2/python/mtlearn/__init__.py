"""Interface Python para MTLearn."""

from importlib import import_module

_bindings = import_module("._mtlearn", package=__name__)

TreeStats = _bindings.TreeStats
make_tree_stats = _bindings.make_tree_stats

WITH_TORCH = getattr(_bindings, "WITH_TORCH", False)


def make_tree_tensor(num_nodes):
    """Retorna (TreeStats, tensor). Requer build com suporte ao LibTorch."""
    return _bindings.make_tree_tensor(num_nodes)

__all__ = [
    "TreeStats",
    "make_tree_stats",
    "make_tree_tensor",
    "WITH_TORCH",
]

__version__ = "0.1.0"
