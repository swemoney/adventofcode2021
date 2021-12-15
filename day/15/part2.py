# Day 15 Part 2

import networkx as nx

def run(data):
    expanded = expanded_grid(data)
    graph = networkx_graph(expanded)
    path = nx.shortest_path(graph, source=(0,0), target=(len(expanded)-1,len(expanded)-1), weight='weight')
    risk = 0
    for point in path[1:]: # Skip starting point
        risk += expanded[point[0]][point[1]]
    return risk

def expanded_grid(grid, times=5):
    new_grid = []
    for _ in range(len(grid) * times):
        new_grid.append([0] * (len(grid) * times))
    for x_inc in range(5):
        for y_inc in range(5):
            for row, row_data in enumerate(grid):
                for col, risk in enumerate(row_data):
                    curr_x = row + (len(grid) * x_inc)
                    curr_y = col + (len(grid) * y_inc)
                    new_grid[curr_x][curr_y] = risk + (x_inc + y_inc)
                    if new_grid[curr_x][curr_y] > 9:
                        new_grid[curr_x][curr_y] -= 9
    return new_grid

def networkx_graph(grid):
    graph = nx.DiGraph()
    for x in range(len(grid)):
        for y in range(len(grid)):
            graph.add_node((x,y))
            for delta_x,delta_y in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_x = x + delta_x
                new_y = y + delta_y
                if 0 <= new_x and new_x < len(grid) and 0 <= new_y and new_y < len(grid):
                    graph.add_edge((x,y), (new_x,new_y), weight=grid[new_x][new_y])
    return graph

def parse_input(data):
    grid = []
    for line in data:
        grid.append([int(risk) for risk in list(line)])
    return grid
