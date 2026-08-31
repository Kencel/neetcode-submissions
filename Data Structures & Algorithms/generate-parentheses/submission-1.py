class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        idx = [set([""])]
        for length in range(1, n + 1): 
            curr = set()
            for i in idx[length - 1]:
                curr.add(i + "()")
                curr.add("()" + i)
                curr.add("(" + i + ")")
            for i in range(2, length // 2 + 1):
                for l in idx[i]:
                    for r in idx[length - i]:
                        curr.add(l + r)
                        curr.add(r + l)
            idx.append(curr)
        return list(idx[n])