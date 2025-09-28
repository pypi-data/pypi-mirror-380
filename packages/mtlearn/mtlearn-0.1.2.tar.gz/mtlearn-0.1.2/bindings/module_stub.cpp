#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "mtlearn/core.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_mtlearn, m)
{
    m.doc() = "MTLearn bindings built without LibTorch support";

    py::class_<mtlearn::TreeStats>(m, "TreeStats")
        .def(py::init<>())
        .def_readwrite("num_nodes", &mtlearn::TreeStats::numNodes)
        .def("describe", [](const mtlearn::TreeStats& stats) {
            return mtlearn::describeTree(stats);
        });

    m.def("make_tree_stats",
          [](int numNodes) {
              return mtlearn::makeTreeStats(numNodes);
          },
          py::arg("num_nodes"),
          "Create a simple TreeStats instance using a node count.");

    m.def("make_tree_tensor",
          [](int) -> py::object {
              throw py::import_error(
                  "mtlearn foi compilado sem suporte ao LibTorch; instale com MTLEARN_WITH_TORCH=ON e LibTorch disponível.");
          },
          py::arg("num_nodes"));

    m.attr("WITH_TORCH") = false;
}
