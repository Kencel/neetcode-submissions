from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        mx = [0] * 26
        for i in range(len(s)):
            mx[ord(s[i]) - ord("a")] = i
        
        curr = 0
        end = 0
        for i in range(len(s)):
            curr += 1
            end = max(end, mx[ord(s[i]) - ord('a')])
            if i == end:
                ans.append(curr)
                curr = 0
        return ans

            
