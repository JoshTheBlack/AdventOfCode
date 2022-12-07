from collections import defaultdict as dd
import pathlib
from comm import timed

def importData(fileName):
    '''Pull in input data and create an array of round data'''
    with open(fileName) as file:
        lines = file.read()
    return lines.strip().split('\n')

@timed
def run(inputdata, d = False):
    fs, cwd = dd(int), pathlib.Path("/")
    for line in inputdata:
        if line.startswith("$"):
            _, cmd, *args = line.split()
            if cmd == "cd":
                if args[0] == "/":
                    cwd = pathlib.Path("/")
                elif args[0] == "..":
                    cwd = cwd.parent
                else:
                    cwd = cwd / args[0]
        elif line.startswith("dir"):
            pass
        else:
            _cwd = cwd / line.split()[1]
            while _cwd != pathlib.Path("/"):
                _cwd = _cwd.parent
                fs[_cwd] += int(line.split()[0])
    
    if not d:
        return sum(size for size in fs.values() if size <= 100_000)
    else:
        return min(size for size in fs.values() if size >= fs.get(pathlib.Path("/")) - 40_000_000)

if __name__ == '__main__':
    inputdata = importData('07.in')
    print(f"Part 1: {run(inputdata)}")
    print(f"Part 2: {run(inputdata, 1)}")
# This one stumped me.  This is modified code from reddit.