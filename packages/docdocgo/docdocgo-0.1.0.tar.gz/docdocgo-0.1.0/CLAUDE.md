# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

docdocgo is a Python package that allows data scientists to insert pandas DataFrames into Microsoft Word documents. Users place markers like `{{DOCDOC_QUARTERLY_NUMBERS}}` in their Word documents, then call `docdocgo(pandas_df, "pathtodoc.docx")` to replace these markers with formatted tables.

## Development Setup

- **Package Manager**: Use `uv` for dependency management
- **Project Type**: Python package with pytest tests
- **Package Configuration**: Managed through `pyproject.toml`

## Key Development Commands

- `just test` - Run comprehensive tests and examples (recommended)
- `just test-unit` - Run only unit tests
- `just test-examples` - Run only examples
- `just test-coverage` - Run tests with coverage report
- `just build` - Build Python wheels
- `just clean` - Clean build artifacts and generated .docx files
- `uv sync` - Install dependencies
- `uv run pytest` - Run tests directly
- `uv run python examples/basic_usage.py` - Run examples

## Project Structure

```
docdocgo/
├── src/docdocgo/          # Main package
│   ├── __init__.py        # Package exports
│   ├── core.py           # Core functionality
│   ├── styling.py        # Table styling
│   └── utils.py          # Utility functions
├── tests/                # Test suite
├── examples/             # Usage examples
├── justfile             # Task runner
└── pyproject.toml       # Package configuration
```

## API Overview

The package provides three main functions:
- `docdocgo(df, path, marker=None)` - Convenience function
- `create_document_with_table(df, output_path)` - Create new document
- `insert_table(df, docx_path, marker)` - Replace marker in existing document

## Dependencies

- `python-docx>=1.1.0` - Word document manipulation
- `pandas>=1.5.0` - DataFrame handling

## Testing Strategy

- Comprehensive pytest test suite (22 tests)
- Integration tests with real Word documents
- Examples that demonstrate all functionality
- Coverage reporting available via `just test-coverage`

