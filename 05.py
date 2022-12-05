from comm import timed

def importData(fileName):
    '''Pull in input data and create an array from the data'''
    with open(fileName) as file:
        lines = file.read()
        groups = lines.split("\n")
    return [x for x in groups]

def fixdata(data):
    s1 = ['D','M','S','Z','R','F','W','N']
    s2 = ['W','P','Q','G','S']
    s3 = ['W','R','V','Q','F','N','J','C']
    s4 = ['F','Z','P','C','G','D','L']
    s5 = ['T','P','S']
    s6 = ['H','D','F','W','R','L']
    s7 = ['Z','N','D','C']
    s8 = ['W','N','R','F','V','S','J','Q']
    s9 = ['R','M','S','G','Z','W','V']
    i = [[0], s1, s2, s3, s4, s5, s6, s7, s8, s9]
    return data, i

@timed
def runA(directions, data):
    for row in directions:
        x = row.split(' ')
        for _ in range(int(x[1])):
            y = data[int(x[3])].pop()
            data[int(x[5])].append(y)
    return f'{data[1][-1]}{data[2][-1]}{data[3][-1]}{data[4][-1]}{data[5][-1]}{data[6][-1]}{data[7][-1]}{data[8][-1]}{data[9][-1]}'

@timed
def runB(directions, data):
    for row in directions:
        x = row.split(' ')
        y = []
        for _ in range(int(x[1])):
            y.append(data[int(x[3])].pop())
        for _ in range(int(x[1])):
            data[int(x[5])].append(y.pop())
    return f'{data[1][-1]}{data[2][-1]}{data[3][-1]}{data[4][-1]}{data[5][-1]}{data[6][-1]}{data[7][-1]}{data[8][-1]}{data[9][-1]}'


if __name__ == "__main__":
    data, i = fixdata(importData("05.in"))
    print(f"A: {runA(data, i)}") #  ms
    data, i = fixdata(importData("05.in"))
    print(f"B: {runB(data, i)}") #  ms