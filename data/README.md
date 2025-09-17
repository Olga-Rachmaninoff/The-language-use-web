# Project Overview

This project visualizes networks and language use. The visualizations include network graphs and Sankey diagrams, created with Python.

# Data Sources

The data is located in the `data/` folder and is available in the following formats:

- **CSV files** (`data/csv/`):
  - `interlocutors.csv`: Interlocutors
  - `media.csv`: Media
  - `places.csv`: Places
  - `situations.csv`: Situations
- **Excel files** (`data/xlsx/`):
  - Same content as the CSV files, but in Excel format
- **JSON files** (`data/json/`):
  - `all_informants_interlocutors.json`: All informants and interlocutors
  - `nodes_links.json`: Nodes and links for the network visualization

# Data Processing (Workflow)

The data is processed in several steps, each represented by a Python script in the `py/` folder:

## Step 1: CSV to JSON
- **Script:** `py/step1_CSVtoJSON.py`
- **Description:**
  - Reads the CSV files and converts them to JSON.
  - Goal: A uniform, machine-readable format for further processing.

## Step 2: Create nodes and links
- **Script:** `py/step2_createNodesAndLinks.py`
- **Description:**
  - Creates nodes and links for the network from the JSON data.
  - Saves the result in `data/json/nodes_links.json`.

## Step 3: Network Visualization
- **Script:** `py/step3_createNetwork.py`
- **Description:**
  - Uses the nodes and links to visualize a network (with pyvis).
  - The result is an interactive HTML file (`network.html`).

## Step 4: Sankey Diagram
- **Script:** `py/step4_createSankeyDiagram.py`
- **Description:**
  - Creates Sankey diagrams to visualize flows (with plotly).
  - Output as HTML file (`sankey.html`).
