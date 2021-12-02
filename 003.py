import os
import numpy as np
from comm import timed

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

@timed
def advent03(data):
    x,y,aim = 0,0,0
    for command in data:
        if command[0].lower() == 'f':
            x += int(command[-1])
            y += int(command[-1]) * aim
        elif command[0].lower() == 'u': 
            aim -= int(command[-1])
        elif command[0].lower() == 'd':
            aim += int(command[-1])
        else:
            print("Error")
    return x * y

if __name__ == "__main__":
    print(advent03(importData("003.txt")))