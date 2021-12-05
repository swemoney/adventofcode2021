# Day 5 Part 1

def run(data):
    grid = plot_lines(data)
    overlaps = 0
    for row in grid:
        for num in row:
            if num > 1: overlaps += 1
    return overlaps

def plot_lines(data):
    grid = create_empty_grid(find_max(data), find_max(data,1))
    for line in data:
        if line[0][0] == line[1][0]: # matching x
            x = line[0][0]
            sorted_y = sorted([line[0][1], line[1][1]])
            r = range(sorted_y[0], sorted_y[1]+1)
            for y in r: grid[y][x] += 1
        elif line[0][1] == line[1][1]: # matching y
            y = line[0][1]
            sorted_x = sorted([line[0][0], line[1][0]])
            r = range(sorted_x[0], sorted_x[1]+1)
            for x in r: grid[y][x] += 1
    return grid

def create_empty_grid(width, height):
    return [[0 for _ in range(width+1)].copy() for _ in range(height+1)]

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
