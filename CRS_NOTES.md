# CRS Notes

## What is CRS?
CRS is Coordinate Reference System. It tells us how map coordinates relate to real locations on Earth.

## Why We Use UTM Instead of WGS84
WGS84 (EPSG:4326) uses degrees (latitude/longitude).
Degrees are not equal in size everywhere on Earth.
This makes area and distance calculations inaccurate.
UTM uses metres, which are equal everywhere. This makes area and distance calculations accurate.

## Our Choice
We automatically detect the correct UTM zone using the centroid of the study area.
For Lahore, Pakistan the correct CRS is EPSG:32643 (UTM Zone 43N).

## What Goes Wrong With WGS84
If we calculate building area in WGS84 degrees, we get wrong numbers. A building that is 100m x 50m would show incorrect area in degree-based systems.