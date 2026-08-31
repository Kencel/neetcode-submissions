class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        prev = -2
        curr = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == prev: continue
            if nums[i] == prev + 1:
                curr += 1
            else:
                curr = 1
            ans = max(ans, curr)
            prev = nums[i]
        return ans



        
        