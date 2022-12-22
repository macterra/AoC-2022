import numpy as np

data = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""

def makeGrid(lines):
    w = max([len(line) for line in lines])
    h = len(lines)
    grid = np.full((h,w), ' ')
    for i in range(h):
        for j in range(len(lines[i])):
            grid[i,j] = lines[i][j]
    return grid

def printGrid(grid):
    h, w = grid.shape
    for row in range(h):
        print("".join(grid[row,:]))

def makeDirections(path):
    return []

def parse(map, path):
    lines = map.split('\n')
    grid = makeGrid(lines)
    directions = makeDirections(path)
    return grid, directions

#data = open('data', 'r').read()
map, path = data.split('\n\n')
grid, directions = parse(map, path)
printGrid(grid)
print(directions)

print(grid[0,], np.where(grid[0,] == '.'), min(np.where(grid[0,] == '.')[0]))
