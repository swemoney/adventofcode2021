# Day 7 Part 1

def run(data):
    lowest_fuel = sum(data)
    for pos in range(max(data)):
        fuel_cost = 0
        for crab in data:
            fuel_cost += abs(crab - pos)
        if fuel_cost < lowest_fuel:
            lowest_fuel = fuel_cost
    return lowest_fuel

def parse_input(data):
    return [int(p) for p in data[0].split(",")]
