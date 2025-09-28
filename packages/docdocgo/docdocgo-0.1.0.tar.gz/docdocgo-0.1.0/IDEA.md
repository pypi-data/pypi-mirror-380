# docdocgo

## Idea

The idea is that data scientist can use their pandas data frames and display them in a MS word document.
The user includes markers like {{DOCDOC_QUARTERLY_NUMBERS}} in the document text.

Then they can run docdocgo(pandas_df, "pathtodoc.docx") to include the dataframe as a table in the document.
There is also a functionality which creates an empty docx and inserts the table.

## Setup

- Use the uv package manager
- Result should be a python package
- Include pytest tests

## Todos that should be considered

- Set up the project with `uv init`
- Edit `pyproject.toml`
- Create an example data frame
- Create an example docx
- Find a way to test the result, maybe `pandoc` which is intalled on the system
- Research docx capabilities in python
- Decide on a nice styling if the tables (with a dark blue heading).
- If possible, use table themes
