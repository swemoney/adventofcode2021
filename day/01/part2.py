# Day 1 Part 2

def run(data):
    increases = 0
    idx = -1
    while idx < len(data):
        idx += 1
        if idx < 3: continue
        if sum(data[idx-2:idx+1]) > sum(data[idx-3:idx]):
            increases += 1
    
    return increases

def parse_input(data):
    return [int(d) for d in data]
