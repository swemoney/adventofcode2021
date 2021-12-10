# Day 9 Part 2

import math

def run(data):
    basins = []
    low_points = find_low_points(data)
    for low_point in low_points:
        basin = {low_point}
        fill_basin(data, basin, low_point)
        basins.append(basin)
    sorted_basins = sorted([len(b) for b in basins])
    return math.prod(sorted_basins[-3:])

def fill_basin(grid, basin, point):
    for neighbor in find_neighbors(point[0], point[1]):
        neighbor_height = grid.get(neighbor, 9)
        if neighbor_height > grid[point] and neighbor_height != 9:
            basin.add(neighbor)
            fill_basin(grid, basin, neighbor)

def find_low_points(grid):
    low_points = []
    for row, col in grid:
        neighbors = find_neighbors(row, col)
        if all(grid.get(neighbor, 9) > grid[(row, col)] for neighbor in neighbors):
            low_points.append((row, col))
    return low_points

def find_neighbors(row, col):
    return [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

def parse_input(data):
    grid = {}
    for row, row_data in enumerate(data):
        for col, height in enumerate(row_data):
            grid[(row, col)] = int(height)
    return grid
