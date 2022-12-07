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
    def test(self, length = 4):

        return i

    @timed
    def run(self):
        print(f"Part one: {self.test()}")
        #print(f"Part two: {self.test(14)}")


if __name__ == "__main__":
    day06 = Puzzle('07.in')
    day06.run()