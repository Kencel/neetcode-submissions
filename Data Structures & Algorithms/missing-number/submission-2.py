class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        m = max(nums)
        if m < len(nums): return m + 1
        for i in range(m + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans