from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        l = [height[0]]
        r = deque([height[-1]])
        for i in range(1, len(height)):
            l.append(max(l[-1], height[i]))
        for i in range(len(height) - 2, -1, -1):
            r.appendleft(max(r[0], height[i]))
        r = list(r)
        ans = 0 
        for i in range(1, len(height) - 1):
            ans += max(0, min(l[i - 1], r[i + 1]) - height[i])
        return ans
            