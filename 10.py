from comm import timed


def importData(fileName):
    '''Pull in input data and create an array from the data'''
    with open(fileName) as file:
        lines = file.read()
        groups = lines.split("\n")
        data = []
        for line in groups:
            if line == 'noop':
                data.append(['noop',0])
                continue
            x,y = line.split()
            data.append([x,int(y)])
    return data

@timed
def run(data):
    clock = 0
    x = 1
    total = 0

    def cycle():
        nonlocal clock, total, x
        clock += 1
        if clock in {20,60,100,140,180,220}:
            total += clock * x  
        print("x " if abs(clock % 40 - x - 1) <= 1 else ". ", end="")
        if clock % 40 == 0: print()

    for op, am in data:
        match op:
            case "noop":
                cycle()
            case "addx":
                cycle()
                cycle()
                x += am
    
    return total


if __name__ == "__main__":
    d = importData('10.in')
    print(f"Part One: {run(d)}") # T: 22  ms 

