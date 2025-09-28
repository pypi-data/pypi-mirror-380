"""
Example usage of docdocgo package installed from TestPyPI.

This demonstrates how to use the docdocgo package in a real project
to create a business report using a template with multiple markers.
"""

from datetime import datetime

import pandas as pd

import docdocgo


def main():
    """Main function demonstrating docdocgo package usage."""
    print("🚀 docdocgo TestPyPI Example Project")
    print("=" * 40)

    try:
        # Use the template in this directory
        template_path = "template.docx"
        result_path = "result.docx"

        print(f"📋 Using template: {template_path}")

        # Create quarterly financial data
        quarterly_data = pd.DataFrame(
            {
                "Quarter": ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"],
                "Revenue ($)": [125000, 142000, 158000, 171000],
                "Expenses ($)": [95000, 102000, 108000, 115000],
                "Profit ($)": [30000, 40000, 50000, 56000],
                "Margin (%)": [24.0, 28.2, 31.6, 32.7],
            }
        )

        # Create product inventory data
        product_data = pd.DataFrame(
            {
                "Product": [
                    "Enterprise Suite",
                    "Pro License",
                    "Basic Package",
                    "Add-on Module",
                ],
                "Units Sold": [1250, 2100, 3400, 850],
                "Price ($)": [299.99, 149.99, 49.99, 29.99],
                "Revenue ($)": [374988, 314979, 169966, 25492],
                "Category": ["Software", "Software", "Software", "Extension"],
            }
        )

        print("\n📊 Replacing {{QUARTERLY_DATA}} marker...")
        # Replace first marker with quarterly data
        docdocgo.insert_table(
            quarterly_data, template_path, "{{QUARTERLY_DATA}}", result_path
        )

        print("📦 Replacing {{PRODUCT_DATA}} marker...")
        # Replace second marker with product data (overwrite result.docx)
        docdocgo.insert_table(product_data, result_path, "{{PRODUCT_DATA}}")

        print("\n🎉 Report generated successfully!")
        print(f"📄 Output file: {result_path}")
        print(f"📊 Quarterly data: {quarterly_data.shape[0]} quarters")
        print(f"📦 Product data: {product_data.shape[0]} products")
        print(f"📅 Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
