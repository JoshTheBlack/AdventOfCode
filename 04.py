from comm import timed

def importData(fileName):
    '''Pull in input data and create an array from the data'''
    with open(fileName) as file:
        lines = file.read()
        groups = lines.split("\n")
    return [x for x in groups]

@timed
def runA(data):
   
    return 

@timed
def runB(data):
  
    return 

if __name__ == "__main__":
    data = importData("04.in")
    print(f"A: {runA(data)}") #  ms
    data = importData("04.in")
    print(f"B: {runB(data)}") #  ms