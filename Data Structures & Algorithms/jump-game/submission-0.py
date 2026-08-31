class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[0]
        for i in range(len(nums) - 1):
            curr = max(curr - 1, nums[i])
            if curr < 1: return False
        return True