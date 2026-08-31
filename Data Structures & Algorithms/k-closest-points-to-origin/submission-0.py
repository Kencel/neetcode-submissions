class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            heapq.heappush(h, (math.sqrt(x ** 2 + y ** 2), x, y))

        ret = []
        for i in range(k):
            temp = heapq.heappop(h)
            ret.append([temp[1], temp[2]])
        return ret