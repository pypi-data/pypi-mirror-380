# ---------------------------------------------------------------------------
# Configuração do módulo pybind11 (_mtlearn)
# ---------------------------------------------------------------------------

find_package(pybind11 CONFIG QUIET)

if(NOT pybind11_FOUND)
    include(FetchContent)
    FetchContent_Declare(
        pybind11
        URL https://github.com/pybind/pybind11/archive/refs/tags/v2.13.1.tar.gz
        DOWNLOAD_EXTRACT_TIMESTAMP TRUE
    )
    FetchContent_MakeAvailable(pybind11)
endif()

find_package(Python3 COMPONENTS Interpreter QUIET)

if(MTLEARN_WITH_TORCH)
    find_package(Torch REQUIRED)
    pybind11_add_module(_mtlearn module.cpp)
    target_link_libraries(_mtlearn PRIVATE mtlearn::core ${TORCH_LIBRARIES})
    target_include_directories(_mtlearn PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../src ${TORCH_INCLUDE_DIRS})
    target_compile_definitions(_mtlearn PRIVATE MTLEARN_WITH_TORCH=1)
else()
    pybind11_add_module(_mtlearn module_stub.cpp)
    target_link_libraries(_mtlearn PRIVATE mtlearn::core)
    target_include_directories(_mtlearn PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../src)
    target_compile_definitions(_mtlearn PRIVATE MTLEARN_WITH_TORCH=0)
endif()

set_target_properties(_mtlearn PROPERTIES OUTPUT_NAME "_mtlearn")
set_property(TARGET _mtlearn PROPERTY CXX_STANDARD 20)
set_property(TARGET _mtlearn PROPERTY CXX_STANDARD_REQUIRED ON)
set_property(TARGET _mtlearn PROPERTY CXX_EXTENSIONS OFF)
set_target_properties(_mtlearn PROPERTIES POSITION_INDEPENDENT_CODE ON)

install(TARGETS _mtlearn
        LIBRARY DESTINATION mtlearn
        ARCHIVE DESTINATION mtlearn
        RUNTIME DESTINATION mtlearn)
