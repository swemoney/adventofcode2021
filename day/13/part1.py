# Day 13 Part 1

def run(data):
    dots, folds = data
    return len(fold(dots, folds[0]))

def fold(dots, fold):
    pos, axis = fold
    for i, dot in enumerate(dots):
        if axis == 'y':
            if dot[1] > pos:
                diff = dot[1] - pos
                dots[i] = (dot[0], pos - diff)
        if axis == 'x':
            if dot[0] > pos:
                diff = dot[0] - pos
                dots[i] = (pos - diff, dot[1])
    return list(set(dots))

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
