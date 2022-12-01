import os
import numpy as np
from comm import timed

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

def fix(data):
    return [[int(char) for char in i] for i in data]

def buildDict(data):
    paths = {}
    for row in data:
        x,y = row.split("-")
        if x not in paths.keys(): paths[x] = []
        if y not in paths.keys(): paths[y] = []
        paths[x].append(y)
        paths[y].append(x)
    fPaths = paths.copy()
    return fPaths

@timed
def day12A(G):
    def add(e, path, qu):
        if e[0].lower() == e[0] and e in path: return
        path2 = path + [e]
        pathstr = ','.join(path2)
        if pathstr in visited: return
        qu.append(path2)
        visited.add(pathstr)

    qu = []
    visited = set()
    add('start', [], qu)
    while qu:
        qu2 = []
        for s in qu:
            u = s[-1]
            for v in G[u]:
                add(v, s, qu2)
        qu = qu2
    no = 0
    for SET in visited:
        if SET[-3:] == 'end':
            no += 1
    return no

@timed
def day12B(G):
    def add(e, path, hasD, qu):
        if e[0].lower() == e[0] and e in path: 
            if e == 'start' or e == 'end': return
            if hasD: return
            hasD = True
        path2 = path + [e]
        pathstr = ','.join(path2)
        if pathstr in visited: return
        qu.append((path2, hasD))
        visited.add(pathstr)

    qu = []
    visited = set()    
    add('start', [], False, qu)
    while qu:
        q2 = []
        for s, hasD in qu:
            u = s[-1]
            for v in G[u]:
                add(v, s, hasD, q2)
        qu = q2
    no = 0
    for SET in visited:
        if SET[-3:] == 'end':
            no += 1
    return no

if __name__ == "__main__":
    data = buildDict(importData("Day 12.txt"))
    print(f"Day 12 A: {day12A(data)}") # 5874
    data = buildDict(importData("Day 12.txt"))
    print(f"Day 12 B: {day12B(data)}") # 153592