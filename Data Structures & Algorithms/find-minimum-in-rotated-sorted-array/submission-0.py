class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = -len(nums)
        r = len(nums)
        ans = nums[0]
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] < ans:
                ans = nums[m]
                r = m
            else:
                l = m
        return ans