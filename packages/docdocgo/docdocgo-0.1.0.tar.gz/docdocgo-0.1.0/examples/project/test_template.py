"""
Test the generated template with docdocgo.

This script creates sample data and uses docdocgo to replace
the marker in the generated template.
"""

import pandas as pd

import docdocgo


def test_template():
    """Test the template with sample data."""
    # Create sample data
    data = pd.DataFrame(
        {
            "Quarter": ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"],
            "Revenue": [150000, 175000, 192000, 210000],
            "Profit": [45000, 52500, 57600, 63000],
            "Growth (%)": [12.5, 16.7, 9.7, 9.4],
        }
    )

    # Use the template
    docdocgo.insert_table(data, "template.docx", "{{QUARTERLY_PERFORMANCE_DATA}}")
    print("✅ Template processed successfully!")
    print("📄 Check template.docx for the result")


if __name__ == "__main__":
    test_template()
