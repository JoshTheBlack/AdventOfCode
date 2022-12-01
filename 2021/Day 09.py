import os
import numpy as np
from collections import Counter
from comm import timed

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

def fix(data):
    for i, v in enumerate(data):
        data[i] = [int(char) for char in v]
    return data

def getCell(data, x, y):
    if x == -1 or y == -1:
        return 9
    try:
        return data[x][y]
    except:
        return 9

def neighbors(x,y):
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
    
@timed   
def day09A(data):
    lows = Counter()
    for i in range(len(data)):
        for j in range(len(data[i])):
            x = getCell(data,i,j)
            y1,y2 = getCell(data,i,j-1),getCell(data,i,j+1)
            x1,x2 = getCell(data,i-1,j),getCell(data,i+1,j)
            if (x < x1 and x < x2 and
                x < y1 and x < y2):
                lows[x] += 1
    answer = 0
    for k,v in lows.items():
        answer += (1+k) * v   
    return answer

@timed
def day09B(data):
    gridCoords = []
    for x in range(len(data)):
        for y in range(len(data[x])):
            gridCoords.append((x, y))
    basins = []
    for x, y in gridCoords:
        q = [(x, y)]
        seen = set(q)
        while q:
            q2 = []
            for i, j in q:
                for ni, nj in neighbors(i, j):
                    if ni >= 0 and ni < len(data) and nj >= 0 and nj <len(data[i]):
                        h_new = data[ni][nj]
                        if h_new != 9 and h_new > data[i][j]:
                            if (ni, nj) not in seen:
                                seen.add((ni, nj))
                                q2.append((ni, nj))
            q = q2
        basins.append(len(seen))
    basins.sort()
    return basins[-3] * basins[-2] * basins[-1]


if __name__ == "__main__":
    data = fix(list(importData("Day 09.txt")))
    print(f"Day 09 A: {day09A(data)}") # 456
    print(f"Day 09 B: {day09B(data)}") # 1047744