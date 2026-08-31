# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a = []
        b = []
        a.append(p)
        b.append(q)
        while a and b:
            curr_a = a.pop()
            curr_b = b.pop()
            if not curr_a and not curr_b: continue
            if not curr_a: return False
            if not curr_b: return False
            if curr_a.val != curr_b.val: return False
            a.append(curr_a.left)
            a.append(curr_a.right)
            b.append(curr_b.left)
            b.append(curr_b.right)
        return True