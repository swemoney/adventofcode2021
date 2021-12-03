# Day 3 Part 1

def run(data):
    gamma = ""
    idx = 0
    while idx < len(data[0]):
        one_bits = len(list(filter(lambda b: b[idx] == "1", data)))
        gamma += "1" if one_bits > len(data)/2 else "0"
        idx += 1
    epsilon = "".join(map(lambda b: "1" if b == "0" else "0", gamma))
    return int(gamma, 2) * int(epsilon, 2)

def parse_input(data):
    return data