from comm import timed

def importData(fileName):
    '''Pull in input data and create an array of round data'''
    with open(fileName) as file:
        lines = file.read()
        groups = lines.split("\n")
    return [x for x in groups]

@timed
def runA(data):
    key = {"A X": 3, "A Y": 6, "A Z": 0, "B X": 0, "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3} # round scoring key
    score = 0
    for round in data:
        us = ord(round[2]) - 87 # Assign value 1 for Rock, 2 for Paper, 3 for Scissors
        score += key[round] + us # Add value for sign used, and score for win/lose/draw (6/0/3)
    return score

@timed
def runB(data):
    key = {"A X": 3, "A Y": 1, "A Z": 2, "B X": 1, "B Y": 2, "B Z": 3, "C X": 2, "C Y": 3, "C Z": 1} # sign decision matrix
    score = 0
    for round in data:
        us = ord(round[2]) - 88 # 0 for lose, 1 for draw, 2 for win
        score += key[round] + (us * 3) # add value for the sign used and score for win/lose/draw
    return score

if __name__ == "__main__":
    data = importData("02.in")
    print(f"A: {runA(data)}") # 2.5 ms
    data = importData("02.in")
    print(f"B: {runB(data)}") # 2.7 ms