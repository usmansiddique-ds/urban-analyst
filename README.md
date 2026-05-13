# Urban Analyst — GIS Pipeline

A Python CLI tool that fetches real OpenStreetMap data and produces geospatial analyses for any city.

## What It Does
- Fetches buildings, roads and green spaces from OSM.
- Reprojects data to correct metric CRS (UTM).
- Calculates building density per grid cell.
- Calculates green space coverage per grid cell.
- Calculates street network connectivity per grid cell.
- Exports GeoJSON files and summary statistics.
- Generates 3 static map PNG images.

## Setup

### 1. Clone the repository
git clone https://github.com/USMAN SIDDIQUE/urban-analyst.git
cd urban-analyst

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

## How to Run

### Using city name
python urban_analyst/cli.py --city "Bangalore, India"

### Using bounding box
python urban_analyst/cli.py --bbox 74.28 31.54 74.36 31.60

## Output Files
- output/buildings.geojson
- output/green_spaces.geojson
- output/grid.geojson
- output/summary_stats.json
- output/building_density.png
- output/slope_map.png
- output/street_connectivity.png

## CRS Design Notes
See CRS_NOTES.md for full explanation.
UTM zone is automatically detected from city location.

## Tools Used
- osmnx — OpenStreetMap data fetching
- geopandas — geospatial data processing
- pyproj — coordinate reference systems
- matplotlib — map visualization
- networkx — street network analysis
- click — CLI interface