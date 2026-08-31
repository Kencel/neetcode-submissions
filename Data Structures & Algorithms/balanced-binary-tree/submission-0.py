# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth = dict()
        def getDepth(node):
            if not node: return 0
            if node in depth: return depth[node]
            depth[node] = max(getDepth(node.left), getDepth(node.right)) + 1
            return depth[node]
        getDepth(root)
        s = [root]
        while s:
            curr = s.pop()
            if not curr: continue
            if abs(getDepth(curr.left) - getDepth(curr.right)) > 1:
                return False
            s.append(curr.left)
            s.append(curr.right)
        return True