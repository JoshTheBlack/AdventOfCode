from comm import timed
import itertools as it
import math
import sys

class Puzzle:
    def importData(self, fileName):
        '''Pull in input data and create an array from the data'''
        with open(fileName) as file:
            lines = file.read()
            groups = lines.split("\n")
        return [[int(x) for x in y] for y in groups]

    def __init__(self, file):
        self.data = self.importData(file)
        return

    @timed
    def test(self, scenic = False):
        trees = self.data
        w, h = len(trees[0]), len(trees)
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
]
        visible_n, best_scenic_score = 0, -math.inf
        for x, y in it.product(range(w), range(h)):
            visible, scenic_score = False, 1
            for dx, dy in directions:
                x0, y0 = x, y
                for s0 in it.count(0):
                    x0, y0 = x0 + dx, y0 + dy
                    if 0 <= x0 < w and 0 <= y0 < h:
                        if trees[y0][x0] >= trees[y][x]:
                            s0 = s0 + 1
                            break
                    else:
                        visible = True
                        break
                
                scenic_score *= s0
            
            visible_n = visible_n + 1*visible
            best_scenic_score = max(best_scenic_score, scenic_score)
        return visible_n if not scenic else best_scenic_score

    @timed
    def run(self):
        print(f"Part one: {self.test()}")
        print(f"Part two: {self.test(True)}")


if __name__ == "__main__":
    day08 = Puzzle('08.in')
    day08.run() 




