"""
Tests for utility functions of docdocgo package.
"""

import tempfile
from pathlib import Path

import pandas as pd
import pytest

from docdocgo.utils import format_cell_value, validate_dataframe, validate_file_path


class TestValidateDataframe:
    """Test validate_dataframe function."""

    def test_valid_dataframe(self):
        """Test with valid DataFrame."""
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        # Should not raise any exception
        validate_dataframe(df)

    def test_empty_dataframe_raises_error(self):
        """Test that empty DataFrame raises ValueError."""
        empty_df = pd.DataFrame()
        with pytest.raises(ValueError, match="DataFrame cannot be empty"):
            validate_dataframe(empty_df)

    def test_non_dataframe_raises_error(self):
        """Test that non-DataFrame input raises TypeError."""
        with pytest.raises(TypeError, match="Expected pandas DataFrame"):
            validate_dataframe("not a dataframe")

        with pytest.raises(TypeError, match="Expected pandas DataFrame"):
            validate_dataframe([1, 2, 3])

        with pytest.raises(TypeError, match="Expected pandas DataFrame"):
            validate_dataframe({"A": [1, 2, 3]})


class TestValidateFilePath:
    """Test validate_file_path function."""

    def test_valid_path_new_file(self):
        """Test valid path for new file."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            new_file_path = Path(tmp_dir) / "new_file.docx"
            # Should not raise any exception
            validate_file_path(new_file_path, must_exist=False)

    def test_existing_file(self):
        """Test with existing file."""
        with tempfile.NamedTemporaryFile(suffix=".docx") as tmp_file:
            file_path = Path(tmp_file.name)
            # Should not raise any exception
            validate_file_path(file_path, must_exist=True)

    def test_nonexistent_file_with_must_exist(self):
        """Test that nonexistent file raises error when must_exist=True."""
        nonexistent_path = Path("/nonexistent/path/file.docx")
        with pytest.raises(FileNotFoundError):
            validate_file_path(nonexistent_path, must_exist=True)

    def test_invalid_parent_directory(self):
        """Test that invalid parent directory raises error."""
        invalid_path = Path("/nonexistent/directory/file.docx")
        with pytest.raises(ValueError, match="Parent directory does not exist"):
            validate_file_path(invalid_path, must_exist=False)


class TestFormatCellValue:
    """Test format_cell_value function."""

    def test_format_string(self):
        """Test formatting string values."""
        assert format_cell_value("hello") == "hello"
        assert format_cell_value("") == ""

    def test_format_integer(self):
        """Test formatting integer values."""
        assert format_cell_value(42) == "42"
        assert format_cell_value(0) == "0"
        assert format_cell_value(-5) == "-5"

    def test_format_float(self):
        """Test formatting float values."""
        assert format_cell_value(3.14159) == "3.14"
        assert format_cell_value(2.0) == "2"
        assert format_cell_value(-1.5) == "-1.50"

    def test_format_nan(self):
        """Test formatting NaN values."""
        assert format_cell_value(pd.NA) == ""
        assert format_cell_value(float("nan")) == ""

    def test_format_boolean(self):
        """Test formatting boolean values."""
        assert format_cell_value(True) == "True"
        assert format_cell_value(False) == "False"

    def test_format_none(self):
        """Test formatting None values."""
        assert format_cell_value(None) == ""
