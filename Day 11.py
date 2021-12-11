import os
import numpy as np
from comm import timed

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

def fix(data):
    return [[int(char) for char in i] for i in data]

def neighbors(x,y):
    return [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]

def step1(data):
    for row in data:
        for k in range(len(row)):
            row[k] += 1
    return step2(data)

def step2(data):
    flashed = {}
    run = 1
    while run:
        run = 0
        for i,row in enumerate(data):
            for k,v in enumerate(row):
                if v > 9 and (i,k) not in flashed.keys():
                    flashed[(i,k)] = 1
                    n = neighbors(i,k)
                    for x,y in n:
                        if x >= 0 and x < len(data) and y >= 0 and y < len(data[x]):
                            data[x][y] += 1
                            if data[x][y] == 10: run = 1
    return step3(data, flashed)

def step3(data, flashed):
    flash = 0
    for x,y in flashed.keys():
        flash += 1
        data[x][y] = 0
    return data, flash, len(flashed)

@timed
def day11A(data):
    count = 0
    for _ in range(100):
        data, i, _ = step1(data)
        count += i
    return count

@timed
def day11B(data):
    step = 0
    while True:
        data, _, count = step1(data)
        step += 1
        if count == 100: return step
    return

if __name__ == "__main__":
    data = fix(importData("Day 11.txt"))
    print(f"Day 11 A: {day11A(data)}") # 1620
    data = fix(importData("Day 11.txt"))
    print(f"Day 11 B: {day11B(data)}") # 371