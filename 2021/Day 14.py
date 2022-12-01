import os
import numpy as np
from comm import timed
from collections import Counter

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

def fix(data):
    key = {}
    for i in data:
        j,k = i.split(" -> ")
        key[j] = k 
    return key

def step(C):
    C2 = Counter()
    for k, v in C.items():
        if k in rules:
            C2[k[0] + rules[k]] += v
            C2[rules[k] + k[1]] += v
        else:
            C2[k] += v
    return C2

def count(C):
    C2 = Counter()
    for k, v in C.items():
        C2[k[0]] += v
    return sorted(C2.values())

@timed
def day14(protein, times):
    C = Counter()
    for i in range(len(protein) - 1):
        C[protein[i:i+2]] += 1
    C[protein[-1]] += 1
    for _ in range(times):
        C = step(C)
    lst = count(C)
    return lst[-1] - lst[0]

if __name__ == "__main__":
    data = "PFVKOBSHPSPOOOCOOHBP"
    rules = fix(importData("Day 14.txt"))
    print(f"Day 14 A: {day14(data, 10)}") # 2937
    print(f"Day 14 B: {day14(data, 40)}") # 3390034818249