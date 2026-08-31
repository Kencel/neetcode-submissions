from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums) + 1):
            c = combinations(nums, i)
            for subset in c:
                ans.append(list(subset))
        return ans
        