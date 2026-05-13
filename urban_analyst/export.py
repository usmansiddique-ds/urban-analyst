import json
import os
import geopandas as gpd

OUTPUT_DIR = "output"

def save_geojson(gdf, filename):
    """Save a GeoDataFrame as GeoJSON."""
    if gdf is None or len(gdf) == 0:
        print(f"Skipping {filename} — no data.")
        return
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)
    gdf_wgs = gdf.to_crs(epsg=4326)
    gdf_wgs.to_file(path, driver='GeoJSON')
    print(f"Saved {filename} ({len(gdf)} features)")

def save_summary(grid, buildings, green_spaces, edges):
    """Save summary statistics as JSON."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    summary = {
        "total_buildings": int(len(buildings)),
        "total_green_spaces": int(len(green_spaces)),
        "total_road_segments": int(len(edges)),
        "grid_cells": int(len(grid)),
        "avg_building_density": round(float(
            grid['building_density'].mean()), 2),
        "max_building_density": round(float(
            grid['building_density'].max()), 2),
        "avg_green_fraction": round(float(
            grid['green_fraction'].mean()), 4),
        "avg_connectivity": round(float(
            grid['connectivity'].mean()), 4),
    }
    path = os.path.join(OUTPUT_DIR, "summary_stats.json")
    with open(path, 'w') as f:
        json.dump(summary, f, indent=2)
    print("Saved summary_stats.json")
    print(json.dumps(summary, indent=2))