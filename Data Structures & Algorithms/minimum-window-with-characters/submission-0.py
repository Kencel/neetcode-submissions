from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        curr = Counter()
        l = 0
        r = 0
        mn = float('inf')
        ans = None
        while r < len(s):
            curr[s[r]] += 1
            r += 1
            for char in target:
                if target[char] > curr[char]:
                    break
            else:
                while curr[s[l]] - 1 >= target[s[l]]:
                    curr[s[l]] -= 1
                    l += 1
                if r - l < mn:
                    mn = r - l
                    ans = (l, r)
        
        if not ans:
            return ""
        return s[ans[0]:ans[1]]
