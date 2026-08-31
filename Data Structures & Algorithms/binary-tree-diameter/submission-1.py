# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    depth = dict()

    def calculateDepth(node):
        if not node: return 0
        Solution.depth[node] = max(Solution.calculateDepth(node.left), Solution.calculateDepth(node.right)) + 1
        return Solution.depth[node]

    def diameter(root):
        if not root: return 0
        s = 0
        if root.left:
            s += Solution.depth[root.left]
        if root.right:
            s += Solution.depth[root.right]
        return max((s, Solution.diameter(root.left), Solution.diameter(root.right)))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        Solution.depth = dict()
        Solution.calculateDepth(root)
        return Solution.diameter(root)
        