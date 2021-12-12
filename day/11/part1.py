# Day 11 Part 2

def run(grid):
    flashes = 0
    for step in range(100):
        # Add 1 to everyone's energy
        for coords in grid:
            grid[coords] += 1

        # Keep track of the octopuses who have flashed this step
        flashed = set()

        # Find all the octopuses who are ready to flash
        flashers = find_flashers(grid, flashed)

        # Loop through and flash all of the flashers
        flash_flashers(grid, flashers, flashed)

        # Reset flashed octopuses
        for coords in flashed:
            grid[coords] = 0

        flashes += len(flashed)
        
    return flashes

def flash_flashers(grid, flashers, flashed):
    extra_flashers = set()
    flashed.update(flashers)
    for flasher in flashers:
        flash(grid, flasher, flashed, extra_flashers)
    if len(extra_flashers) > 0:
        flash_flashers(grid, extra_flashers, flashed)

def flash(grid, flasher, flashed, extra_flashers):
    for neighbor in find_neighbors(flasher):
        if grid.get(neighbor) != None:
            grid[neighbor] += 1
            if grid[neighbor] > 9 and neighbor not in flashed:
                extra_flashers.add(neighbor)

def find_flashers(grid, flashed):
    return [coords for coords, energy in grid.items() if energy > 9]

def find_neighbors(coords):
    row, col = coords
    return [
        (row - 1, col - 1),
        (row - 1, col    ),
        (row - 1, col + 1),
        (row,     col - 1),
        (row,     col + 1),
        (row + 1, col - 1),
        (row + 1, col    ),
        (row + 1, col + 1)]

def display_grid(grid):
    for row in range(10):
        for col in range(10):
            print(grid[(row, col)], end='')
        print()

def parse_input(data):
    grid = {}
    for row, row_data in enumerate(data):
        for col, energy in enumerate(row_data):
            grid[(row, col)] = int(energy)
    return grid

    