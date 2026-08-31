class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        def backtrack(curr, idx):
            ret.append(curr)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]: continue
                backtrack(curr + [nums[i]], i + 1)
        backtrack([], 0)

        return ret