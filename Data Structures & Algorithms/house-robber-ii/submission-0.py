class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [0, 0, 0]
        for i in range(len(nums) - 1):
            dp.append(max(dp[i], dp[i + 1]) + nums[i])
        ans = max(dp[-1], dp[-2])

        dp = [0, 0, 0]
        for i in range(1, len(nums)):
            dp.append(max(dp[i], dp[i - 1]) + nums[i])
        ans = max(ans, max(dp[-1], dp[-2]))
        return ans