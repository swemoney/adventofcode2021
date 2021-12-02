# Day 2 Part 2

def run(data):
    h_pos = 0
    depth = 0
    aim = 0
    for inst in data:
        if inst[0] == "forward":
            h_pos += inst[1]
            depth += aim * inst[1]
        else:
            move = 1 if inst[0] == "down" else -1
            aim += inst[1] * move
    return h_pos * depth

def parse_input(data):
    instructions = []
    for inst in data:
        parts = inst.split(" ")
        instructions.append((parts[0], int(parts[1])))
    return instructions
