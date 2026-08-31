# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth = dict()
        self.ret = True
        def getDepth(node):
            global ret
            if not node: return 0
            l = getDepth(node.left)
            r = getDepth(node.right)
            if abs(l - r) > 1: self.ret = False
            return max(l, r) + 1
        getDepth(root)
        return self.ret