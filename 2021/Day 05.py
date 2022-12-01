import os
import numpy as np
from comm import timed

def importData(fileName):
    return np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=int, skiprows=0, delimiter=",")

def addLine(line, map, diag = None):
    if line[0] == line[2]:
        if line[3] > line[1]: z = 1
        if line[3] < line[1]: z = -1
        for y in range(line[1],line[3]+z,z):
            map[y][line[0]] += 1
    elif line[1] == line[3]:
        if line[2] > line[0]: z = 1
        if line[2] < line[0]: z = -1
        for x in range(line[0],line[2]+z,z):
            map[line[1]][x] += 1
    elif diag:
        map = addDiag(line,map)
    return map

def addDiag(line,map):
    if line[3] > line[1]: t = 1
    if line[3] < line[1]: t = -1
    if line[2] > line[0]: u = 1
    if line[2] < line[0]: u = -1
    for x, y in zip(range(line[0],line[2]+u,u), range(line[1],line[3]+t,t)):
        map[y][x] += 1
    return map

@timed
def day05A(data):
    map = [[0 for i in range(1001)] for j in range(1001)]
    for line in data:
        map = addLine(line,map)
    count = 0
    for x in map:
        for y in x:
            if y > 1: count += 1
    return count

@timed
def day05B(data):
    map = [[0 for i in range(1001)] for j in range(1001)]
    for line in data:
        map = addLine(line,map,1)
    count = 0
    for x in map:
        for y in x:
            if y > 1: count += 1
    return count
    return


if __name__ == "__main__":
    data = importData("Day 05.txt")
    print(f"Day 05 A: {day05A(data)}")
    print(f"Day 05 B: {day05B(data)}")
