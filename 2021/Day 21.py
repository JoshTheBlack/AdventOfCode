from comm import timed
from collections import Counter


@timed
def day21A(data):
    score = [1,2,3,4,5,6,7,8,9,10]
    turn = 0
    p1,p2 = 0,0
    for i in range(3,10000,3):

        move = i*3-3
        turn += 1
        if turn % 2:
            move += data[0] - 1
            data[0] = score[move % 10]
            p1 += data[0]
        else:
            move += data[1] - 1
            data[1] = score[move % 10]
            p2 += data[1]
        if p2 >= 1000:
            return p1 * i
        elif p1 >= 1000:
            return p2 * i
    return "ERROR"

@timed
def day21B(data):
    DP = {}
    rolls = [1, 2, 3]
    C = Counter()
    for a in rolls:
        for b in rolls:
            for c in rolls:
                C[a + b + c] += 1
    
    def solve(who, pos1, pos2, p1, p2):
        T = who, pos1, pos2, p1, p2
        if T in DP:
            return DP[T]
        if p1 >= 21:
            return (1, 0)
        if p2 >= 21:
            return (0, 1)
        V = [0, 0]
        for k, no in C.items():
            if who == 0:
                np = (pos1 + k - 1)%10 + 1
                w1, w2 = solve(1, np, pos2, p1 + np, p2)
            else:
                np = (pos2 + k - 1)%10 + 1
                w1, w2 = solve(0, pos1, np, p1, p2 + np)
            V[0] += w1*no
            V[1] += w2*no
        DP[T] = V
        return V
    V = solve(0, 4, 3, 0, 0)
    
    return max(V)
    

if __name__ == "__main__":
    players = {0:4,1:3}
    print(f"Day 21 A: {day21A(players)}") # 734820
    print(f"Day 21 B: {day21B(players)}") # 193170338541590
    # Code for part 2 shamelessly stolen from elsewhere.  Code for part 1 is my own.