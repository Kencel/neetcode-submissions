from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        c = Counter(s)
        curr = set()
        needed = 0
        count = 0
        for i in range(len(s)):
            if s[i] in curr:
                needed -= 1
            else:
                curr.add(s[i])
                needed += c[s[i]] - 1
            count += 1
            if needed == 0:
                ans.append(count)
                count = 0
                curr = set()
        return ans
            
