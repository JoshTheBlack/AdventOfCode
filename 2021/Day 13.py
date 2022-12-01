import os
import numpy as np
from comm import timed

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

def fix(data):
    data = [i.split(',') for i in data]
    return [[int(x) for x in i] for i in data]

def buildGrid(x = 900):
    return [[' ' for i in range(x+1)] for _ in range(x+1)]

def fold(dots, axis, location):
    if axis == 'x':
        ndata = []
        for i in range(len(dots)):
            if dots[i][0] <= location: 
                ndata.append(tuple(dots[i]))
                continue
            a = tuple(dots[i])
            offset = a[0] - location
            ndata.append((location - offset, a[1]))
    if axis == 'y':
        ndata = []
        for i in range(len(dots)):
            a = tuple(dots[i])
            if a[1] <= location:
                ndata.append(a)
                continue
            offset = a[1] - location
            ndata.append((a[0],location - offset))
    return ndata

@timed
def day13A(data,folds):
    x = fold(data, folds[0][0], folds[0][1])
    return len(set(x))


@timed
def day13B(data, folds):
    for axis,location in folds:
        data = fold(data,axis,location)
    grid = buildGrid(max(max(data)))
    for x,y in data:
        grid[y][x] = "1"
    for row in grid:
        print("".join(row))
    return

if __name__ == "__main__":
    data = fix(importData("Day 13.txt"))
    folds = [('x',655),('y',447),('x',327),('y',223),('x',163),('y',111),('x',81),('y',55),('x',40),('y',27),('y',13),('y',6)]
    print(f"Day 13 A: {day13A(data, folds)}") # 
    data = fix(importData("Day 13.txt"))
    print(f"Day 13 B: {day13B(data, folds)}") # 