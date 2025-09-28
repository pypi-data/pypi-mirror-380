#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <torch/extension.h>

#include "mtlearn/core.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_mtlearn, m)
{
    m.doc() = "Python bindings for MTLearn built on top of mmcfilters";

    py::class_<mtlearn::TreeStats>(m, "TreeStats")
        .def(py::init<>())
        .def_readwrite("num_nodes", &mtlearn::TreeStats::numNodes)
        .def("describe", [](const mtlearn::TreeStats& stats) {
            return mtlearn::describeTree(stats);
        });

    m.def(
        "make_tree_stats",
        [](int numNodes) {
            return mtlearn::makeTreeStats(numNodes);
        },
        py::arg("num_nodes"),
        "Create a simple TreeStats instance using a node count.");

    m.def(
        "make_tree_tensor",
        [](int numNodes) {
            auto stats = mtlearn::makeTreeStats(numNodes);
            auto tensor = torch::arange(numNodes, torch::dtype(torch::kFloat32));
            return py::make_tuple(stats, tensor);
        },
        py::arg("num_nodes"),
        "Return TreeStats and a torch tensor with a simple range.");

    m.attr("WITH_TORCH") = true;
}
