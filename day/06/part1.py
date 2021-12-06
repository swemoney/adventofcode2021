# Day 6 Part 1

def run(data):
    for day in range(80):
        curr_fish = data.copy()
        idx = 0
        while idx < len(curr_fish):
            data[idx] -= 1
            if data[idx] < 0:
                data[idx] = 6
                data.append(8)
            idx += 1
    return len(data)

def parse_input(data):
    return [int(age) for age in data[0].split(',')]