# Day 8 Part 1

NUM_SEGMENTS = {
    1: 2,
    4: 4,
    7: 3,
    8: 7,
}

def run(data):
    occurrences = 0
    for entry in data:
        for digit in entry["output"]:
            if len(digit) in [NUM_SEGMENTS[1], NUM_SEGMENTS[4], NUM_SEGMENTS[7], NUM_SEGMENTS[8]]:
                occurrences += 1
    return occurrences

def parse_input(data):
    return [{"digits":part[0].split(), "output":part[1].split()} for part in [entry.split(" | ") for entry in data]]
