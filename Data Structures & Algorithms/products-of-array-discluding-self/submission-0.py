class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)
        elif nums.count(0) == 1:
            p = 1
            idx = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    p *= nums[i]
                else:
                    idx = i
            ans = [0] * len(nums)
            ans[idx] = p
            return ans
        
        p = 1
        for i in range(len(nums)):
            p *= nums[i]
        ans = []
        for i in range(len(nums)):
            ans.append(p // nums[i])
        return ans
            

        