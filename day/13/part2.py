# Day 13 Part 2

def run(data):
    dots, folds = data
    for f in folds:
        dots = fold(dots, f)
    print_paper(dots)
    return len(dots)

def fold(dots, f):
    pos, axis = f
    for i, dot in enumerate(dots):
        if axis == 'y':
            if dot[1] > pos:
                diff = dot[1] - pos
                dots[i] = (dot[0], pos - diff)
        else:
            if dot[0] > pos:
                diff = dot[0] - pos
                dots[i] = (pos - diff, dot[1])
    return list(set(dots))

def print_paper(dots):
    x_max = max(map(lambda dot: dot[0], dots))
    y_max = max(map(lambda dot: dot[1], dots))
    grid = []
    for row in range(y_max+1):
        grid.append([" "] * (x_max+1))
    for dot in dots:
        grid[dot[1]][dot[0]] = 'X'
    for row in range(y_max+1):
        for col in range(x_max+1):
            print(grid[row][col], end='')
        print()

def parse_input(data):
    dots = []
    folds = []
    for line in data:
        if line == '': continue
        if "x=" in line:
            folds.append( (int(line.split('x=')[1]), 'x') )
            continue
        if "y=" in line:
            folds.append( (int(line.split('y=')[1]), 'y') )
            continue
        dots.append( (int(line.split(',')[0]), int(line.split(',')[1])) )
    return (dots, folds)
