from comm import timed

def importData(fileName):
    '''Pull in input data and create an array from the data'''
    with open(fileName) as file:
        lines = file.read()
        groups = lines.split("\n")
    return [x for x in groups]

def fixdata(data):
    out = []
    for line in data:
        x = line.split(',')
        a, b = x[0].split('-'), x[1].split('-')
        out.append([range(int(a[0]),int(a[1])), range(int(b[0]),int(b[1]))])
    return out

@timed
def runA(data):
    count = 0
    for a in data:
        if a[0].start <= a[1].start and a[0].stop >= a[1].stop or a[1].start <= a[0].start and a[1].stop >= a[0].stop:
            count += 1
    return count

@timed
def runB(data):
    count = 0
    for line in data:
        if line[0].start <= line[1].stop and line[1].start <= line[0].stop:
            count += 1
    return count

if __name__ == "__main__":
    data = fixdata(importData("04.in"))
    print(f"A: {runA(data)}") # 1.44 ms
    data = fixdata(importData("04.in"))
    print(f"B: {runB(data)}") # .85 ms