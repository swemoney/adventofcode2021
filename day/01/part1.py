# Day 1 Part 1

def run(data):
    increases = 0
    for idx, depth in enumerate(data):
        if idx == 0: continue
        if depth > data[idx - 1]:
            increases += 1
    
    return increases

def parse_input(data):
    return [int(d) for d in data]
