# Day 10 Part 2

POINT_VALS = { ")": 1, "]": 2, "}": 3, ">": 4 }

def run(data):
    extra_chars = []
    for line in data:
        line_validity = is_line_valid(line)
        if line_validity[0] == True:
            extra_chars.append(line_validity[1])
    scores = sorted([calculate_score(chars) for chars in extra_chars])
    return scores[int(len(scores)/2)]

# Return (True, completion_chars) if valid or the first invalid char
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
    stack.reverse()
    return (not len(stack) == 0, "".join([ends[starts.index(c)] for c in stack]))

def calculate_score(chars):
    score = 0
    for c in chars:
        score *= 5
        score += POINT_VALS[c]
    return score

def parse_input(data):
    return data
