from collections import deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters = set(s)
        ans = 0 
        for char in characters:
            curr = k
            q = deque()
            print(char)
            for c in s:
                q.append(c)
                if c != char:
                    if curr > 0:
                        curr -= 1
                    else:
                        temp = q.popleft()
                        while temp == char:
                            temp = q.popleft()
                        if not q: curr += 1
                print(*q, k)
                ans = max(ans, len(q))
        return ans