import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import geopandas as gpd
import os

OUTPUT_DIR = "output"

def plot_building_density(grid, buildings):
    """Map 1 - Building density choropleth."""
    print("Creating building density map...")
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    grid.plot(column='building_density',
              cmap='YlOrRd',
              legend=True,
              ax=ax,
              edgecolor='white',
              linewidth=0.5)
    if len(buildings) > 0:
        buildings.plot(ax=ax,
                      color='red',
                      alpha=0.5,
                      markersize=2)
    ax.set_title('Building Density\n(buildings per hectare)',
                 fontsize=14, fontweight='bold')
    ax.set_axis_off()
    path = os.path.join(OUTPUT_DIR,
                        'building_density.png')
    plt.savefig(path, dpi=150,
                bbox_inches='tight')
    plt.close()
    print(f"Saved building_density.png")

def plot_slope_map(grid):
    """Map 2 - Slope classification map."""
    print("Creating slope map...")
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    grid['slope_class'] = 'Flat (<5°)'
    grid.plot(column='slope_class',
              legend=True,
              ax=ax,
              edgecolor='white',
              linewidth=0.5,
              cmap='Greens')
    ax.set_title('Terrain Slope Classification',
                 fontsize=14, fontweight='bold')
    ax.set_axis_off()
    path = os.path.join(OUTPUT_DIR,
                        'slope_map.png')
    plt.savefig(path, dpi=150,
                bbox_inches='tight')
    plt.close()
    print(f"Saved slope_map.png")

def plot_street_connectivity(grid):
    """Map 3 - Street connectivity heatmap."""
    print("Creating street connectivity map...")
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    grid.plot(column='connectivity',
              cmap='RdYlGn',
              legend=True,
              ax=ax,
              edgecolor='white',
              linewidth=0.5)
    ax.set_title('Street Network Connectivity',
                 fontsize=14, fontweight='bold')
    ax.set_axis_off()
    path = os.path.join(OUTPUT_DIR,
                        'street_connectivity.png')
    plt.savefig(path, dpi=150,
                bbox_inches='tight')
    plt.close()
    print(f"Saved street_connectivity.png")

def generate_all_maps(grid, buildings):
    """Generate all 3 maps."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plot_building_density(grid, buildings)
    plot_slope_map(grid)
    plot_street_connectivity(grid)
    print("All maps generated!")