class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        s = []
        for i in range(len(temperatures)):
            if not s:
                s.append(i)
                continue
            while s and temperatures[s[-1]] < temperatures[i]:
                temp = s.pop()
                ans[temp] = i - temp
            s.append(i)
        return ans