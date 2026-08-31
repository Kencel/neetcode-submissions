from collections import defaultdict as dd
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        target = dd(int)
        for s in s1:
            target[s] += 1
        curr = dd(int)
        for i in range(len(s1)):
            curr[s2[i]] += 1
        for i in range(len(s1), len(s2)):
            if target == curr: return True
            prev = s2[i - len(s1)]
            if curr[prev] == 1:
                curr.pop(prev)
            else:
                curr[prev] -= 1
            curr[s2[i]] += 1
        return target == curr
        