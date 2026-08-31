# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        d = deque()
        while head:
            d.append(head)
            head = head.next
        head = d[0]
        parity = True
        while len(d) > 1:
            if parity:
                d[0].next = d[-1]
                d.popleft()
            else:
                d[-1].next = d[0]
                d.pop()
            parity = not parity
        d[0].next = None
