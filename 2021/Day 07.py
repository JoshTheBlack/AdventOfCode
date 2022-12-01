import os
import numpy as np
import math
from comm import timed

def importData(fileName):
    return np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=int, skiprows=0, delimiter=",")

def sumOfDigitsFrom1ToN(n):
    return sum(range(n+1))

@timed
def day07A(data):
    fuel = []
    for i in range(max(data)):
        x = 0
        for crab in data:
            x += abs(crab - i)
        fuel.append(x)
    return min(fuel)

@timed
def day07B(data):
    fuel = []
    for i in range(max(data)):
        x = 0
        for crab in data:
            x += abs(sumOfDigitsFrom1ToN(abs(crab - i)))
        fuel.append(x)
    return min(fuel)

if __name__ == "__main__":
    data = importData("Day 07.txt")
    print(f"Day 07 A: {day07A(data)}")
    print(f"Day 07 B: {day07B(data)}")