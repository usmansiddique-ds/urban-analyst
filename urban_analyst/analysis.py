import geopandas as gpd
import numpy as np
from shapely.geometry import box
import networkx as nx

def make_grid(gdf, cell_size=200):
    """Divide the area into a grid of squares."""
    bounds = gdf.total_bounds
    xmin, ymin, xmax, ymax = bounds
    cols = int((xmax - xmin) / cell_size) + 1
    rows = int((ymax - ymin) / cell_size) + 1
    cells = []
    for i in range(cols):
        for j in range(rows):
            x1 = xmin + i * cell_size
            y1 = ymin + j * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            cells.append(box(x1, y1, x2, y2))
    grid = gpd.GeoDataFrame(geometry=cells, crs=gdf.crs)
    return grid

def building_density(grid, buildings):
    """Calculate building density per grid cell."""
    print("Calculating building density...")
    joined = gpd.sjoin(buildings, grid,
                       how='left', predicate='intersects')
    cell_area_ha = (grid.geometry.area / 10000)
    counts = joined.groupby('index_right').size()
    areas = joined.groupby('index_right')[
        'geometry'].apply(
        lambda x: x.area.sum())
    grid = grid.copy()
    grid['building_count'] = counts.reindex(
        grid.index, fill_value=0)
    grid['built_area_m2'] = areas.reindex(
        grid.index, fill_value=0)
    grid['cell_area_ha'] = cell_area_ha
    grid['building_density'] = (
        grid['building_count'] /
        grid['cell_area_ha'])
    grid['built_fraction'] = (
        grid['built_area_m2'] /
        grid.geometry.area)
    return grid

def green_space_coverage(grid, green_spaces):
    """Calculate green space per grid cell."""
    print("Calculating green space coverage...")
    grid = grid.copy()
    grid['green_area_m2'] = 0.0
    grid['green_fraction'] = 0.0
    if len(green_spaces) == 0:
        return grid
    joined = gpd.sjoin(green_spaces, grid,
                       how='left',
                       predicate='intersects')
    areas = joined.groupby('index_right')[
        'geometry'].apply(
        lambda x: x.area.sum())
    grid['green_area_m2'] = areas.reindex(
        grid.index, fill_value=0)
    grid['green_fraction'] = (
        grid['green_area_m2'] /
        grid.geometry.area)
    return grid

def street_connectivity(grid, G):
    """Calculate street network metrics per grid cell."""
    print("Calculating street connectivity...")
    grid = grid.copy()
    grid['node_count'] = 0
    grid['dead_ends'] = 0
    grid['connectivity'] = 0.0
    if G is None:
        return grid
    nodes, edges = None, None
    try:
        import osmnx as ox
        nodes, edges = ox.graph_to_gdfs(G)
        nodes = nodes.to_crs(grid.crs)
    except:
        return grid
    joined = gpd.sjoin(nodes, grid,
                       how='left',
                       predicate='intersects')
    counts = joined.groupby('index_right').size()
    degrees = {n: d for n, d in G.degree()}
    joined['degree'] = joined.index.map(
        lambda x: degrees.get(x, 0))
    dead_ends = joined[
        joined['degree'] == 1].groupby(
        'index_right').size()
    grid['node_count'] = counts.reindex(
        grid.index, fill_value=0)
    grid['dead_ends'] = dead_ends.reindex(
        grid.index, fill_value=0)
    grid['connectivity'] = np.where(
        grid['node_count'] > 0,
        1 - (grid['dead_ends'] /
             grid['node_count']), 0)
    return grid