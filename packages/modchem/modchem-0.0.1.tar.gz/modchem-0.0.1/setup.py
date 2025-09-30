from setuptools import setup, Extension
from pybind11.setup_helpers import build_ext, Pybind11Extension

ext_modules = [
    Pybind11Extension(
        "_electrons",
        ["./src/cppscripts/electric.cpp"],
        extra_compile_args=["-std=c++11"]  # Убедитесь, что ваш компилятор поддерживает C++11+
    ),
]