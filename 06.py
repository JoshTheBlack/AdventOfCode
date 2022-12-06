from comm import timed

class Puzzle:
    def importData(self, fileName):
        '''Pull in input data and create an array from the data'''
        with open(fileName) as file:
            lines = file.read()
            groups = lines.split("\n")
        return [x for x in groups]

    def __init__(self, file):
        self.data = self.importData(file)
        return

    @timed
    def runA(self):
        '''Find index of the last character of first instance of 4 distinct consecutive characters'''
        x = self.data[0]
        for i in range(len(self.data[0])):
            y = set(f"{x[i]}{x[i+1]}{x[i+2]}{x[i+3]}")
            if len(y) == 4: break
        return i+4

    @timed
    def runB(self):
        '''Find index of the last character of first instance of 14 distinct consecutive characters'''
        x = self.data[0]
        for i in range(len(self.data[0])):
            y = set(f"{x[i]}{x[i+1]}{x[i+2]}{x[i+3]}{x[i+4]}{x[i+5]}{x[i+6]}{x[i+7]}{x[i+8]}{x[i+9]}{x[i+10]}{x[i+11]}{x[i+12]}{x[i+13]}")
            if len(y) == 14: break
        return i+14

    @timed
    def run(self):
        print(self.runA())
        print(self.runB())


if __name__ == "__main__":
    day06 = Puzzle('06.in')
    day06.run() # A: 1.5, B: 11, T: 13.9 