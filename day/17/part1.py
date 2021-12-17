# Day 17 Part 1

def run(data):
    xrng, yrng = data
    return simulate_all(xrng, yrng)

def simulate_all(xrng, yrng):
    max_y = 0
    for xv in range(max(xrng)):
        for yv in range(abs(min(yrng))):
            height_reached = simulate_launch(xv, yv, xrng, yrng)
            if height_reached != None and height_reached > max_y:
                max_y = height_reached
    return max_y

def simulate_launch(xv, yv, xrng, yrng, x=0, y=0):
    max_y = 0
    while y >= min(yrng):
        x, y, xv, yv = step(x, y, xv, yv)
        if y > max_y:
            max_y = y
        if x in xrng and y in yrng:
            return max_y
    return None

def step(x, y, xvel, yvel):
    x += xvel
    y += yvel
    yvel -= 1
    if xvel > 0:
        xvel -= 1
    elif xvel < 0:
        xvel += 1
    return x, y, xvel, yvel

def parse_input(data):
    x, y = data[0].split(": ")[1].split(", ")
    x_range = x.split("=")[1]
    y_range = y.split("=")[1]
    x1, x2 = x_range.split("..")
    y1, y2 = y_range.split("..")
    return range(int(x1), int(x2)+1), range(int(y1), int(y2)+1)
