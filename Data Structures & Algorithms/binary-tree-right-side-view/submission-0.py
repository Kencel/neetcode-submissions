# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        s = [(root, 0)]
        while s:
            curr, d = s.pop()
            if len(ans) <= d: ans.append(curr.val)
            if curr.left: s.append((curr.left, d + 1))
            if curr.right: s.append((curr.right, d + 1))
            
        return ans