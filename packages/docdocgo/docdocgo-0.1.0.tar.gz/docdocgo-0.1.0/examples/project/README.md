# Example docdocgo Usage Project

This project demonstrates how to install and use the `docdocgo` package from TestPyPI in a real Python project.

## About

This example project showcases:

- Installing `docdocgo` from TestPyPI using uv
- Creating Word documents with pandas DataFrames
- Using marker replacement in existing documents
- All three main API functions of docdocgo

## Setup

The project is configured to install `docdocgo` from TestPyPI with fallback to PyPI for other dependencies.

### Install Dependencies

```bash
cd examples/project
uv sync --index-strategy unsafe-best-match
```

**Note**: The `--index-strategy unsafe-best-match` flag is required because this project installs `docdocgo` from TestPyPI while getting other dependencies from PyPI.

### Using the Template

A pre-generated Word template (`template.docx`) is included in the project.

The template includes:

- Arial font throughout
- Professional headings and lorem ipsum content
- `{{QUARTERLY_PERFORMANCE_DATA}}` marker for docdocgo replacement

### Run the Example

```bash
uv run python main.py
```

## What It Does

The example creates three different Word documents:

1. **Sales Report** (`quarterly_sales_report.docx`)
   - Demonstrates `create_document_with_table()`
   - Creates a new document with quarterly sales data

2. **Employee Report** (`employee_report_template.docx`)
   - Demonstrates `insert_table()` with marker replacement
   - Creates a template with `{{EMPLOYEE_PERFORMANCE_DATA}}` marker
   - Replaces the marker with employee performance data

3. **Financial Summary** (`financial_summary.docx`)
   - Demonstrates the main `docdocgo()` convenience function
   - Creates a financial summary document

## Project Configuration

The `pyproject.toml` is configured to:

- Install `docdocgo` from TestPyPI
- Use PyPI as fallback for other dependencies like `pandas`
- Support Python e3.9

## Expected Output

```
=� docdocgo TestPyPI Example Project
========================================
=� Creating quarterly sales report...
 Sales report created: quarterly_sales_report.docx
Sales data shape: (4, 4)

=e Creating employee performance report...
 Employee report created: employee_report_template.docx
Employee data shape: (4, 4)

= Demonstrating convenience function...
 Financial summary created: financial_summary.docx
Financial data shape: (4, 3)

<� All examples completed successfully!
=� Generated files:
   - quarterly_sales_report.docx
   - employee_report_template.docx
   - financial_summary.docx
```

## Package Configuration

The key configuration in `pyproject.toml`:

```toml
dependencies = [
    "docdocgo",
    "pandas",
]

[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"

[[tool.uv.index]]
name = "pypi"
url = "https://pypi.org/simple/"
default = true
```

This setup ensures `docdocgo` is installed from TestPyPI while other dependencies come from the main PyPI index.

## Template Features

The generated `template.docx` includes:

- Professional business report structure
- Arial font (11pt) throughout the document
- Multiple heading levels with proper formatting
- Lorem ipsum placeholder content
- `{{QUARTERLY_PERFORMANCE_DATA}}` marker for docdocgo
- Centered alignment for title and data sections

