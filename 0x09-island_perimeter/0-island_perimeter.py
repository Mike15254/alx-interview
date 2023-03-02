

#!/usr/bin/python3
'''
contains island perimeter solution
'''


def island_perimeter(grid):
    '''
    island perimeter solution
    Reasoning: find the perimeter of all island squares, then
    subtract the sides that touch each other from the total perimeter
    If a side is shared between two squares, then we'll need to
    subtract 2 * side since each one of the two squares has that side
    bordering the neighbouring square
    '''
    if not grid or any(type(arr) != list for arr in grid):
        return 0
    if any(len(arr) != len(grid[0]) for arr in grid):
        return 0

    squares = connections = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                squares += 1
                # is there any neighbour to the right?
                if col < len(grid[0]) - 1 and grid[row][col + 1]:
                    connections += 1
                # is there any neighbour beneath the current square?
                if row < len(grid) - 1 and grid[row + 1][col]:
                    connections += 1
    return squares * 4 - 2 * connections
