# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        d = deque()
        curr = head
        while curr:
            d.append(curr)
            curr = curr.next
        parity = True
        while len(d) > 1:
            if parity:
                node = d.popleft()
                node.next = d[-1]
            else:
                node = d.pop()
                node.next = d[0]
            parity = not parity
        d[0].next = None
