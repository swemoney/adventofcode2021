# Day 12 Part 1

from collections import defaultdict

def run(data):
    return path(data)

def path(data, cave="start", visited=set()):
    if cave.islower():
        visited.add(cave)

    paths = 0
    for next_cave in data[cave]:
        if next_cave == "end":
            paths += 1
        elif next_cave not in visited:
            paths += path(data, next_cave, visited.copy())
    return paths

def parse_input(data):
    connections = defaultdict(set)
    for line in data:
        points = line.split("-")
        connections[points[0]].add(points[1])
        connections[points[1]].add(points[0])
    return connections
