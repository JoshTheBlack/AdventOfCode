import os
import numpy as np
from comm import timed

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

def testLine(line):
    chars = []
    valid = ["{","[", "<", "("]
    close = {"}" : "{", "]" : "[", ">" : "<", ")" : "("}
    open = {"{" : "}", "[" : "]", "<" : ">", "(" : ")"}
    for sym in line:
        if sym in valid:
            chars.append(sym)
        else:
            x = close[sym]
            if x == chars[-1]:
                chars.pop(-1)
            else:
                return sym, chars
    missing = []
    for sym in chars:
        missing.append(open[sym])
    return 1, missing

@timed
def day10A(data):
    score = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
    result = 0
    for line in data:
        x, _ = testLine(line)
        if x == 1: continue
        else: result += score[x]
    return result

@timed
def day10B(data):
    score = {")" : 1, "]" : 2, "}" : 3, ">" : 4}
    data2 = []
    for line in data:
        x, missing = testLine(line)
        if x == 1:
            total = 0
            for sym in reversed(missing):
                total *= 5
                total += score[sym]
            data2.append(total)
    y = len(data2) // 2
    return sorted(data2)[y]

if __name__ == "__main__":
    data = importData("Day 10.txt")
    print(f"Day 10 A: {day10A(data)}") # 271245
    print(f"Day 10 B: {day10B(data)}") # 1685293086