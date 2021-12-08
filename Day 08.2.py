from itertools import permutations
import os
import numpy as np
from collections import Counter
from comm import timed

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

def fix(s):
    return ''.join(sorted(s))

def match(dgs2, my_dgs):
    sols = []
    for p in permutations('abcdefg'):
        mapping = {}
        for dg in my_dgs:
            my_s = []
            for l in dg:
                my_s.append(p[ord(l) - ord('a')])
            D = fix(my_s)
            MD = fix(dg)
            if D in dgs2:
                mapping[MD] = dgs2[D]
            else:
                break
        if len(mapping) == len(my_dgs):
            return mapping


def p1(lines):
    cnt = 0
    for l in lines:
        X = l.split()
        for th in X[-4:]:
            if len(th) in [2, 3, 4, 7]:
                cnt += 1
    return cnt

@timed
def p2(lines):
    dgs = {
        0 : 'abcefg',
        1 : 'cf',
        2 : 'acdeg',
        3 : 'acdfg',
        4 : 'bcdf',
        5 : 'abdfg',
        6 : 'abdefg',
        7 : 'acf',
        8 : 'abcdefg',
        9 : 'abcdfg'
    }
    dgs2 = {}
    for k, v in dgs.items():
        dgs2[v] = k
    su = 0
    for l in lines:
        ks, pin = l.split('|')
        my_dgs = ks.split()
        mapping = match(dgs2, my_dgs)
        vs = []
        for v in pin.split():
            v2 = fix(v)
            vs.append(str(mapping[v2]))
        su += int(''.join(vs))
    return su

if __name__ == "__main__":
    data = importData("Day 08.txt")
    print(p1(data))
    print(p2(data))