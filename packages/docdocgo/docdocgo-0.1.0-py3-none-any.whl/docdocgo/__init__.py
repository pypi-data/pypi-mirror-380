"""
docdocgo - Insert pandas DataFrames as tables into Microsoft Word documents.

This package allows data scientists to insert pandas DataFrames as formatted tables
into Word documents by using markers like {{DOCDOC_QUARTERLY_NUMBERS}} in the document.
"""

from .core import create_document_with_table, docdocgo, insert_table

__version__ = "0.1.0"
__all__ = ["docdocgo", "insert_table", "create_document_with_table"]
