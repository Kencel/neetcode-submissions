class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for i in range(len(nums)):
            dp.append(max(dp[i], dp[i + 1]) + nums[i])
        return max(dp)