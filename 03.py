from comm import timed

def importData(fileName):
    '''Pull in input data and create an array from the data'''
    with open(fileName) as file:
        lines = file.read()
        groups = lines.split("\n")
    return [x for x in groups]

def buildKey():
    '''build a key/data store for scoring'''
    key, value = {}, 1
    for letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        key[letter] = value
        value += 1
    return key

@timed
def runA(data):
    '''calculate score for items existing in both first half and last half of each string, first appearance only'''
    key = buildKey() # create scoring key
    score = 0
    for pack in data:
        a = pack[:len(pack)//2] # first half of string
        b = pack[len(pack)//2:] # second half of string
        for item in a:
            if item in b:
                score += key[item] # add to score
                break # break loop to only count first occurance per list item
    return score

@timed
def runB(data):
    '''calculate score for items shared between each group of 3 strings'''
    key = buildKey() # create scoring key
    score = 0
    for i in range(0, len(data), 3):
        a,b,c = data[i:i+3] # unpack 3 strings from array
        for letter in a:
            if letter in b and letter in c: # if letter is common between all 3
                score += key[letter] # add its priority value
                break
    return score

if __name__ == "__main__":
    data = importData("03.in")
    print(f"A: {runA(data)}") # 1.4 ms
    data = importData("03.in")
    print(f"B: {runB(data)}") # .7 ms