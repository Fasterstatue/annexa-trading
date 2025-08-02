"""
Utilities for retrieving and loading market data.

This package currently contains a simple data loader that reads
historical price information from a local CSV file. In offline
environments, you can't fetch data from remote APIs, so a sample
dataset is provided in ``data/sample_stock.csv`` to get started.

Future versions may include functions to download data from
public APIs (e.g. Alpha Vantage, Stooq) once network access or API
keys are configured.
"""

from .fetch_sample import load_sample_data  # noqa: F401

__all__ = ["load_sample_data"]