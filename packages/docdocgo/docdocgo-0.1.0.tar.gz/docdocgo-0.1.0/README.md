# docdocgo

Insert pandas DataFrames as tables into Microsoft Word documents.

## Features

- **Simple API**: Just call `docdocgo(df, "document.docx")` to update Word documents
- **Marker Replacement**: Use markers like `{{QUARTERLY_NUMBERS}}` in your Word templates
- **Professional Styling**: Tables with dark blue headers and alternating row colors
- **Type Support**: Handles all pandas data types including NaN values
- **Performance Optimized**: Efficient table creation for large DataFrames

## Installation

```bash
uv add docdocgo
```

Or with pip:

```bash
pip install docdocgo
```

## Quick Start

```python
import pandas as pd
from docx import Document
import docdocgo

data = pd.DataFrame({
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Revenue": [120000, 135000, 142000, 158000],
    "Profit": [25000, 32000, 28000, 41000],
})

doc = Document()
doc.add_heading("Quarterly Report", 0)
doc.add_paragraph("Here are the quarterly results:")
doc.add_paragraph("{{QUARTERLY_DATA}}")
doc.add_paragraph("Thank you for reviewing this report.")
doc.save("template.docx")

docdocgo.insert_table(data, "template.docx", "{{QUARTERLY_DATA}}", "result.docx")
```

This transforms your template document into a final report:

📄 **[template.docx](examples/template.docx)** → 📊 **[result.docx](examples/result.docx)**

From template with marker to professional report with formatted table

## API Reference

### `docdocgo(df, path, marker=None, output_path=None)`

Convenience function to insert DataFrame into Word document.

**Parameters:**

- `df` (pandas.DataFrame): DataFrame to insert
- `path` (str | Path): Path to Word document
- `marker` (str, optional): Marker to replace. If None, creates new document
- `output_path` (str | Path, optional): Output path. If None, overwrites input file

### `create_document_with_table(df, output_path)`

Create a new Word document with a DataFrame table.

**Parameters:**

- `df` (pandas.DataFrame): DataFrame to insert
- `output_path` (str | Path): Path for the new document

### `insert_table(df, docx_path, marker, output_path=None)`

Replace a marker in an existing Word document with a DataFrame table.

**Parameters:**

- `df` (pandas.DataFrame): DataFrame to insert
- `docx_path` (str | Path): Path to existing Word document
- `marker` (str): Marker string to replace
- `output_path` (str | Path, optional): Output path. If None, overwrites input document

## Development

Uses [just](https://just.systems/man/en/).

```bash
# Clone and setup
git clone <repository>
cd docdocgo
uv sync

# Run tests and examples
just test
```

## License

MIT License

