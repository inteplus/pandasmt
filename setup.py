#!/usr/bin/env python3

from setuptools import setup, find_packages, find_namespace_packages
from pandasmt.version import VERSION

setup(
    name='pandasmt',
    version=VERSION,
    description="MT's extra modules for pandas",
    author=["Minh-Tri Pham"],
    packages=find_packages() + find_namespace_packages(include=['mt.*']),
    install_requires=[
        'pandas>=0.23.0',  # for dataframes
        'dask[dataframe]',  # for reading chunks of CSV files in parallel
        'basemt>=0.3.0',  # Minh-Tri's base modules for logging and multi-threading
    ],
)
