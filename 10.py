from comm import timed

class stacks:
    def importData(self, fileName):
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

    def __init__(self, file):
        self.data = self.importData(file)
        self.cycles = [20,60,100,140,180,220]
        return


    @timed
    def run(self):
        clock = 0
        x = 1
        signal = 0
        display = []
        for op, am in self.data:
            display.append('#') if (abs(x - (clock % 40)) <= 1) else display.append('.')
            clock += 1
            signal += self.check(clock, x, self.cycles)
            if op == "addx":
                display.append('#') if (abs(x - (clock % 40)) <= 1) else display.append('.')
                clock += 1
                signal += self.check(clock, x, self.cycles)
                x += am
        d = [display[:40], display[40:80], display[80:120], display[120:160], display[160:200], display[200:240]]
        self.printdisplay(d)
        return signal

    def printdisplay(self, d):
        print(*d[0])
        print(*d[1])
        print(*d[2])
        print(*d[3])
        print(*d[4])
        print(*d[5])
        return

    def check(self, clock, x, cycles):
        if clock in cycles:
            return clock * x
        else:
            return 0


if __name__ == "__main__":
    puzzle = stacks('10.in')
    print(f"Part One: {puzzle.run()}") # T: 22  ms 
    