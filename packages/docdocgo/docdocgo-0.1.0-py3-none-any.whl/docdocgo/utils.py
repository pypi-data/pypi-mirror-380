"""
Utility functions for docdocgo package.
"""

from pathlib import Path
from typing import Union

import pandas as pd


def validate_dataframe(df: pd.DataFrame) -> None:
    """
    Validate that the input is a proper pandas DataFrame.

    Args:
        df: Object to validate

    Raises:
        TypeError: If df is not a pandas DataFrame
        ValueError: If DataFrame is empty
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(f"Expected pandas DataFrame, got {type(df).__name__}")

    if df.empty:
        raise ValueError("DataFrame cannot be empty")


def validate_file_path(path: Union[str, Path], must_exist: bool = False) -> None:
    """
    Validate file path.

    Args:
        path: Path to validate
        must_exist: If True, raises error if file doesn't exist

    Raises:
        FileNotFoundError: If must_exist is True and file doesn't exist
        ValueError: If path is not a valid file path
    """
    path = Path(path)

    if must_exist and not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if must_exist and not path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    # Check if parent directory exists (for new files)
    if not must_exist and not path.parent.exists():
        raise ValueError(f"Parent directory does not exist: {path.parent}")


def format_cell_value(value) -> str:
    """
    Format a cell value for display in Word table.

    Args:
        value: Value to format

    Returns:
        Formatted string representation
    """
    if pd.isna(value):
        return ""
    elif isinstance(value, float):
        # Format floats with reasonable precision
        if value.is_integer():
            return str(int(value))
        else:
            return f"{value:.2f}"
    else:
        return str(value)
