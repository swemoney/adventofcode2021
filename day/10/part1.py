# Day 10 Part 1

POINT_VALS = { ")": 3, "]": 57, "}": 1197, ">": 25137 }

def run(data):
    bad_chars = []
    for line in data:
        line_validity = is_line_valid(line)
        if line_validity != True:
            bad_chars.append(line_validity)
    return calculate_score(bad_chars)

# Return True if the line is valid or the first invalid character
def is_line_valid(line, starts="({[<", ends=")}]>"):
    stack = []
    for char in line:
        if char in starts:
            stack.append(char)
        elif char in ends:
            if len(stack) == 0:
                return char
            else:
                popped = stack.pop()
                if popped != starts[ends.index(char)]:
                    return char
    return not len(stack) == 0

def calculate_score(chars):
    scores = []
    for char, points in POINT_VALS.items():
        scores.append(points * chars.count(char))
    return sum(scores)

def parse_input(data):
    return data
