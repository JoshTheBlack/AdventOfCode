import os
import numpy as np
from comm import timed

def importData(fileName):
    return int(str(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n")), 16)

def fix(data):
    return str(bin(data))[2:]

def getVT(bits, i):
    return int(bits[i:i+3], 2), int(bits[i+3: i+6])

def read(bits, i, no):
    return int(bits[i: i+no], 2), i + no

def parsePacket(bits, i):
    v, i = read(bits, i, 3)
    t, i = read(bits, i, 3)
    totV = v
    value = 0
    if t == 4:
        labels = []
        while 1:
            x, i = int(bits[i]), i+1    
            lab, i = read(bits, i, 4)
            labels.append(lab)
            if x == 0: break
        vs = 0
        for lab in labels:
            vs = vs*16 + lab
        value = vs
    else:
        values = []
        I, i = read(bits, i, 1)
        if I == 0: 
            L = 15
            totL, i = read(bits, i, L)
            si = i
            while i < si + totL:
                vsum, v, i = parsePacket(bits, i)
                totV += vsum
                values.append(v)
        else: 
            L = 11 
            no, i = read(bits, i, L)
            for _ in range(no):
                vsum, v, i = parsePacket(bits, i)
                totV += vsum
                values.append(v)
        if t == 0:
            value = sum(values)
        elif t == 1:
            value = 1
            for v in values:
                value *= v
        elif t == 2:
            value = min(values)
        elif t == 3:
            value = max(values)
        elif t == 5:
            value = 1 if values[0] > values[1] else 0
        elif t == 6:
            value = 1 if values[0] < values[1] else 0
        elif t == 7:
            value = 1 if values[0] == values[1] else 0
    return totV, value, i

@timed
def day16A(data):
    return parsePacket(data, 0)[0]

@timed
def day16B(data):
    return parsePacket(data, 0)[1]

if __name__ == "__main__":
    # Shamelessly stolen from reddit.  Couldn't crack this one myself.
    data = fix(importData("Day 16.txt"))
    print(f"Day 16 A: {day16A(data)}") # 
    data = fix(importData("Day 16.txt"))
    print(f"Day 16 B: {day16B(data)}") # 