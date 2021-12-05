# Day 5 Part 2

import numpy as np

def run(data):
    grid = plot_lines(data)
    overlaps = 0
    for row in grid:
        for num in row:
            if num > 1: overlaps += 1
    return overlaps

def plot_lines(data):
    grid = create_empty_grid(find_max(data), find_max(data,1))
    for line_data in data:
        line_points = get_line_points(line_data)
        for point in line_points:
            grid[point[1]][point[0]] += 1
    return grid

def get_line_points(ends): # https://stackoverflow.com/a/47705495/1390317
    ends = np.array(ends)
    diff_x, diff_y = np.abs(np.diff(ends, axis=0))[0]
    if diff_x > diff_y:
        return np.c_[np.linspace(ends[0, 0], ends[1, 0], diff_x + 1, dtype=np.int16),
                     np.round(np.linspace(ends[0, 1], ends[1, 1], diff_x + 1))
                     .astype(np.int16)]
    else:
        return np.c_[np.round(np.linspace(ends[0, 0], ends[1, 0], diff_y + 1))
                     .astype(np.int16),
                     np.linspace(ends[0, 1], ends[1, 1], diff_y + 1, dtype=np.int16)]

def create_empty_grid(width, height):
    return np.zeros([height, width], dtype=np.uint16)

def find_max(data, xy=0):
    res = 0
    for line in data:
        for point in line:
            if point[xy] > res:
                res = point[xy]
    return res + 1

def parse_input(data):
    line_strs = [line.split(" -> ") for line in data]
    return [([int(point) for point in line[0].split(",")], [int(point) for point in line[1].split(",")]) for line in line_strs]
