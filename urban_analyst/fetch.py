import osmnx as ox
import geopandas as gpd
from geopy.geocoders import Nominatim

def get_city_center(city):
    geolocator = Nominatim(user_agent="urban_analyst")
    location = geolocator.geocode(city)
    if not location:
        raise ValueError(f"City '{city}' not found!")
    return location.latitude, location.longitude

def fetch_urban_data(city_name, dist=500):
    lat, lon = get_city_center(city_name)
    print(f"Found {city_name} at: {lat:.4f}, {lon:.4f}")

    print("Fetching road network...")
    G = ox.graph_from_point(
        (lat, lon), dist=dist, network_type='drive')
    edges = ox.graph_to_gdfs(G, nodes=False)
    print(f"Found {len(edges)} road segments.")

    print("Fetching buildings and green spaces...")
    tags = {
        'building': True,
        'leisure': ['park', 'garden'],
        'landuse': ['grass', 'forest', 'meadow']
    }
    gdf_all = ox.features_from_point(
        (lat, lon), tags=tags, dist=dist)

    buildings = gdf_all[
        gdf_all['building'].notnull()].copy()
    green_spaces = gdf_all[
        gdf_all['leisure'].isin(['park', 'garden']) |
        gdf_all['landuse'].isin(
            ['grass', 'forest', 'meadow'])].copy()

    print(f"Found {len(buildings)} buildings.")
    print(f"Found {len(green_spaces)} green spaces.")

    return G, edges, buildings, green_spaces