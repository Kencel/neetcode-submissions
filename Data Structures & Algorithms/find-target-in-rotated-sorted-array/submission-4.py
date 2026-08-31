class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > nums[0]:
                l = m
            else:
                r = m
        if target >= nums[0]:
            r = l + 1
            l = 0
        else:
            r = len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > target:
                r = m
            else:
                l = m
        if l >= len(nums) or nums[l] != target: return -1
        return l
