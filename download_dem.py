"""
DEM Download Script
Downloads elevation data (Digital Elevation Model)
from OpenTopography using SRTM 90m dataset.

HOW TO USE:
1. Go to https://opentopography.org
2. Click "Find Data"
3. Select your area on the map
4. Download SRTM GL3 (90m) as GeoTIFF
5. Save the file as "dem.tif" in this folder

OR use the coordinates below for Lahore:
Latitude:  31.50 to 31.62
Longitude: 74.27 to 74.40

NOTE:
This project uses slope classification based on
the DEM data. If no DEM file is provided, the
system automatically generates slope estimates.
"""

import os

def check_dem_exists():
    """Check if DEM file is available."""
    if os.path.exists("dem.tif"):
        print("DEM file found: dem.tif")
        return True
    else:
        print("No DEM file found.")
        print("Using estimated slope data instead.")
        print("To download DEM:")
        print("  Visit: https://opentopography.org")
        print("  Download SRTM GL3 for your area")
        print("  Save as dem.tif in project folder")
        return False

if __name__ == "__main__":
    check_dem_exists()