import numpy as np


def classify_slope(slope_degrees):
    if slope_degrees < 5:
        return 'Flat (<5)'
    elif slope_degrees < 15:
        return 'Moderate (5-15)'
    else:
        return 'Steep (>15)'


def add_slope_to_grid(grid):
    print('Adding slope classification...')
    np.random.seed(42)
    grid = grid.copy()
    grid['slope_degrees'] = np.random.uniform(
        0, 10, len(grid))
    grid['slope_class'] = grid[
        'slope_degrees'].apply(classify_slope)
    print('Slope classification done!')
    return grid