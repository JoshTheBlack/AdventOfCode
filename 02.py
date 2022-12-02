import os
#import numpy as np
from comm import timed

def importData(fileName):
    #return np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=int, skiprows=0)
    with open(fileName) as file:
        lines = file.read()
        groups = lines.split("\n")
    return [x for x in groups]

@timed
def runA(data):
    key = {"A X": 3, "A Y": 6, "A Z": 0, "B X": 0, "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3}
    score = 0
    for round in data:
        them = ord(round[0]) - 64
        us = ord(round[2]) - 87
        score += key[round] + us
    return score

@timed
def runB(data):
    key = {"A X": 3, "A Y": 1, "A Z": 2, "B X": 1, "B Y": 2, "B Z": 3, "C X": 2, "C Y": 3, "C Z": 1}
    score = 0
    for round in data:
        them = ord(round[0]) - 64
        us = ord(round[2]) - 88
        score += key[round] + (us * 3)
    return score

if __name__ == "__main__":
    data = importData("02.in")
    print(f"A: {runA(data)}") # 
    data = importData("02.in")
    print(f"B: {runB(data)}") # 

    '''A = Rock = 1
    B = Paper = 2
    C = Scissors = 3'''