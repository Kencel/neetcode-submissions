class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        if ans <= 0: return ans
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            temp = max(temp, 0)
            ans = max(temp, ans)
        return ans