import os
import numpy as np
from comm import timed

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), skiprows=0, delimiter=" "))

def buildSummedTripletArray(data, output = []):
    for i in range(len(data)):
        if i < 2: continue

        output.append(data[i-2] + data[i-1] + data[i])

    return output

@timed
def advent01(data, total = 0):
    for i in range(len(data)):
        if data[i] > data[i-1]:
            total += 1
    
    return total

if __name__ == "__main__":
    print(advent01(buildSummedTripletArray(importData("001.txt"))))