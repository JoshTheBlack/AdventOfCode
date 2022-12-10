# from comm import timed
# from defaultlist import defaultlist

# class stacks:
#     def importData(self, fileName):
#         '''Pull in input data and create an array from the data'''
#         with open(fileName) as file:
#             lines = file.read()
#             groups = lines.split("\n")
#         return groups

#     def __init__(self, file):
#         self.data = self.importData(file)
#         return


#     @timed
#     def run(self):
#         d = self.data
#         grid = defaultlist(lambda: defaultlist(0))
#         grid[100][100]
#         x, y = 50, 50
#         tx, ty = x, y
#         grid[tx][ty] = 1
#         key = {'D': (1,0), 'U': (-1,0), 'L': (0,-1), 'R': (0,1)}
#         for move in d:
#             i,j = key[move[0]]
#             for k in range(int(move[3])):
#                 x += i
#                 y += j
#                 if 
#                 grid[a][b] = 1
#             print()
#         return



# if __name__ == "__main__":
#     puzzle = stacks('09.in')
#     puzzle.run() # A:  ms, B:  ms, T:  ms 
import math

def main(input: str) -> (int | str | None):
    segments = input.rstrip("\n").split("\n\n")
    knots = [(0, 0)] * 10
    lines = segments[0].split("\n")
    tails = {(0, 0)}
    for line in lines:
        d, dist_ = line.split()
        dx, dy = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}[d]
        for _ in range(int(dist_)):
            knots[0] = knots[0][0] + dx, knots[0][1] + dy
            for i in range(len(knots) - 1):
                while 1:
                    x_diff = knots[i][0] - knots[i + 1][0]
                    y_diff = knots[i][1] - knots[i + 1][1]
                    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
                        break

                    mov_x = int(math.copysign(min(1, abs(x_diff)), x_diff))
                    mov_y = int(math.copysign(min(1, abs(y_diff)), y_diff))
                    knots[i + 1] = knots[i + 1][0] + mov_x, knots[i + 1][1] + mov_y
                    if i == 8:
                        tails.add(knots[i + 1])

    return len(tails)

with open('09.in') as file:
    i = file.read()

print(main(i))