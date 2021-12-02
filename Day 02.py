import os
import numpy as np
from comm import timed

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

@timed
def day02A(data):
    x,y,aim = 0,0,0
    for command in data:
        if command[0].lower() == 'f':
            x += int(command[-1])
        elif command[0].lower() == 'u': 
            y -= int(command[-1])
        elif command[0].lower() == 'd':
            y += int(command[-1])
        else:
            print("Error")
    return x * y

@timed
def day02B(data):
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
    data = importData("Day 02.txt")
    print(f"Challenge 1: {day02A(data)}")
    print(f"Challenge 2: {day02B(data)}")