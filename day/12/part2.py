# Day 12 Part 2

from collections import defaultdict

def run(data):
    return path(data)

def path(data, cave="start", visited=set(), visitedTwice=False):
    if cave in visited and visitedTwice == False:
        visitedTwice = True

    if cave.islower():
        visited.add(cave)

    paths = 0
    for next_cave in data[cave]:
        if next_cave == "end":
            paths += 1
        elif valid_next_cave(next_cave, visited, visitedTwice):
            paths += path(data, next_cave, visited.copy(), visitedTwice)
    return paths

def valid_next_cave(cave, visited, visitedTwice):
    if cave == "start":
        return False
    if visitedTwice == False:
        return True
    if cave not in visited:
        return True
    return False

def parse_input(data):
    connections = defaultdict(set)
    for line in data:
        points = line.split("-")
        connections[points[0]].add(points[1])
        connections[points[1]].add(points[0])
    return connections
