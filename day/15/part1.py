# Day 15 Part 1

import networkx as nx

def run(data):
    graph = networkx_graph(data)
    path = nx.shortest_path(graph, source=(0,0), target=(len(data)-1,len(data)-1), weight='weight')
    risk = 0
    for point in path[1:]: # Skip starting point
        risk += data[point[0]][point[1]]
    return risk

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
