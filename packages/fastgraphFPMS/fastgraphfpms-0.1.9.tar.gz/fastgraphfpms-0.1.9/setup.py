import sys
from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext
import pybind11

extra_compile_args = []
if sys.platform == "win32":
    extra_compile_args = ['/bigobj'] 

ext_modules = [
    Pybind11Extension(
        "fastgraphFPMS",
        sources=[
            "python/fastgraphFPMS_module.cpp",
            "src/graph.cpp"
        ],
        include_dirs=[
            "src",
            pybind11.get_include()
        ],
        language='c++',
        cxx_std=14,
        extra_compile_args=extra_compile_args,  # Important pour Windows
    ),
]

setup(
    name="fastgraphFPMS",
    version="0.1.9",
    author="Flavio D.",
    author_email="drogoflavio16@gmail.com",
    description="Fast Graph Algorithms Library implemented in C++",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: C++"
    ],
)