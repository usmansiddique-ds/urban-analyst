import geopandas as gpd
from pyproj import CRS

def get_utm_crs(gdf):
    """Automatically find the best metric CRS for the area."""
    centroid = gdf.geometry.unary_union.centroid
    utm_crs = CRS.from_dict({
        'proj': 'utm',
        'zone': int((centroid.x + 180) / 6) + 1,
        'south': centroid.y < 0
    })
    return utm_crs.to_epsg()
def reproject(gdf, crs = None):
    """Reproject a GeoDataFrame to metric CRS."""
    if gdf is None or len(gdf) == 0:
        return gdf
    if crs is None:
        crs = get_utm_crs(gdf)
    return gdf.to_crs(epsg=crs)