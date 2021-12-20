# Day 18 Part 1

from functools import reduce
from math import ceil

def run(data):
    return magnitude(reduce(add, data))

def add(lhs, rhs):
    new_num = [[num, depth + 1] for num, depth in lhs + rhs]
    while True:
        new_num, changed = explode(new_num)
        if changed:
            continue
        new_num, changed = split(new_num)
        if not changed:
            break
    return new_num

def split(num):
    for i, (n, depth) in enumerate(num):
        if n > 9:
            return num[:i] + [[n//2, depth+1], [ceil(n/2), depth+1]] + num[i+1:], True
    return num, False

def explode(num):
    for i, ((num1,depth1), (num2,depth2)) in enumerate(zip(num, num[1:])):
        if depth1 < 5 or depth1 != depth2:
            continue
        if i > 0:
            num[i-1][0] += num1
        if i < len(num) - 2:
            num[i+2][0] += num2
        return num[:i] + [[0, depth1-1]] + num[i+2:], True
    return num, False

def magnitude(num):
    while len(num) > 1:
        for i, ((num1,depth1), (num2,depth2)) in enumerate(zip(num, num[1:])):
            if depth1 != depth2:
                continue
            new_num = (num1 * 3) + (num2 * 2)
            num = num[:i] + [[new_num, depth1-1]] + num[i+2:]
            break
    return num[0][0]

def flatten(datastring):
    ret = []
    depth = 0
    for char in datastring:
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char.isdigit():
            ret.append([int(char), depth])
    return ret

def parse_input(data):
    return [flatten(line) for line in data]
