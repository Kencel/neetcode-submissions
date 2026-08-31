class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        def backtrack(curr, remaining):
            if not remaining:
                ret.append(curr)
                return
            new = set(remaining)
            for i in remaining:
                new.remove(i)
                backtrack(curr + [i], new)
                new.add(i)

        backtrack([], set(nums))
        return ret
