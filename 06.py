from comm import timed

class Puzzle:
    def importData(self, fileName):
        '''Pull in input data and create an array from the data'''
        with open(fileName) as file:
            lines = file.read()
        return lines

    def __init__(self, file):
        self.data = self.importData(file)
        return

    @timed
    def test(self, length = 4):
        '''Find index of the last character of first instance of a variable (length) distinct consecutive characters'''
        for i in range(length, len(self.data)):
            y = set(f"{self.data[i-length:i]}")
            if len(y) == length: break
        return i

    @timed
    def run(self):
        print(f"Part one: {self.test()}")
        print(f"Part two: {self.test(14)}")


if __name__ == "__main__":
    day06 = Puzzle('06.in')
    day06.run() # A: 0.9, B: 4.0, T: 6.2 