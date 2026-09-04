# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def good(curr, mx):
            if not curr: return 0
            ret = 0
            if curr.val >= mx:
                ret += 1
                mx = curr.val
            ret += good(curr.left, mx)
            ret += good(curr.right, mx)
            return ret
        
        return good(root, -100)