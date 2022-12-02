from comm import timed
from copy import deepcopy as dp

def fix(data):
    return [[char for char in i] for i in data.split()]

def step(grid):
    ngrid = [['.' if i == '>' else i for i in x ] for x in grid]
    for x, row in enumerate(grid):
        for y, v in enumerate(row):
            if y == (len(grid[x]) - 1): 
                y = -1
            if v == '>' and grid[x][y+1] == '.':
                ngrid[x][y+1] = v
            elif v =='>' and grid[x][y+1] != '.':
                ngrid[x][y] = v
    grid = [['.' if i == 'v' else i for i in x] for x in ngrid]
    for x, row in enumerate(ngrid):
        for y, v in enumerate(row):
            if x == (len(ngrid) - 1): x = -1
            if v == 'v' and ngrid[x+1][y] == '.':
                grid[x+1][y] = v
            elif v == 'v' and ngrid[x+1][y] != '.':
                grid[x][y] = v
    return grid

@timed
def day25A(data):
    i = 0
    while True:
        i += 1
        ndata = step(data)
        if ndata ==data: return i
        data = dp(ndata)


if __name__ == "__main__":
    data = fix(open("Day 25.txt","r").read())
    print(f"Day 25 A: {day25A(data)}") # 
