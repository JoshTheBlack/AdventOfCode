from comm import timed

class stacks:
    def importData(self, fileName):
        '''Pull in input data and create an array from the data'''
        with open(fileName) as file:
            lines = file.read()
            groups = lines.split("\n")
        return [x for x in groups]

    def __init__(self, file):
        s1 = ['D','M','S','Z','R','F','W','N']
        s2 = ['W','P','Q','G','S']
        s3 = ['W','R','V','Q','F','N','J','C']
        s4 = ['F','Z','P','C','G','D','L']
        s5 = ['T','P','S']
        s6 = ['H','D','F','W','R','L']
        s7 = ['Z','N','D','C']
        s8 = ['W','N','R','F','V','S','J','Q']
        s9 = ['R','M','S','G','Z','W','V']
        self.a = [[0], [*s1], [*s2], [*s3], [*s4], [*s5], [*s6], [*s7], [*s8], [*s9]] # unpack to make individual copy instead of references 
        self.b = [[0], [*s1], [*s2], [*s3], [*s4], [*s5], [*s6], [*s7], [*s8], [*s9]]
        self.directions = self.importData(file)
        return

    def report(self):
        return f'{self.a[1][-1]}{self.a[2][-1]}{self.a[3][-1]}{self.a[4][-1]}{self.a[5][-1]}{self.a[6][-1]}{self.a[7][-1]}{self.a[8][-1]}{self.a[9][-1]}'

    @timed
    def runA(self):
        '''Rearrange items from the end of lists one at a time according to directions'''
        for row in self.directions:
            x = row.split(' ') # split direction into array
            for _ in range(int(x[1])):
                y = self.a[int(x[3])].pop() # remove item from source
                self.a[int(x[5])].append(y) # place item on destination
        return self.report()

    @timed
    def runB(self):
        '''Rearrange stacks of items according to directions'''
        self.a = self.b.copy()
        for row in self.directions:
            x = row.split(' ') # split direction into array
            self.a[int(x[5])].extend(self.a[int(x[3])][-int(x[1]):]) # copy items from source and extend onto destination
            self.a[int(x[3])] = self.a[int(x[3])][:-int(x[1])] # remove items from source
        return self.report()

    @timed
    def run(self):
        print(self.runA())
        print(self.runB())


if __name__ == "__main__":
    stackA = stacks('05.in')
    stackA.run() # A: 4.0 ms, B: 2.3 ms, T: 7.3 MS 