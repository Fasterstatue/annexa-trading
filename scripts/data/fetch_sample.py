"""
Sample data loader for Annexa Trading.

This module provides a simple function to load historical price data
from a local CSV file. The sample dataset ships with the project
under ``data/sample_stock.csv``. It includes one month of daily
bar data for a fictional stock. The columns are ``date``, ``open``,
``high``, ``low``, ``close``, and ``volume``.

Usage::

    from scripts.data import load_sample_data

    df = load_sample_data()
    print(df.head())

The loader returns a :class:`pandas.DataFrame` indexed by the
``date`` column. If ``pandas`` is not installed, the function
raises an informative ImportError.

Future development::

    This module can be extended with functions to download data
    from public data providers or broker APIs. For example, a
    function ``download_yahoo(symbol, start, end)`` could
    download data via ``pandas_datareader`` if network access
    is available. Until then, the local sample CSV provides a
    deterministic dataset for development and testing.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Optional


def _check_pandas() -> object:
    """Return the pandas module if it is installed.

    Raises:
        ImportError: if pandas is not installed.
    """
    module_name = "pandas"
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        raise ImportError(
            "The pandas library is required to load sample data. "
            "Install it with 'pip install pandas' inside your environment."
        )
    return importlib.import_module(module_name)


def load_sample_data(file_path: Optional[str] = None):
    """Load the bundled sample stock data as a pandas DataFrame.

    Parameters
    ----------
    file_path : str, optional
        Path to a CSV file with columns ``date``, ``open``, ``high``,
        ``low``, ``close``, and ``volume``. If omitted, the
        default file ``data/sample_stock.csv`` relative to the
        project root will be used.

    Returns
    -------
    pandas.DataFrame
        A DataFrame indexed by ``date`` with the remaining
        columns as numeric values.

    Raises
    ------
    FileNotFoundError
        If the specified file does not exist.
    ImportError
        If pandas is not installed.
    """
    pd = _check_pandas()
    # Determine the path to the sample data file. If a custom
    # path is provided, use it. Otherwise, locate the default
    # CSV relative to this module (../data/sample_stock.csv).
    if file_path is not None:
        csv_path = Path(file_path)
    else:
        # The project root is two levels up from this file.
        here = Path(__file__).resolve().parent
        csv_path = here.parent.parent / "data" / "sample_stock.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"Data file not found: {csv_path}")

    df = pd.read_csv(csv_path)
    # Convert date column to datetime and set as index
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    return df