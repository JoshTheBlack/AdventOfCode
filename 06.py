from comm import timed

class Puzzle:
    def importData(self, fileName):
        '''Pull in input data and create an array from the data'''
        with open(fileName) as file:
            lines = file.read()
            groups = lines.split("\n")
        return [x for x in groups]

    def __init__(self, file):
        
        return

    @timed
    def runA(self):
    
        return 

    @timed
    def runB(self):
       
        return 

    @timed
    def run(self):
        print(self.runA())
        #print(self.runB())


if __name__ == "__main__":
    day06 = Puzzle('05.in')
    day06.run() # A: , B: , T:  