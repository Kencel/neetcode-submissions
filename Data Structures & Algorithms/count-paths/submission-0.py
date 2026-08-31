from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = (m + n - 2)
        r = min(m, n) - 1
        ans = 1
        for i in range(r):
            ans *= a
            a -= 1
        return ans // factorial(r)