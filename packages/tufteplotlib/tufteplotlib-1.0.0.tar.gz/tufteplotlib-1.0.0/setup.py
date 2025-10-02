#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file for the long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    author="Jon Woolfrey",
    author_email="jonathan.woolfrey@gmail.com",
    description="An extension to matplotlib for creating graphs in the style of Edward Tufte.",
    entry_points={
        "console_scripts": [
            "tufte-bar       = tufteplotlib.plots.bar:main",
            "tufte-barcode   = tufteplotlib.plots.barcode:main",
            "tufte-density   = tufteplotlib.plots.density:main",
            "tufte-galaxy    = tufteplotlib.plots.galaxy:main",
            "tufte-histogram = tufteplotlib.plots.histogram:main",
            "tufte-line      = tufteplotlib.plots.line:main",
            "tufte-pareto    = tufteplotlib.plots.pareto:main",
            "tufte-quartile  = tufteplotlib.plots.quartile:main",
            "tufte-rug       = tufteplotlib.plots.rug:main",
            "tufte-scatter   = tufteplotlib.plots.scatter:main",
            "tufte-sparkline = tufteplotlib.plots.sparkline:main",
            "tufte-stem      = tufteplotlib.plots.stem_and_leaf:main",
            "tufte-time      = tufteplotlib.plots.time:main",
        ],
    },
    include_package_data=True,
    install_requires=[
        "matplotlib>=3.0",
        "numpy>=1.21",
        "pandas>=1.4",
    ],
    keywords="matplotlib tufte visualization plotting minimalistic graph",
    license="GPLv3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests*", "examples*"]),
    project_urls={
        "Bug Reports": "https://github.com/Woolfrey/software_tufte_plot/issues",
        "Source": "https://github.com/Woolfrey/software_tufte_plot",
    },
    python_requires=">=3.10",
    url="https://github.com/Woolfrey/software_tufte_plot",
    version="1.0.0",
    name="tufteplotlib",
)
