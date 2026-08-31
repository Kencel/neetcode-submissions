from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles) + 1
        while r - l > 1:
            m = (r + l) // 2
            curr = 0
            for i in range(len(piles)):
                curr += ceil(piles[i] / m)
            print(m, curr)
            if curr > h:
                l = m
            else:
                r = m
        return r