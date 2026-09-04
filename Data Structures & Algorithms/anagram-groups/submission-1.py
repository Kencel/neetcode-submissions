class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        ans = []
        c = 0
        for s in strs:
            key = ''.join(sorted(s))
            if key in d:
                ans[d[key]].append(s)
            else:
                d[key] = c
                c += 1
                ans.append([s])
        return ans