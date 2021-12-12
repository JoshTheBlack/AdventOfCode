import os
import numpy as np
from comm import timed

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

def fix(data):
    return [[int(char) for char in i] for i in data]


@timed
def day12A(data):
    
    return

@timed
def day12B(data):
    
    return

if __name__ == "__main__":
    data = fix(importData("Day 12.txt"))
    print(f"Day 11 A: {day12A(data)}") # 
    data = fix(importData("Day 12.txt"))
    print(f"Day 11 B: {day12B(data)}") # 