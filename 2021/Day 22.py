from comm import timed
from collections import defaultdict

def parse(data):
    final = []
    for row in data:
        i, result = row.split(","), []
        x = range(int(i[1]),int(i[2])+1)
        y = range(int(i[3]),int(i[4])+1)
        z = range(int(i[5]),int(i[6])+1)
        result = [1 if i[0] == "on" else 0, x,y,z]
        final.append(result)
    return final

@timed
def day22A(data, init = 1):
    # max of 50, min of -50
    cubes = defaultdict(int)
    for row in data:
        v = row[0]
        if init:
            skip = [1, 1, 1]
            for i in range(-50,51):
                if i in row[1]: skip[0] = 0
                if i in row[2]: skip[1] = 0
                if i in row[3]: skip[2] = 0
                if sum(skip) == 0:
                    break
            if sum(skip): continue
        for x in row[1]:
            for y in row[2]:
                for z in row[3]:
                    a = ",".join([str(i) for i in (x,y,z)])
                    cubes[a] = v

    return sum(cubes.values())

@timed
def day22B(data):
    
    return

if __name__ == "__main__":
    data = parse(open("Day 22.txt","r").read().replace(" x=",",").replace("y=","").replace("z=","").replace("..",",").split("\n"))
    print(f"Day 11 A: {day22A(data)}") # 623748
    # print(f"Day 11 B: {day22A(data, 0)}") # Part 2 doesn't work.  Runs out of RAM.
