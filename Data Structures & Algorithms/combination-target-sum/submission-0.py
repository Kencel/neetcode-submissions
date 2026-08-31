class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        def backtrack(curr, s, idx):
            if s > target: return
            if s == target:
                ret.append(curr)
                return
            for i in range(idx, len(nums)):
                backtrack(curr + [nums[i]], s + nums[i], i)
        backtrack([], 0, 0)
        return ret