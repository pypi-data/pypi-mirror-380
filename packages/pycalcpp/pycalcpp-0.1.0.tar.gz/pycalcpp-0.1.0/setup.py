from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "Operaciones",
        ["Operaciones.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=["/std:c++17"] if "msvc" in pybind11.get_include() else ["-std=c++17"],
    )
]

setup(
    name="pycalcpp",
    version="0.1.0",
    description="Calculadora matemática de alto rendimiento (C++ + pybind11)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="JOSEDVP76",
    url="https://github.com/JDEVELOPER76/PyCal-plus-plus",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    ext_modules=ext_modules,
    py_modules=["Calculadora"],
    zip_safe=False,
)