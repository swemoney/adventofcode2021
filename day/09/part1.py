# Day 9 Part 1

def run(data):
    low_points = []
    for row, col in data:
        neighbors = find_neighbors(row, col)
        if all(data.get(neighbor, 9) > data[(row, col)] for neighbor in neighbors):
            low_points.append(data[(row, col)] + 1)
    return sum(low_points)

def find_neighbors(row, col):
    return [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

def parse_input(data):
    grid = {}
    for row, row_data in enumerate(data):
        for col, height in enumerate(row_data):
            grid[(row, col)] = int(height)
    return grid
