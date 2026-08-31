class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = nums[0]
        curr = 1
        neg = 0
        for i in range(len(nums)):
            if curr == 0: curr = 1
            curr *= nums[i]
            if curr < 0 and neg == 0:
                neg = curr
            elif curr < 0:
                ret = max(ret, curr // neg)
            elif curr == 0:
                neg = 0
            ret = max(ret, curr)

        return ret