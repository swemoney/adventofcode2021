# Day 7 Part 2

def run(data):
    lowest_fuel = None
    for pos in range(max(data)):
        fuel_cost = 0
        for crab in data:
            moves = abs(crab - pos)
            fuel_cost += ((moves * (moves + 1)) / 2)
        if lowest_fuel == None or fuel_cost < lowest_fuel:
            lowest_fuel = fuel_cost
    return lowest_fuel

def parse_input(data):
    return [int(p) for p in data[0].split(",")]
