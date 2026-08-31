class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []

        def backtrack(curr, s, idx):
            if s > target: return
            if s == target:
                ret.append(curr)
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]: continue
                backtrack(curr + [candidates[i]], s + candidates[i], i + 1)
        backtrack([], 0, 0)
        return ret
