import os
import numpy as np
from comm import timed
from skimage import graph

def importData(fileName):
    return np.transpose(np.loadtxt(os.path.join(os.sys.path[0], fileName), dtype=str, skiprows=0, delimiter="\n"))

def fix(data):
    return np.array([list(z) for z in data]).astype('i')


@timed
def day15A(data):
    cost = graph.MCP(data,fully_connected=False)
    cost.find_costs(starts=[(0,0)])
    return sum([data[loc] for loc in cost.traceback((99,99))[1:]])

@timed
def day15B(maze):
    large = maze
    for i in range(1,5):
        large = np.concatenate([large,(maze+i)],axis=1)
    maze = large
    for i in range(1,5):
        maze = np.concatenate([maze,(large+i)])
    maze %= 9
    maze[maze==0] = 9
    cost = graph.MCP(maze,fully_connected=False)
    cost.find_costs(starts=[(0,0)])
    return sum([maze[loc] for loc in cost.traceback((499,499))[1:]])
  

if __name__ == "__main__":
    data = fix(importData("Day 15.txt"))
    print(f"Day 12 A: {day15A(data)}") # 626
    data = fix(importData("Day 15.txt"))
    print(f"Day 12 B: {day15B(data)}") # 2966