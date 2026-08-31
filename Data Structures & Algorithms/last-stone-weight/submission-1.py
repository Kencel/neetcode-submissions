from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for i in range(len(stones)):
            heappush(h, -stones[i])
        
        while len(h) > 1:
            x, y = heappop(h), heappop(h)
            if x != y:
                heappush(h, -abs(x - y))

        if not h: return 0
        return -h[0]