#!/usr/bin/env python3

from setuptools import setup, find_packages
from pandasmt.version import VERSION as version

setup(
    name='pandasmt',
    version=version,
    description="MT's extra modules for pandas",
    author=["Minh-Tri Pham"],
    packages=find_packages(),
    install_requires=[
        'pandas>=0.23.0',  # for dataframes
        'dask[dataframe]',  # for reading chunks of CSV files in parallel
        'basemt',  # Minh-Tri's base modules for logging and multi-threading
    ],
)
