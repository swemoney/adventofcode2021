from importlib import import_module

# tuple (day,part)
DAY = 1
PART = 1

def file_not_found(filename):
    print(f"Could not locate {filename}")
    print(f"Make sure it's present at ./day/{DAY:02}/{filename}")
    exit()

try:
    puzzle = import_module(f"day.{DAY:02}.part{PART}")
except ImportError:
    file_not_found(f"part{PART}.py")
    
try:
    with open(f"day/{DAY:02}/input.txt") as f:
        data = [l.rstrip('\n') for l in f.readlines()]
except FileNotFoundError:
    file_not_found("input.txt")

print(f"Running day {DAY}, part {PART}...")

puzzle.run(data)