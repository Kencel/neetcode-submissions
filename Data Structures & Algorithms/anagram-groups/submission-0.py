from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        taken = set()
        ans = []
        for i in range(len(strs)):
            if i in taken: continue
            curr = [strs[i]]
            c = Counter(strs[i])
            for j in range(i + 1, len(strs)):
                if Counter(strs[j]) == c:
                    curr.append(strs[j])
                    taken.add(j)
            ans.append(curr)
        return ans
        