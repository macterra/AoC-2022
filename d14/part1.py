import numpy as np

data = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

def parse(lines):
    paths = []
    for line in lines:
        points = line.split(' -> ')
        path = []
        for point in points:
            x, y = point.split(',')
            path.append((int(x), int(y)))
        paths.append(path)
    return paths

def makeGrid(paths):
    print(paths)
    rows = 0
    cols = 0
    minx = 10000
    miny = 10000
    for path in paths:
        for x,y in path:
            cols = max(cols, x)
            rows = max(rows, y)
            minx = min(minx, x)
            miny = min(miny, y)

    print(rows)
    grid = np.full((rows+1,cols+1), '.')

    for path in paths:
        for i in range(len(path)-1):
            x1, y1 = path[i]
            x2, y2 = path[i+1]
            print("from {}:{} to {}:{}".format(x1, y1, x2, y2))

            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)
            grid[y1:y2+1,x1:x2+1] = '#'

    return grid, minx, miny

lines = data.split('\n')
paths = parse(lines)
grid, minx, miny = makeGrid(paths)
print(grid.shape)
print(minx, miny)

grid[0:1,500:501] = '+'

w,h = grid.shape
for row in range(w):
    print(row, "".join(grid[row,:][minx:]))