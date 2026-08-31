# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        if root.left and root.right:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        elif root.left:
            root.right = self.invertTree(root.left)
            root.left = None
        else:
            root.left = self.invertTree(root.right)
            root.right = None

        return root