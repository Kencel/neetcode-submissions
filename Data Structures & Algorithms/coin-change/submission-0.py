class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        INF = 10 ** 9
        for i in range(1, amount + 1):
            mn = INF
            for j in coins:
                if i - j < 0: continue
                if dp[i - j] != -1:
                    mn = min(mn, dp[i - j])
            if mn == INF:
                dp.append(-1)
            else:
                dp.append(mn + 1)
        return dp[amount]