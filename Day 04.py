import os
import numpy as np
from comm import timed
import math

def importData(fileName):
    return np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=int, skiprows=0, delimiter=" ")

def markNumber(number, data):
    for i in range(len(data)):
        for index, item in enumerate(data[i]):
            if item == number:
                data[i][index] = -1
    return data

def findWinner(data):
    result = []
    x = 0
    for index, item in enumerate(data):
        if sum(item) == -5: 
            x = 5 * math.floor(index / 5)
            for i in range(5):
                result.append(data[x + i])
            return result, x

    if len(data) > 5:
        for j in range(5):
            for k in range(0, len(data)-5, 5):
                wintest = data[k][j] + data[k+1][j] + data[k+2][j] + data[k+3][j] + data[k+4][j]
                if wintest == -5:
                    x = 5 * math.floor(k/5)
                    for i in range(5):
                        result.append(data[x + i])
    else:
        for j in range(5):
            for k in range(0, len(data), 5):
                wintest = data[k][j] + data[k+1][j] + data[k+2][j] + data[k+3][j] + data[k+4][j]
                if wintest == -5:
                    x = 5 * math.floor(k/5)
                    for i in range(5):
                        result.append(data[x + i])

    return result, x

@timed
def day03A(data, numbers):
    for number in numbers:
        data = markNumber(number, data)
        winner, _ = findWinner(data)
        if winner:
            result = 0
            for row in winner:
                for num in row:
                    if num != -1:
                        result += num
            
            return result * number

@timed
def day03B(data, numbers):
    for number in numbers:
        data = markNumber(number, data)
        winner, row = findWinner(data)
        if len(data) == 5:
            if winner:
                result = 0
                for row in data:
                    for num in row:
                        if num != -1:
                            result += num
                return result * number
        while winner:
            for i in range(4, -1, -1):
                data.pop(row + i)
            winner, row = findWinner(data)
    return

# Higher than 1100
# Lower than 15840


if __name__ == "__main__":
    data = list(importData("Day 04.txt"))
    numbers = [87,12,53,23,31,70,37,79,95,16,72,9,98,92,5,74,17,60,96,80,75,11,73,33,3,84,81,2,97,93,59,13,77,52,69,83,51,64,48,82,7,49,20,8,36,66,19,0,99,41,91,78,42,40,62,63,57,39,55,47,29,50,58,34,27,43,30,35,22,28,4,14,26,32,10,88,46,65,90,76,38,6,71,67,44,68,86,25,21,24,56,94,18,89,61,15,1,45,54,85]
    # numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    print(day03A(data,numbers))
    data = list(importData("Day 04.txt"))
    print(day03B(data,numbers))
