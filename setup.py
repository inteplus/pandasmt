#!/usr/bin/env python3

from setuptools import setup, find_packages
from mt.pandas.version import VERSION

setup(
    name='pandasmt',
    version=VERSION,
    description="MT's extra modules for pandas. This package has been deprecated. Use package 'mtpandas' instead.",
    author=["Minh-Tri Pham"],
    packages=find_packages(),
    install_requires=[
        'pandas>=0.23.0',  # for dataframes, and we need custom dtypes
        'dask[dataframe]',  # for reading chunks of CSV files in parallel
        'mtpandas>=0.2.0',  # Minh-Tri's base modules for logging and multi-threading
    ],
)
