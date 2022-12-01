import os
import numpy as np
from collections import Counter
from itertools import permutations
from comm import timed

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

def match(code):
    digs = {
        'abcefg' : 0,
        'cf' : 1,
        'acdeg' : 2,
        'acdfg' : 3,
        'bcdf' : 4,
        'abdfg' : 5,
        'abdefg' : 6,
        'acf' : 7,
        'abcdefg' : 8,
        'abcdfg' : 9
    }
    count = 0
    key = {}
    for p in permutations('abcdefg'):
        for digit in code:
            test = []
            for line in digit:
                test.append(p[ord(line) - ord('a')])
            a = "".join(sorted(test))
            b = "".join(sorted(digit))
            if a in digs: 
                key[b] = digs[a]
            else: break
        if len(key) == len(code): 
            return key

def decodeKey(data):
    key = ['','','','','','','']
    zero, one, two, three, four, five, six, seven, eight, nine = 0,0,0,0,0,0,0,0,0,0
    for i in data:
        if len(i) == 2: one = i
        elif len(i) == 3: seven = i
        elif len(i) == 4: four = i
        elif len(i) == 7: eight = i
        if one and seven and four and eight: break
    for letter in seven:
        if letter not in one: key[0] = letter
        else: 
            key[2] += letter
            key[5] += letter
    for i in data:
        if len(i) == 6:
            unknown = ''
            count = 0
            for letter in i:
                if letter in key[2]: count += 1
            if count == 1:
                ab = key[2]
                for letter in i:
                    if letter in key[2]:
                        key[5] = letter
                for letter in ab:
                    if letter not in key[5]:
                        key[2] = letter
        if len(key[2]) == 1 and len(key[5]) == 1: break
    for i in data:
        if len(i) == 5:
            unknown = ''
            count = 0
            for letter in i:
                if letter in key[2]: count += 1
                elif letter in key[5]: count += 2
                elif letter in key[0]: continue
                else: unknown += letter
            if count == 3:
                key[3] = unknown
                key[6] = unknown
    for i in data:
        if len(i) == 5:
            unknown = ''
            count = 0
            for letter in i:
                if letter in key[2]: count += 1
                elif letter in key[5]: count += 2
                elif letter in key[0]: continue
                else: unknown += letter
            if count == 2 and key[3] != '':
                for letter in unknown:
                    if letter not in key[3]:
                        key[1] = letter
            elif count == 1 and key[3] != '':
                for letter in unknown:
                    if letter not in key[3]:
                        key[4] = letter
    for i in data:
        if len(i) == 6:
            count = 0
            unknown = ''
            for letter in i:
                if letter in key[0]: 
                    count += 1
                    continue
                if letter in key[1]: 
                    count += 1
                    continue
                if letter in key[2]: 
                    count += 1
                    continue
                if letter in key[4]: 
                    count += 1
                    continue
                if letter in key[5]: 
                    count += 1
                    continue
                unknown += letter
            if count == 5:
                key[6] = unknown
    for letter in 'abcdefg':
        if (letter not in key[0] and letter not in key[1] and letter not in key[2] and
            letter not in key[6] and letter not in key[4] and letter not in key[5]):
            key[3] = letter
    return key

@timed
def day08A(data):
    c = Counter()
    for line in data:
        result = line.split(' | ')[1].split(' ')
        for digit in result:
            c[len(digit)] += 1
    return c[2] + c[3] + c[4] + c[7]
    
@timed
def day08B(data):
    result = 0
    for line in data:
        digits = ''
        code = line.split(' | ')[0].split(' ')
        answer = line.split(' | ')[1].split(' ')
        key = decodeKey(code)
        for digit in answer:
            if len(digit) == 2:
                digits += '1'
                continue
            elif len(digit) == 3:
                digits += '7'
                continue
            elif len(digit) == 4:
                digits += '4'
                continue
            elif len(digit) == 7:
                digits += '8'
                continue
            elif len(digit) == 6:
                if key[3] not in digit:
                    digits += '0'
                    continue
                elif key[2] not in digit:
                    digits += '6'
                    continue
                elif key[4] not in digit:
                    digits += '9'
                    continue
            elif len(digit) == 5:
                if key[2] in digit and key[5] in digit:
                    digits += '3'
                    continue
                elif key[2] in digit and key[4] in digit:
                    digits += '2'
                    continue
                elif key[1] in digit and key[5] in digit:
                    digits += '5'
                    continue
        result += int(digits)
    return result

@timed
def day08B2(data):
    answer = 0
    for line in data:
        code, decode = line.split(' | ')
        code = code.split()
        decode = decode.split()
        key = match(code)
        digs = []
        for digit in decode:
            digs.append(str(key["".join(sorted(digit))]))
        dc = int("".join(digs))
        answer += dc

    return answer

if __name__ == "__main__":
    data = importData('Day 08.txt')
    print(f"Day 08 A: {day08A(data)}")
    print(f"Day 08 B: {day08B(data)}")
    print(f"Day 08 B Alternate: {day08B2(data)}")