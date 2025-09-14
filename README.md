# IFC-data-extraction-pipeline
A Python-based tool that automates the extraction of geometric and attribute data (e.g., volumes, areas) from IFC files, enabling efficient BIM data processing and analysis.

## Features
- Extract building volumes, areas, positions, and attributes from IFC files.
- Calculate geometric properties such as height, footprint perimeter, and side areas of walls and other building elements.
- Output the extracted data in a structured format (CSV, JSON, or database).
- Fully automated process for easy integration into BIM workflows.

## Requirements
- Python 3.x
- `ifcopenshell` library for processing IFC files

You can install the required dependencies by running:

```bash
pip install ifcopenshell
