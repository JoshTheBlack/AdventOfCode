import os
import numpy as np
from comm import timed

def importData(fileName):
    #return np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=int, skiprows=0)
    with open(fileName) as file:
        lines = file.read()
        groups = [ grp.split("\n") for grp in lines.split("\n\n") ]
    return [[int(x) for x in l] for l in groups]

@timed
def runA(data):
    sums = []
    for x in data:
        sums.append(sum(x))
    return max(sums)

@timed
def runB(data):
    sums = []
    for x in data:
        sums.append(sum(x))
    sums.sort(reverse=True)
    return sums[0] + sums[1] + sums[2]

if __name__ == "__main__":
    data = importData("01.in")
    print(f"Day 11 A: {runA(data)}") # 
    data = importData("01.in")
    print(f"Day 11 B: {runB(data)}") # 