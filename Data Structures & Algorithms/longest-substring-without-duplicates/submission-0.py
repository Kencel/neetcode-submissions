from collections import deque, defaultdict as dd
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        curr = deque()
        count = dd(int)
        for i in range(len(s)):
            while count[s[i]] > 0:
                count[curr.popleft()] -= 1
            count[s[i]] += 1
            curr.append(s[i])
            ans = max(ans, len(curr))
        return ans
            

