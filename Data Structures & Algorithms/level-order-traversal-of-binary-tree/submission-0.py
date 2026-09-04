# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        s = [(root, 0)]
        while s:
            curr, d = s.pop()
            if not curr: continue
            if len(ans) <= d: ans.append(list())
            ans[d].append(curr.val)
            s.append((curr.right, d + 1))
            s.append((curr.left, d + 1))
        return ans