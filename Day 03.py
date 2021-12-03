import os
import numpy as np
from comm import timed

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

def findMostCommonBits(data, bit):
    x = 0
    for item in data:
        x += int(item[bit])

    if x > len(data) / 2:
        return 1
    elif x < len(data) / 2:
        return 0
    else:
        return 2

@timed
def day03A(data):
    epsilon = ""
    gamma = ""
    for i in range(len(data[0])):
        x = findMostCommonBits(data,i)
        gamma += str(x)
        epsilon += str(int(not x))
    
    return int(gamma,2) * int(epsilon,2)

@timed
def day03B(data):
    o2 = list(data)
    co2 = list(data)
    for i in range(len(data[0])):
        test = findMostCommonBits(o2, i)
        if test == 2: test = 1
        if len(o2) > 1:
            o3 = [item for item in o2 if int(item[i]) == test]
            o2 = o3

        test = findMostCommonBits(co2, i)
        if test == 2: test = 1
        if len(co2) > 1:
            co3 = [item for item in co2 if int(item[i]) != test]
            co2 = co3
   
    return int(o2[0],2) * int(co2[0],2)

if __name__ == "__main__":
    data = importData("Day 03.txt")
    print(day03A(data))
    # data = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    print(day03B(data))