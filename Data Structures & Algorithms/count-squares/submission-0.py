from collections import defaultdict as dd
class CountSquares:

    def __init__(self):
        self.x = dd(set)
        self.xy = dd(int)

    def add(self, point: List[int]) -> None:
        self.x[point[0]].add(point[1])
        self.xy[point[0], point[1]] += 1

    def count(self, point: List[int]) -> int:
        ret = 0

        for i in self.x[point[0]]:
            if i == point[1]: continue
            d = abs(point[1] - i)
            ret += self.xy[point[0], i] * self.xy[point[0] - d, point[1]] * self.xy[point[0] - d, i]
            ret += self.xy[point[0], i] * self.xy[point[0] + d, point[1]] * self.xy[point[0] + d, i]

        return ret